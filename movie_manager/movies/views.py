from django.shortcuts import render
from . models import MovieInfo

# Create your views here.

from . forms import MovieForm
def create(request):  
    frm= MovieForm()
    if request.POST:
        frm= MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
        else:
            frm= MovieForm()

    return render(request, 'create.html', {'frm': frm})

def List(request):
    movie_set= movie_data= MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'list.html', {'movies':movie_set})

def edit(request):
    return render(request, 'edit.html')