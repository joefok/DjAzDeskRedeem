from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import csv
token = {}
with open('upload/mac_map.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        token[row[0]] = row[-1]
print(token)
base_url = 'https://guatraroom.eastasia.cloudapp.azure.com/guacamole/?username=secret&password=secret'


def image_upload(request):
    token_get = request.GET.get('token')
    return redirect(base_url.replace('secret', '{}'.format(token[token_get])))
    # return render(request, "upload.html")

