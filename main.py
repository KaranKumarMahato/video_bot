import os
import asyncio
import requests
import youtube_dl
from tqdm import tqdm
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import aiohttp
import json

# API URLs
UPLOAD_URL = "https://api.socialverseapp.com/posts/generate-upload-url"
CREATE_POST_URL = "https://api.socialverseapp.com/posts"

# Set your Flic-Token (from Telegram message)
FLIC_TOKEN = "<YOUR_TOKEN>"

# Define the category id (adjust this based on your platform)
CATEGORY_ID = 1

# Directory to monitor
VIDEO_DIR = "./videos"

# Helper function to get upload URL
async def get_upload_url():
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(UPLOAD_URL, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result.get('url', None)
            else:
                print(f"Failed to get upload URL: {response.status}")
                return None

# Helper function to upload video
async def upload_video(file_path, upload_url):
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as f:
            async with session.put(upload_url, headers=headers, data=f) as response:
                if response.status == 200:
                    print(f"Uploaded {file_path} successfully")
                else:
                    print(f"Failed to upload {file_path}: {response.status}")

# Helper function to create post
async def create_post(file_name, video_hash):
    headers = {
        "Flic-Token": FLIC_TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "title": file_name,
        "hash": video_hash,
        "is_available_in_public_feed": False,
        "category_id": CATEGORY_ID
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(CREATE_POST_URL, headers=headers, json=data) as response:
            if response.status == 200:
                print(f"Post created for {file_name}")
            else:
                print(f"Failed to create post: {response.status}")

# Download video from URL (Instagram or TikTok)
async def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(VIDEO_DIR, '%(title)s.%(ext)s'),
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_name = ydl.prepare_filename(info_dict)
        return file_name

# Watchdog event handler to monitor the video directory
class VideoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".mp4"):
            asyncio.run(handle_new_video(event.src_path))

async def handle_new_video(file_path):
    # Step 1: Get upload URL
    upload_url = await get_upload_url()
    if not upload_url:
        print("No upload URL received. Exiting...")
        return

    # Step 2: Upload video
    await upload_video(file_path, upload_url)

    # Step 3: Create post
    video_hash = file_path.split("/")[-1]  # Simple way to get video hash (could be enhanced)
    await create_post(file_path, video_hash)

    # Step 4: Delete local file after upload
    os.remove(file_path)
    print(f"Deleted {file_path} after upload.")

# Main function to start the bot
async def main():
    # Create videos directory if it doesn't exist
    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR)

    # Start directory monitor
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, VIDEO_DIR, recursive=False)
    observer.start()

    try:
        while True:
            await asyncio.sleep(1)  # Keep the bot running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start the bot
if __name__ == "__main__":
    asyncio.run(main())
