# **YouDon - YouTube Downloader**  

**YouDon** is a YouTube video and audio downloader with a graphical user interface built using PyQt6. It allows users to download videos in the highest quality available and also supports playlist downloads. The application manages its dependencies automatically and ensures smooth operation by checking for required components.  

---

## **Installation Requirements**  

### **1. Install FFmpeg (Full Version) Globally**  

Before using YouDon, **FFmpeg must be installed globally** to enable proper merging of audio and video.  

#### **Steps to Install FFmpeg on Windows**  

1. **Download FFmpeg (Full Version)** from [FFmpeg from Gyan.dev](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z).  
2. Extract the contents to `C:\ffmpeg` or another preferred location.  (Please note, file locations of disk can be varied as per your preference, here an example is shown)
3. Add `C:\ffmpeg\bin` to the **System Environment Variables**:  
   - Open **System Properties** → **Advanced** → **Environment Variables**.  
   - Under "System Variables," find `Path`, click **Edit**, and add:  
     ```
     C:\ffmpeg\bin
     ```
   - Click **OK** and restart the computer.  
4. To verify FFmpeg installation, open **Command Prompt** and run:  
   ```sh
   ffmpeg -version
   ```
   If FFmpeg is correctly installed, the version details will be displayed.  

---

## **Downloading YouDon**  

- Download the latest **YouDon.exe** from the [Releases Page](https://github.com/MishrajiAryan/YouDon/releases/).  
- Move `YouDon.exe` to a dedicated folder before running it.  

---

## **How to Use YouDon**  

### **First-Time Setup**  

1. **After downloading `YouDon.exe`, do not run it immediately.**  
   - Create a new folder, for example, `C:\YouDon\`.  
   - Move `YouDon.exe` into this folder.  
   - This will store configuration files and dependencies.  

2. **Run `YouDon.exe`**  
   - The application will automatically **install `yt-dlp`** if it is missing.  
   - It will also check if FFmpeg is correctly installed.  
   - A configuration file and dependencies folder will be created inside the same directory.  

3. **Set a Default Download Folder**  
   - Before downloading anything, go to **"Choose Download Folder"** and select the preferred location.  
   - The application will remember this folder for future downloads.  

---

## **Features**  

- Download videos and audio in the **best available quality**.  
- Support for **single video** and **playlist downloads**.  
- Automatically **installs `yt-dlp`** if missing.  
- Uses **FFmpeg for proper audio and video merging**.  
- Saves and remembers the **default download folder**.  
- Shows **download progress in a Command Prompt window**.  
- Standalone `.exe` file that does not require Python installation.  

---

## **Important Notes**  

1. **Do not delete the `config.json` and `dependencies` folder**  
   - These files are created automatically in the same folder as `YouDon.exe`.  
   - They store user preferences and necessary dependencies.  

2. **Keep `YouDon.exe` in a dedicated folder**  
   - The application generates files on first use, so it is best to keep it in a separate folder.  

3. **Change the download folder before the first download**  
   - The first time YouDon is used, set a preferred **download folder** to avoid storing files in the default location.  

---

## **Troubleshooting**  

- **FFmpeg not detected**  
  - Ensure FFmpeg is installed globally as described in the installation section.  

- **Videos downloading without sound**  
  - This happens when FFmpeg is missing. Install FFmpeg and restart the application.  

- **Command Prompt window disappears too quickly**  
  - Run `YouDon.exe` from the Command Prompt manually:  
    ```sh
    cd "C:\YouDon"
    YouDon.exe
    ```

---

## **Developer**  

**Aryan Mishra**  

If you find any issues or want to request a feature, open an issue in this repo.  

---
