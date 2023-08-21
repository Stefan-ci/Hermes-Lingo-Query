from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import Response, APIView

from translate import Translator

from translations.serializers import TranslatorSerializer
from hermes_lingo_query.mixins import ApiKeyRequiredMixin
from translations.utils import translator_query_paramaters



class TranslatorApiView(ApiKeyRequiredMixin, APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(responses={200: TranslatorSerializer}, manual_parameters=translator_query_paramaters())
    def get(self, request, format=None):
        from_ = str(request.GET.get("from")) or ""
        to = str(request.GET.get("to")) or ""
        sentence = str(request.GET.get("sentence")) or ""
        
        data = {
            "from_": from_,
            "to": to,
            "sentence": sentence,
            "translation": Translator(from_lang=from_,to_lang=to).translate(sentence),
        }
        return Response(TranslatorSerializer(data, many=False).data, status=status.HTTP_200_OK)
