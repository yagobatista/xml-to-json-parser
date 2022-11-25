from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.converter.converter import xml_to_dict


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    # parser_classes = [JSONParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        file = request.data.get("file")
        file_data = file.read().decode()

        return Response(xml_to_dict(file_data), content_type="application/json")
