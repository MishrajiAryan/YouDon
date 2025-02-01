import subprocess
import os
from PyQt6.QtWidgets import QLabel

class YouTubeDownloader:
    def __init__(self):
        self.download_button = None  # To be set by the UI

    def set_download_button(self, button):
        self.download_button = button

    def download_video(self, url, format_choice, download_type, download_folder):
        """Download YouTube video using yt-dlp."""
        if url:
            yt_dlp_path = os.path.join(os.getcwd(), "dependencies", "yt-dlp.exe")
            if not os.path.exists(yt_dlp_path):
                return "yt-dlp.exe not found in dependencies folder!"
            
            # Video Download (best video + audio)
            if download_type == "single":
                if format_choice == "audio":
                    command = [yt_dlp_path, '-f', 'bestaudio', '--audio-quality', '0', '--audio-multistreams', '--extract-audio', '--audio-format', 'mp3', '-o', f"{download_folder}/%(title)s.%(ext)s", url]
                else:  # format_choice == "video"
                    command = [yt_dlp_path, '-f', 'bestvideo+bestaudio', '--merge-output-format', 'mp4', '-o', f"{download_folder}/%(title)s.%(ext)s", url]
            elif download_type == "playlist":
                if format_choice == "audio":
                    command = [yt_dlp_path, '-f', 'bestaudio', '--audio-quality', '0', '--audio-multistreams', '--extract-audio', '--audio-format', 'mp3', '--yes-playlist', '-o', f"{download_folder}/%(title)s.%(ext)s", url]
                else:  # format_choice == "video"
                    command = [yt_dlp_path, '-f', 'bestvideo+bestaudio', '--merge-output-format', 'mp4', '--yes-playlist', '-o', f"{download_folder}/%(title)s.%(ext)s", url]
            
            subprocess.run(command, shell=True)
            return "Download Completed!"
