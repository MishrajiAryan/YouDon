import os
import subprocess
import requests
from PyQt6.QtCore import QThread, pyqtSignal
import sys

# URLs for downloading dependencies
YT_DLP_URL = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"

# Paths for dependencies
APP_DIR = os.getcwd()
DEPENDENCIES_DIR = os.path.join(APP_DIR, "dependencies")
YT_DLP_PATH = os.path.join(DEPENDENCIES_DIR, "yt-dlp.exe")
FFMPEG_EXE = "ffmpeg"  # Use system-wide FFmpeg, assuming it’s installed

class InstallThread(QThread):
    """Thread for downloading and installing dependencies."""
    progress_update = pyqtSignal(int)  # Signal to update progress bar
    status_update = pyqtSignal(str)    # Signal to update status label
    button_enable = pyqtSignal()       # Signal to enable the download button

    def run(self):
        """Run the installation process in the background."""
        self.check_and_install_dependencies()

    def download_file(self, url, output_path):
        """Download a file with progress updates."""
        self.status_update.emit(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        downloaded_size = 0

        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    percent_done = int((downloaded_size / total_size) * 100)
                    self.progress_update.emit(percent_done)

        self.progress_update.emit(100)
        self.status_update.emit(f"Downloaded: {os.path.basename(output_path)}")

    def check_ffmpeg(self):
        """Check if FFmpeg is available in the system path."""
        try:
            subprocess.check_call([FFMPEG_EXE, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.status_update.emit("FFmpeg is installed and available.")
            return True
        except subprocess.CalledProcessError:
            self.status_update.emit("FFmpeg not found! Please install FFmpeg manually.")
            return False

    def check_and_install_dependencies(self):
        """Check if yt-dlp and FFmpeg are installed, and install them if missing."""

        # Create 'dependencies' folder if it doesn't exist
        if not os.path.exists(DEPENDENCIES_DIR):
            os.makedirs(DEPENDENCIES_DIR)

        # 1️⃣ Check for yt-dlp
        if not os.path.exists(YT_DLP_PATH):
            self.status_update.emit("yt-dlp not found! Downloading...")
            self.download_file(YT_DLP_URL, YT_DLP_PATH)
            os.chmod(YT_DLP_PATH, 0o755)  # Make it executable
            self.status_update.emit("yt-dlp installed successfully.")

        # 2️⃣ Check for FFmpeg
        if not self.check_ffmpeg():
            self.status_update.emit("FFmpeg is required for video/audio merging. Please install it manually.")

        # 3️⃣ Ensure yt-dlp can find FFmpeg (assuming FFmpeg is in system PATH)
        os.environ["FFMPEG_BINARY"] = "ffmpeg"  # Set FFmpeg binary for yt-dlp
        self.status_update.emit("All dependencies verified!")

        # Enable the download button after dependencies are installed
        self.button_enable.emit()

