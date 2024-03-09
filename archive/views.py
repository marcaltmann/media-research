from django.shortcuts import get_object_or_404, render

from .models import Archive, Interview

def index(request):
    all_archives = Archive.objects.all
    context = {
        "archives": all_archives
    }
    return render(request, "archive/index.html", context)

def detail(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, "archive/detail.html", {"archive": archive})

def interview_index(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, "archive/interview_index.html",
                  {"archive": archive})

def interview_detail(request, archive_id, interview_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    interview = get_object_or_404(Interview, pk=interview_id)
    return render(request, "archive/interview_detail.html",
                  {"archive": archive, "interview": interview})
