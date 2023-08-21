from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import Response, APIView

from PyDictionary import PyDictionary
from eng_to_ipa import convert as convert_to_phonetics
from wordhoard import Antonyms, Hypernyms, Synonyms, Hyponyms

from dictionaries.serializers import DictionarySerilizer
from hermes_lingo_query.mixins import ApiKeyRequiredMixin
from dictionaries.utils import dictionary_query_paramaters



class DictionaryApiView(ApiKeyRequiredMixin, APIView):
    """ 
        Find phonetics, meaning, antonyms, synonyms, hyponyms, hypernyms of a given word in english.
            Query Params:
                - word (__str__): *The word to look for.*
    """
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(responses={200: DictionarySerilizer}, manual_parameters=dictionary_query_paramaters())
    def get(self, request, format=None):
        word = str(request.GET.get("word")) or ""
        
        phonetic = convert_to_phonetics(word)
        meaning = PyDictionary().meaning(word)
        synonyms = Synonyms(search_string=word, max_number_of_requests=10, rate_limit_timeout_period=30).find_synonyms()
        antonyms = Antonyms(search_string=word, max_number_of_requests=10, rate_limit_timeout_period=30).find_antonyms()
        hypernyms = Hypernyms(search_string=word, max_number_of_requests=10, rate_limit_timeout_period=30).find_hypernyms()
        hyponyms = Hyponyms(search_string=word, max_number_of_requests=10, rate_limit_timeout_period=30).find_hyponyms()
        
        data = {
            "language": "en",
            "word": word,
            "phonetics": phonetic,
            "meaning": meaning,
            "synonyms": synonyms,
            "antonyms": antonyms,
            "hyponyms": hyponyms,
            "hypernyms": hypernyms,
        }
        return Response(DictionarySerilizer(data, many=False).data, status=status.HTTP_200_OK)
