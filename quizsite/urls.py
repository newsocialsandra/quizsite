from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.startpage),
	url(r"^quiz/[a-z-]+/$", views.quiz),
	url(r"^quiz/[a-z-]+/question/[0-9]/$", views.question),
	url(r"^quiz/[a-z-]+/completed/$", views.completed),
]
