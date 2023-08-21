from drf_yasg import openapi

def dictionary_query_paramaters():
    word = openapi.Parameter("word", openapi.IN_QUERY, description="Word to look for", type=openapi.TYPE_STRING, required=True)
    api_key = openapi.Parameter("x-api-key", openapi.IN_QUERY, description="API Key", type=openapi.TYPE_STRING, required=False)
    return [word, api_key]
