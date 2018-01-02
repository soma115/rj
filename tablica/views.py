from django.shortcuts import render


def tablica(request):
    return render(request, 'tablica/rozklad.html', {})
