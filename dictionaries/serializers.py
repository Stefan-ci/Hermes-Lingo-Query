from rest_framework import serializers

class DictionarySerilizer(serializers.Serializer):
    language = serializers.CharField(read_only=True)
    word = serializers.CharField(read_only=True)
    phonetics = serializers.CharField(read_only=True)
    meaning = serializers.CharField(read_only=True)
    synonyms = serializers.ListField()
    antonyms = serializers.ListField()
    hyponyms = serializers.ListField()
    hypernyms = serializers.ListField()
