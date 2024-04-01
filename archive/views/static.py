from django.shortcuts import render

def accessibility(request):
    return render(request, "archive/pages/accessibility.html")
