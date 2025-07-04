from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

# Create your views here.
def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        else:
             error = 'Данные были заполнены некорректно'
    form = FilmForm()
    return render(request, 'add_film.html', {'form': form, 'error':error})

def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films})