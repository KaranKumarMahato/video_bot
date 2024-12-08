The Video Upload Automation Bot is a Python script that automates the process of downloading videos from social media platforms like Instagram and TikTok, uploading them to a platform via an API, and creating posts with the relevant metadata. The bot monitors a specified directory for new video files, downloads them, uploads them to the platform, and deletes the local files after a successful upload. This automation helps streamline the process of managing video content.

Features
Download Videos: The bot can download videos from Instagram and TikTok using URLs.
Upload Videos: Once downloaded, the bot uploads videos to a platform using a provided API.
Create Post: After uploading, the bot creates a post with metadata (such as the video title and hash) using the platform's API.
Monitor Directory: The bot continuously monitors a designated directory for new video files (specifically .mp4 files) and processes them automatically.
Delete After Upload: The local video files are deleted after being successfully uploaded, ensuring there is no unnecessary storage usage.
Requirements
The bot requires Python 3.7+ and the following libraries: requests for HTTP requests, youtube_dl for downloading videos from social media platforms, tqdm for progress bars, watchdog for directory monitoring, aiohttp for asynchronous HTTP requests, and json for handling JSON data. These dependencies can be installed by running the command pip install requests youtube_dl tqdm watchdog aiohttp.

Configuration
Before running the bot, configure the script by setting the following variables:

FLIC_TOKEN: This is your unique Flic token, which is required for API authentication and can be obtained via a message on Telegram.
CATEGORY_ID: This refers to the category ID for the posts and should be set according to the platform's categories.
VIDEO_DIR: This is the directory where videos will be temporarily stored. Ensure the directory exists, or it will be created automatically.
Functions
get_upload_url(): Retrieves a unique upload URL for video files from the platform's API.
upload_video(file_path, upload_url): Uploads a video to the platform using the upload URL obtained from the API.
create_post(file_name, video_hash): Creates a post with the video's metadata, including the title and hash, via the platform's API.
download_video(url): Downloads videos from the specified URL (Instagram or TikTok) using youtube_dl.
A custom event handler class, VideoHandler, uses the watchdog library to monitor the video directory for new .mp4 files. It triggers the handle_new_video function when a new video is detected, which:

Retrieves the upload URL.
Uploads the video.
Creates a post with metadata.
Deletes the local file after successful upload.
Usage
To use the bot, clone or download the repository to your local machine. Ensure that all dependencies are installed by running pip install -r requirements.txt. Configure the script with your FLIC_TOKEN, CATEGORY_ID, and VIDEO_DIR. Then, run the bot using the command python bot.py. The bot will begin monitoring the VIDEO_DIR directory. Whenever new .mp4 files are added, it will:

Download the video (if a URL is provided).
Upload it to the specified platform.
Create a post for the video.
Delete the local video file after successful upload.
License
This project is licensed under the MIT License. For more details, refer to the LICENSE file.

Troubleshooting
Permission Issues: Ensure the script has read and write permissions for the video directory.
API Errors: Check the API response status codes. A non-200 response indicates an error, such as an incorrect token or a failed upload.
Directory Monitoring Not Triggering: Ensure that the VIDEO_DIR directory exists and contains .mp4 files for the bot to monitor and process.
This bot offers an efficient and automated way to manage video content, download from social media platforms, and upload them to your specified platform without manual intervention.