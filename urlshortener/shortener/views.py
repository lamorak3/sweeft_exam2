from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Short_Data

from .forms import Url
# Create your views here.

def home_view(request):
    context={
        'form':Url()
    }
    if request.method == 'POST':
        #post brdzanebis shemtxvevashi daamatebs axal obieqts
        form = Url(request.POST)
        if form.is_valid():
            val = form.save()
            new_url = request.build_absolute_uri('/')+val
            url = val.url
            context['url'] = url
            context['new_url'] = new_url
            return render(request, 'shortener/home.html', context)
        return render(request, 'shortener/home.html', context)
        #tu sheyvanili monacemebi validuri ar aris tavidan sheyvana ar mouwios
    elif request.method == 'GET':
        return render(request, 'shortener/home.html', context)

def click_url_view(request,string):
    try:
        shortener = Short_Data.objects.get(short_url=string)
        shortener.accessed_times += 1     
        shortener.save()
        
        return HttpResponseRedirect(shortener.url)
        #gadaamisamartebs shesabamis bmulze da gazrdis accessed_times cvlads
    except:
        raise Http404('Wrong Link')
        #gamoitans 404 shecdomas tu linki arasworia