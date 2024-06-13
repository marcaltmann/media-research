from django.shortcuts import render


def terms(request):
    return render(request, "archive/pages/terms.html")


def privacy(request):
    return render(request, "archive/pages/privacy.html")


def accessibility(request):
    return render(request, "archive/pages/accessibility.html")
