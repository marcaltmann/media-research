from django.shortcuts import render


def welcome(request):
    return render(request, "pages/welcome.html")


def terms(request):
    return render(request, "pages/terms.html")


def privacy(request):
    return render(request, "pages/privacy.html")


def accessibility(request):
    return render(request, "pages/accessibility.html")
