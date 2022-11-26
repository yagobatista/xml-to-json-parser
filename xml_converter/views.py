from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from xml_converter.converter.converter import xml_to_dict


class ConnectedView(APIView):
    """
    A view that the connected html page which uploads a xml file and parses the same file to json
    """
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="upload_page.html")

    def post(self, request):
        file = request.FILES.get("file")

        if file is None:
            raise ValidationError({"file": "required"})

        file_data = file.read().decode()

        return Response(xml_to_dict(file_data), content_type="application/json")
