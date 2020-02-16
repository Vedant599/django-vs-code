from django.shortcuts import render
from polls.models import MyChoice,MyQuestion


# Create your views here.
def index(request):
    latest_question_list=MyQuestion.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question=MyQuestion.objects.get(pk=question_id)
    except:
        raise http404('question Doesn\'t exist')
    return render(request,'polls/result.html',{'question':question})
