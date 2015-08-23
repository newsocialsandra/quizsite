# coding: utf-8
from django.http import Http404
from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from quiz.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.
def startpage(request):
	context = {
			"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404

	context = {
			"quiz": quiz,
	}
	return render(request, "quiz/quiz.html", context)
def question(request, slug, number):
	number = int(number)
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404

	context = {
	"quiz": quiz,
	}

	questions = quiz.questions.all()
	question = questions[number - 1]
	if request.POST:
		answer = int(request.POST["answer"])

		saved_answers = {}
		if quiz.slug in request.session:
			saved_answers = request.session[quiz.slug]

		saved_answers[str(number)] = answer
		request.session[quiz.slug] = saved_answers
		if questions.count() == number:
			return redirect("completed_page", quiz.slug)
		else:
			return redirect("question_page", quiz.slug, number +1)

	if number > questions.count():
		raise Http404	
	
	context = {
		"question_number": number,
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"quiz": quiz,
		"imagelink": question.imagelink,
	}
	return render(request, "quiz/question.html", context)
def completed(request, slug):
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404

	context = {
	"quiz": quiz,
	}
	questions = quiz.questions.all()
	saved_answers = request.session[slug]
	num_correct_answers = 0
	
	for counter, question in enumerate(questions):
		if question.correct == saved_answers[str(counter + 1)]:
			num_correct_answers += 1

	context = {
		"correct": num_correct_answers,
		"total": questions.count(),
		"quiz": quiz,
		}
	return render(request, "quiz/resultat.html", context)

# def contact(request):
# 	form_class = ContactForm

# 	return render(request, "quiz/kontakt.html", {
# 		"form": form_class,
# 		})

def contact(request):
	form_class = ContactForm

	# new logic!
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" +'<http://djurspanaren.herokuapp.com/>',
				['svensean@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			return redirect('contact_page')

	return render(request, 'quiz/kontakt.html', {
		'form': form_class,
	})

def random(request):
	return render(request, "quiz/random.html")

def handler404(request):
	response = render_to_response('404.html', {},
			context_instance=RequestContext(request))
	response.status_code = 404
	return response