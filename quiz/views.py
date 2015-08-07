# coding: utf-8

from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.
def startpage(request):
	context = {
	    	"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	context = {
		"quiz": Quiz.objects.get(slug=slug),
	}
	return render(request, "quiz/monstermastaren.html", context)
def question(request, slug, number):
	context = {
		"question_number": number,
		"question": u"Vem går klädd i svartvita ränder?",
		"answer1": u"Fröken Zebra",
	   	"answer2": u"Fru Leopard",
	    "answer3": u"Lilla Björn",
	    "quiz_slug": slug,
	}
	return render(request, "quiz/monstermastaren1.html", context)
def completed(request, slug):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_slug": slug,
		}
	return render(request, "quiz/resultat.html", context)