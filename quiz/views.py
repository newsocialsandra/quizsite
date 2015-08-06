# coding: utf-8

from django.shortcuts import render

quizzes = {
	"monstermastaren": {
   		"name": u"Mönstermästaren",
	   	"description": u"Känn igen djuret på dess mönster."
	},
	"nosa": {
	   	"name": u"Nosa rätt på djuret",
	   	"description": u"Vem gömmer sig bakom nosen, näsan eller näbben?"
	},
	"tassar": {
	    "name": u"Alla tassarna på jorden",
	    "description": u"Kan du se vem fötterna tillhör?"	},
	"raven": {
	    "name": u"Vad säger räven?",
	    "description": u"Lyssna på djurens läten och gissa vem som är vem."	},
	"kvittkvitt": {
	    "name": u"Kvitt-kvitt-kvivitt-kvitt",
	    "description": u"Kan du känna igen fågelsången?"	},
}

# Create your views here.
def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
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