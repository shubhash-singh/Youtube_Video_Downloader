from pytube import YouTube

def download_video(url, save_path='.'):
    try:
        # Create YouTube object
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Number of views: {yt.views}")

        # Get the highest resolution stream
        ys = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading...")
        ys.download(save_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example URL of the YouTube video
    video_url = "https://youtu.be/91BUM3WhCfo?si=6-0XGXF7fJaVu5Vn"
    # Path where the video will be saved
    save_path = "/media/ragnar/Codes/Projects"

    # Download the video
    download_video(video_url, save_path)
