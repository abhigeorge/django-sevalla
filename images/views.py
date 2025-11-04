from django.shortcuts import render, redirect
from .forms import UploadedImageForm
from .models import UploadedImage


def upload_image_view(request):
    if request.method == "POST":
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_success")
    else:
        form = UploadedImageForm()
    return render(request, "upload.html", {"form": form})


def home_view(request):
    images = UploadedImage.objects.order_by("-uploaded_at")
    return render(request, "home.html", {"images": images})
