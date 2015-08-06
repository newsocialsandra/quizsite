from django.shortcuts import render

# Create your views here.
def startpage(request):
	return render(request, "quiz/startpage.html")
def quiz(request):
	return render(request, "quiz/monstermastaren.html")
def question(request):
	return render(request, "quiz/monstermastaren1.html")
def completed(request):
	return render(request, "quiz/resultat_monstermastaren.html")
def random(request):
return render(request, "quiz/random.html")
