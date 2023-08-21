from drf_yasg import openapi

def translator_query_paramaters():
    _from = openapi.Parameter("from", openapi.IN_QUERY, description="From language (code)", type=openapi.TYPE_STRING, required=True)
    to = openapi.Parameter("to", openapi.IN_QUERY, description="To language (code)", type=openapi.TYPE_STRING, required=True)
    sentence = openapi.Parameter("sentence", openapi.IN_QUERY, description="Sentence to translate", type=openapi.TYPE_STRING, required=True)
    api_key = openapi.Parameter("x-api-key", openapi.IN_QUERY, description="API Key", type=openapi.TYPE_STRING, required=False)
    return [_from, to, sentence, api_key]
