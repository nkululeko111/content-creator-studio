from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(video_path, title, description):
    youtube = build("youtube", "v3", credentials=YOUR_CREDS)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["news", "gossip"],
                "categoryId": "24"  # Entertainment
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(video_path)
    )
    response = request.execute()
    return response

if __name__ == "__main__":
    upload_video("output.mp4", "Kenny Kunene EXPOSED", "The truth behind the rumors...")










#     from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# import os
# import json

# # Load credentials from a file or environment
# # You need OAuth 2.0 credentials setup
# def get_authenticated_service():
#     credentials = None
#     # Load credentials.json (OAuth client secrets)
#     # For simplicity, assume you've already done OAuth setup
#     # and have token.json
#     import google_auth_oauthlib.flow
#     from google.oauth2.credentials import Credentials

#     SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
#     creds = None
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     else:
#         flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#             "credentials.json", SCOPES)
#         creds = flow.run_local_server(port=0)
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())

#     youtube = build("youtube", "v3", credentials=creds)
#     return youtube

# def upload_video(video_path, title, description, tags, playlist_id=None):
#     youtube = get_authenticated_service()

#     body=dict(
#         snippet=dict(
#             title=title,
#             description=description,
#             tags=tags,
#             playlistId=playlist_id
#         ),
#         status=dict(
#             privacyStatus="public"
#         )
#     )

#     media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
#     request = youtube.videos().insert(
#         part="snippet,status",
#         body=body,
#         media_body=media
#     )
#     response = request.execute()
#     print(f"Uploaded video ID: {response['id']}")
#     return response['id']

# if __name__ == "__main__":
#     video_path = "videos/output_video.mp4"
#     title = "Kenny Kunene Politician Controversy"
#     description = "Latest news and controversies about Kenny Kunene."
#     tags = ["Kenny Kunene", "Politics", "News"]
#     upload_video(video_path, title, description, tags)