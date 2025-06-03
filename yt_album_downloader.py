
import yt_dlp
import os

def download_album(playlist_url, download_path="downloads"):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(download_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'noplaylist': False,
        'quiet': False,
        'nocheckcertificate': True,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    url = input("Nhập URL album (playlist) YouTube: ")
    folder = "downloads"
    download_album(url, folder)
    print("✅ Tải xong!")
