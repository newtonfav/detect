from .serializers import FileUploadSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# @api_view(['POST'])
# def uploadPics(self, request, *args, **kwargs):
#     serializer = FileUploadSerializer(data=request.data)

#     if serializer.is_valid():
#         # Save the uploaded file to a specified directory
#         uploaded_file = serializer.validated_data['file']
#         with open('uploads/' + uploaded_file.name, 'wb+') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)

#         return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # Save the uploaded file to a specified directory
            uploaded_file = serializer.validated_data['file']
            with open('uploads/' + uploaded_file.name, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
