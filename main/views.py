from django.shortcuts import render
import random


def Home(request):

    return render(request, 'main/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[]^_`{|}~'))
    length = int(request.GET.get('length', 8))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'main/password.html', {'password': thepassword})
