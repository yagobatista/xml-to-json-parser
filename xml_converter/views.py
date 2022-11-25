from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.converter.converter import xml_to_dict


def upload_page(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        file_data = file.read().decode()

        return JsonResponse(xml_to_dict(file_data))

    return render(request, "upload_page.html")
