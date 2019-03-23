from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from django.contrib.auth.decorators import login_required
from .models import Service

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

def index(request):
	return render(request, 'blog/index.html')

def home(request):
	services = Service.objects.all()
	paginator = Paginator(services, 9) # Muestra 9 servicio por página
	page = request.GET.get('page')
	services = paginator.get_page(page)
	return render(request, 'blog/home.html', {'services': services})

def ourteam(request):
	return render(request, 'blog/ourteam.html')

def faqs(request):
	return render(request, 'blog/faqs.html')

def search(request):
	requestVideos = request.GET.get('video_name', '')
	
	if requestVideos == '' :
		messages.warning(request, 'No se pudo efectuar la búsqueda... el campo de la misma no debe estar vacío')
		return redirect('blog-home')
	else:
		listOfVideos = youtube_search(requestVideos, 27) # La cantidad máxima de respuestas es 27
		paginator = Paginator(listOfVideos, 9) # Muestra 9 videos por página
		page = request.GET.get('page')
		listOfVideos = paginator.get_page(page)
		
	return render(request, 'blog/search.html', {'videos': listOfVideos, 'video_name':requestVideos} )
