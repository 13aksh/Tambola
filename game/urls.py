from django.conf.urls import url
from . import views

urlpatterns = [
	# Game homepage
	url(r'^$', views.index, name='index'),

	# Tickets genration page
	url(r'^(?P<noticks>[0-9]+)/$', views.tickets, name='tickets'),
]