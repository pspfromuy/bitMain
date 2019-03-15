from django.shortcuts import render
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyD_J7a1LfWjW-JTMZB7lSfnnU1fYezaG5A"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

	# Call the search.list method to retrieve results matching the specified
	# query term.
	search_response = youtube.search().list(
	q=q,
	part="id,snippet",
	maxResults=max_results
	).execute()

	videos = []

	# Add each result to the appropriate list, and then display the lists of
	# matching videos, channels, and playlists.
	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			#videos.append("%s (%s)" % (search_result["snippet"]["title"],
			#							search_result["id"]["videoId"]))
			videos.append(search_result)
	return videos


# Create your views here.

def home(request):
	return render(request, 'blog/home.html')

def ourteam(request):
	return render(request, 'blog/ourteam.html')

def faqs(request):
	return render(request, 'blog/faqs.html')

def search(request):
	requestVideos = request.GET.get('video_name', '')
	if requestVideos == '' :
		listOfVideos = []
	else:
		listOfVideos = youtube_search(requestVideos, 10)
	return render(request, 'blog/search.html', {'videos': listOfVideos})

