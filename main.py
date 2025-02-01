import subprocess
import sys
import importlib.util
import os

# Function to check if a package is installed
def check_and_install_package(package_name):
    try:
        # Check if package is already installed
        package_spec = importlib.util.find_spec(package_name)
        if package_spec is None:
            print(f"{package_name} not found. Installing...")
            # Install the package using pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"{package_name} installed successfully.")
        else:
            print(f"{package_name} is already installed.")
    except subprocess.CalledProcessError:
        print(f"Error installing {package_name}. Please ensure you have internet access.")
        sys.exit(1)

# Function to check and install necessary packages
def install_required_packages():
    packages = ["PyQt6", "requests"]
    
    for package in packages:
        check_and_install_package(package)

# Run the package check before starting the app
install_required_packages()

# Now, you can import PyQt6 and requests without issues
from PyQt6.QtWidgets import QApplication
from ui import YouTubeDownloaderUI  # Ensure you import your UI class correctly

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloaderUI()  # Instantiate the UI class
    window.show()
    sys.exit(app.exec())
