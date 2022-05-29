from multiprocessing import context

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from music.models import Album


def index(request):
    num_alb = Album.objects.all().count()
    alba = Album.objects.order_by('a_name')[:3]

    context = {
        'num_alb': num_alb,
        'alba': alba,

    }
    return render(request, 'index.html', context=context)


class AlbumListView(ListView):
    model = Album

    context_object_name = 'alba'
    template_name = 'list.html'

class AlbumDetailView(DetailView):
    model = Album

    context_object_name = 'alba_detail'
    template_name = 'detail.html'