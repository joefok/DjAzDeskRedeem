from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return redirect('https://www.bing.com')
    return render(request, "upload.html")

