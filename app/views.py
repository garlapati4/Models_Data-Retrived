from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name='Circket')
    LTO=Topic.objects.exclude(topic_name='Circket')
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Circket')
    LWO=Webpage.objects.exclude(topic_name='Rugby')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    LARO=AccessRecord.objects.all()
    LARO=AccessRecord.objects.filter(name='nikki')
    LARO=AccessRecord.objects.exclude(name='nikki')
    LARO=AccessRecord.objects.all().order_by('name')
    d={'LARO':LARO}
    return render(request,'display_accessrecords.html',d)