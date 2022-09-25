import random
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    content = 'Hello world! I am learning Django!'

    return HttpResponse(content)


def luck_number(request):
    number = random.randint(1, 10)
    content = f'Your lucky number is {number}'

    return HttpResponse(content)


def favorite_pet(request):
    pet = request.GET.get('mypet')

    if pet is None:
        content = 'You do not like any pets :('
    else:
        content = f'Your favorite pet is {pet} :)'

    return HttpResponse(content)


def pet_names(request, pet_type):
    if pet_type == 'dog':
        names = ['Lulu', 'Muki', 'Zeus', 'Thor', 'Odin']

    elif pet_type == 'cat':
        names = ['Mimi', 'Garfield', 'Felix', 'Miisu', 'Meow']

    else:
        content = f'Sorry. We do not have any suggestion for {pet_type} at the moment'
        return HttpResponse(content)

    content = 'Here are some suggestions for you: ' + ', '.join(names)

    return HttpResponse(content)



