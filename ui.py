import json
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QComboBox, QPushButton, QFileDialog, QLineEdit
from installer import InstallThread
from downloader import YouTubeDownloader
import sys

CONFIG_FILE = "config.json"  # File to store settings like download folder

class YouTubeDownloaderUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouDon - YouTube Downloader")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.status_label = QLabel("Checking dependencies...")
        layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.url_label = QLabel("Enter YouTube URL:")
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.format_label = QLabel("Select Download Type:")
        layout.addWidget(self.format_label)

        self.format_dropdown = QComboBox()
        self.format_dropdown.addItems(["audio", "video"])
        layout.addWidget(self.format_dropdown)

        self.playlist_label = QLabel("Download Type (Video or Playlist):")
        layout.addWidget(self.playlist_label)

        self.playlist_dropdown = QComboBox()
        self.playlist_dropdown.addItems(["single", "playlist"])
        layout.addWidget(self.playlist_dropdown)

        self.folder_label = QLabel("Download Folder: Not selected")
        layout.addWidget(self.folder_label)

        self.folder_button = QPushButton("Choose Download Folder")
        self.folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_button)

        self.download_button = QPushButton("Download")
        self.download_button.setEnabled(False)  # Will be enabled after dependencies check
        layout.addWidget(self.download_button)

        self.setLayout(layout)

        # Load saved settings (default folder)
        self.download_folder = self.load_config()

        if self.download_folder:
            self.folder_label.setText(f"Download Folder: {self.download_folder}")

        # Run the dependency installation in a background thread
        self.install_thread = InstallThread()
        self.install_thread.progress_update.connect(self.update_progress)
        self.install_thread.status_update.connect(self.update_status)
        self.install_thread.button_enable.connect(self.enable_download_button)
        self.install_thread.start()

        # Initialize downloader
        self.downloader = YouTubeDownloader()
        self.downloader.set_download_button(self.download_button)

        # Connect download button to downloader
        self.download_button.clicked.connect(self.download_video)

    def update_progress(self, percentage):
        """Update progress bar."""
        self.progress_bar.setValue(percentage)

    def update_status(self, status):
        """Update the status label."""
        self.status_label.setText(status)

    def enable_download_button(self):
        """Enable the download button when dependencies are installed."""
        self.download_button.setEnabled(True)

    def select_folder(self):
        """Allow the user to choose a download folder and save it."""
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", "")
        if folder:
            self.download_folder = folder
            self.folder_label.setText(f"Download Folder: {folder}")
            self.save_config(folder)  # Save the selected folder

    def save_config(self, folder):
        """Save the selected folder to a config file."""
        config = {"download_folder": folder}
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file)

    def load_config(self):
        """Load the saved download folder from config file."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                config = json.load(file)
                return config.get("download_folder", "")
        return ""

    def download_video(self):
        """Handle video download."""
        url = self.url_input.text()
        format_choice = self.format_dropdown.currentText()
        download_type = self.playlist_dropdown.currentText()

        # Use the saved download folder or prompt the user to select one
        if hasattr(self, 'download_folder') and self.download_folder:
            download_folder = self.download_folder
        else:
            self.select_folder()  # Prompt user to select a folder
            download_folder = self.download_folder

        status = self.downloader.download_video(url, format_choice, download_type, download_folder)
        self.status_label.setText(status)
