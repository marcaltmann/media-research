from django.shortcuts import render, get_object_or_404

from .models import ImageMaterial


def image_material_detail(request, image_material_id):
    image_material = get_object_or_404(ImageMaterial, pk=image_material_id)
    resource = image_material.resource
    context = {
        "image_material": image_material,
        "resource": resource,
    }
    return render(request, "materials/image_material_detail.html", context)
