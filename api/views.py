from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

from api.models import Spreadsheet
from api.serializers import SpreadsheetSerializer
from rest_framework.response import Response
import os
import pandas as pd

@api_view()
@permission_classes([AllowAny])
def merge_two_spreadsheets(request):
    response = {'message': 'the merge of the two spreadsheets finished successfully'}
    merge_dir = request.query_params['merge_dir']
    print(merge_dir)
    output_file = request.query_params['output_file']
    print(output_file)
    merge_dir_system = os.path.abspath(merge_dir)
    files = os.listdir(merge_dir_system)

    df_total = pd.DataFrame()
    for file in files:
        print('merging file ' + file)
        excel_file = pd.ExcelFile(merge_dir + file)
        sheets = excel_file.sheet_names
        for sheet in sheets:  # loop through sheets inside an Excel file
            df = excel_file.parse(sheet_name=sheet)
            df_total = df_total.append(df)
    df_total.to_excel(output_file)

    return Response(response, status=status.HTTP_200_OK)

class SpreadSheetViewSet(viewsets.ModelViewSet):
    queryset = Spreadsheet.objects.all()
    serializer_class = SpreadsheetSerializer
    authentication_classes = (TokenAuthentication,)