from django.shortcuts import render_to_response
from django.shortcuts import render 
from django.http import HttpResponse

from mongoengine import *  #Import things like connect

from granule.models import Employee
from granule.models import Poll, Choice
import mongoengine

# ...

user = authenticate(username=username, password=password)
assert isinstance(user, mongoengine.django.auth.User)

poll = Poll.objects(question__contains="What").first()
choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
poll.choices.append(choice)
poll.save()

print poll.question


def home(request):
	return HttpResponse("Granule!")

def index(request):
    return render_to_response("granule/index.html",{"hello":"Hey how was everything"})


# Create your views here.

def emp(request):
    employee = Employee.objects.create(
        email="pedro.kong@company.com",
        first_name="Pedro",
        last_name="Kong"
    )
    employee.save()
    return render_to_response('granule/emp.html', {})


def poll(request):
	choice =Choice()
    one = Poll.objects.create(choices =choice)
    one.save()
    return render_to_response('granule/poll.html', {})










