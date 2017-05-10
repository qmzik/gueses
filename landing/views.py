from django.shortcuts import render


def first(request):
    return render(request, 'landing/first.html', locals())


def main(request):
    return render(request, 'landing/main.html', locals())


def second(request):
    return render(request, 'landing/second.html', locals())


def third(request):
    return render(request, 'landing/third.html', locals())
