from rest_framework import serializers

class TranslatorSerializer(serializers.Serializer):
    from_ = serializers.CharField(read_only=True)
    to = serializers.CharField(read_only=True)
    sentence = serializers.CharField(read_only=True)
    translation = serializers.CharField(read_only=True)
