from django.shortcuts import render
from events.models import Event

def homePage(request):
    page = "home"
    context = {'page':page}
    return render(request, 'home.html', context)


def eventsPage(request):
    page = 'events'
    events = Event.objects.all()
    context = {
        'page':page,
        'events':events,
    }
    return render(request, 'pages/events.html', context)

def newsPage(request):
    page = 'news'
    news = []
    context = {
        'page': page,
        'news': news
    }
    return render(request, 'pages/news.html', context)

def test(request):
    return render(request, 'pages/test.html', {})