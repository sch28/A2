# url file for music
from django.conf.urls import url
from . import views

urlpatterns = [
	# /mainPage/
    url(r'^$', views.index, name = 'index'), #navigating to main page
	url(r'tasks/$', views.tasks, name ='tasks' ),
	
	# /music/<music_id>/favorite/
	url(r'complete/$', views.complete, name ='complete' ),
	# /music/<music_id>/favorite/
	url(r'done/$', views.done, name ='done' ),
	
	
]