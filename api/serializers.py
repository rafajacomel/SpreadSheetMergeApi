from rest_framework import serializers

from api.models import Spreadsheet


class SpreadsheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spreadsheet
        fields = ('file', 'path')