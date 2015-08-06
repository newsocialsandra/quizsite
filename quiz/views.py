# coding: utf-8

from django.shortcuts import render

quizzes = {
	"klassiker": {
   		"name": u"Klassiska böcker",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Största fotbollslagen",
	   	"description": u"Kan du dina lag?"
	},
	"kanda-hackare": {
	    	"name": u"Världens mest kända hackare",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}

# Create your views here.
def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request):
	return render(request, "quiz/monstermastaren.html")
def question(request):
	return render(request, "quiz/monstermastaren1.html")
def completed(request):
	return render(request, "quiz/resultat.html")