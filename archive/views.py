from django.shortcuts import get_object_or_404, render

from .models import Archive

def index(request):
    all_archives = Archive.objects.all
    context = {
        "archives": all_archives
    }
    return render(request, "archive/index.html", context)

def detail(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, "archive/detail.html", {"archive": archive})
