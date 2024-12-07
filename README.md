video_bot
Video Upload Automation Bot Overview This Python script automates the process of downloading videos from social media platforms (Instagram, TikTok), uploading them to a platform using an API, and creating posts with relevant metadata. It monitors a specified directory for new videos, downloads them, uploads them to the platform, and deletes the local files after a successful upload.

Features Download Videos: Downloads videos from URLs (Instagram, TikTok). Upload Videos: Uploads downloaded videos to a platform via an API. Create Post: Creates a post with video metadata using the platform's API. Monitor Directory: Monitors a directory for new video files and processes them automatically. Delete After Upload: Deletes local video files after they have been uploaded successfully. Requirements Python 3.7+ Install the following Python libraries: requests: For HTTP requests to interact with the API. youtube_dl: For downloading videos from social media platforms. tqdm: For progress bars in long-running processes. watchdog: For directory monitoring. aiohttp: For asynchronous HTTP requests. json: For working with JSON data. Install the required dependencies using:

bash Copy code pip install requests youtube_dl tqdm watchdog aiohttp Configuration Before running the script, ensure the following variables are set:

FLIC_TOKEN: Your Flic token, which is required to authenticate with the API. (Received from Telegram message) CATEGORY_ID: The category ID for the posts. Adjust based on your platform's categories. VIDEO_DIR: The directory where videos will be stored temporarily. Make sure the directory exists or it will be created. python Copy code FLIC_TOKEN = "your_flic_token_here" CATEGORY_ID = 2 VIDEO_DIR = "./videos" Functions

get_upload_url() This function retrieves a unique upload URL for video files from the API.

upload_video(file_path, upload_url) This function uploads a video to the platform using the upload URL received from the API.

create_post(file_name, video_hash) This function creates a post with the uploaded video's metadata, including the title and hash, via the platform's API.

download_video(url) Downloads a video from a URL (Instagram or TikTok) using youtube_dl.

VideoHandler A custom event handler class that uses watchdog to monitor the video directory for new .mp4 files and triggers the handle_new_video function when a new video is added.

handle_new_video(file_path) This function handles the steps to:

Retrieve the upload URL. Upload the video. Create a post with metadata. Delete the local video file after successful upload. 7. main() The main function sets up the monitoring of the video directory and runs the bot indefinitely, processing new videos as they are added.

Usage Clone or download this repository to your local machine. Ensure all dependencies are installed by running: bash Copy code pip install -r requirements.txt Configure the script with your FLIC_TOKEN, CATEGORY_ID, and VIDEO_DIR. Run the bot using: bash Copy code python bot.py The bot will begin monitoring the VIDEO_DIR directory. When new .mp4 files are added, it will: Download the video (if the URL is provided). Upload it to the specified platform. Create a post for the video. Delete the local file after successful upload. License This project is licensed under the MIT License - see the LICENSE file for details.

Troubleshooting Permission Issues: Ensure the script has read and write permissions for the video directory. API Errors: Check the API response status codes. A non-200 response indicates an error (e.g., incorrect token or failed upload). Directory Monitoring Not Triggering: Ensure that the VIDEO_DIR directory exists and contains .mp4 files.
