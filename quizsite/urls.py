from django.conf.urls import url
from quiz import views
urlpatterns = [
	url("^$", views.startpage, name="start_page"),
	url(r"^quiz/([a-z-]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([a-z-]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([a-z-]+)/completed/$", views.completed, name="completed_page"),
]
