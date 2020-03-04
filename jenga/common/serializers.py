from rest_framework import serializers


class CommonSerializer(serializers.ModelSerializer):

    class Meta:
        read_only_fields = ('created', 'updated')
