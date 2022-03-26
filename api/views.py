from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

from api.models import Spreadsheet
from api.serializers import SpreadsheetSerializer
from rest_framework.response import Response


class SpreadSheetViewSet(viewsets.ModelViewSet):
    queryset = Spreadsheet.objects.all()
    serializer_class = SpreadsheetSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['POST'])
    def test_response(self, request, pk=None):
        response = {'message': 'probably the logic to merge spreadsheet is here.'}
        spreadsheet = Spreadsheet.objects.get(id=pk)
        print(spreadsheet.file)
        return Response(response, status=status.HTTP_200_OK)
