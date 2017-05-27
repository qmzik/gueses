from django.shortcuts import render


def main(request):
    return render(request, 'landing/main.html', locals())


def first(request):
    return render(request, 'landing/first.html', locals())


def second(request):
    return render(request, 'landing/second.html', locals())


def third(request):
    return render(request, 'landing/third.html', locals())


def fourth(request):
    return render(request, 'landing/fourth.html', locals())
