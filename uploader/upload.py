from googleapiclient.discovery import build

def upload_video(video_path, title, description, playlist_id):
    youtube = build("youtube", "v3", credentials=YOUR_CREDS)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "playlistId": playlist_id,
                "categoryId": "24"
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(video_path)
    )
    request.execute()

if __name__ == "__main__":
    upload_video("output.mp4", "Beyoncé Scandal!", "Trending news", "PLAYLIST_ID_NEWS")