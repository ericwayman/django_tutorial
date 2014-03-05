from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll
from django.http import Http404

# Create your views here.
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	a = [1,2,3]
	context = {'latest_poll_list': latest_poll_list,
				'a':a}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	try:
	    poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
	    raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)