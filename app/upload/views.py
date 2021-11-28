from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import csv
token = {}
with open('upload/mac_map.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        token[row[0]] = row[-1]

base_url = 'https://guatraroom.eastasia.cloudapp.azure.com/guacamole/?username=secret&password=secret'


def image_upload(request):
    if request.method == 'GET':
        print(request.GET)
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return redirect(base_url)
    # return render(request, "upload.html")

