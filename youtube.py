import pytube
import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

# settings
video_status = 'public'
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# legal stuff
email = 'the-yt-archive@pm.me'

video_url_input = input("Enter video URL: ")
video_url = video_url_input
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('./videos')

title = video.title
description = youtube.description
length = youtube.length
author = youtube.author
views = youtube.views
rating = youtube.rating
original_video = video_url_input

description_redone = ('This video has been automatically re-uploaded under the YouTube Archive channel.\n\nOriginal:\nVideo: ' + video_url_input + '\nAuthor: ' + author + '\n\nOriginal Description:\n' + description + '\n\nLegal:\nIf you want us to remove your video, please contact us here: ' + email)

# actually upload the video now
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    'snippet': {
        'title': title,
        'description': description_redone,
        'tags': None
    },
    'status': {
        'privacyStatus': video_status,
    },
    'notifySubscribers': True
}

mediaFile = MediaFileUpload('./videos/' + title + '.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

