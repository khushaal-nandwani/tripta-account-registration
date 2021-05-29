from rest_framework import serializers
from tform.models import TForm, Email


class TFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TForm
        fields = ('email', 'client_code', 'company_name', 'mobile_no',
                  'address', 'city', 'state')


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
