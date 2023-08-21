# Hermes Lingo Query

__Hermes Lingo Query__ is a minimalist DRF App to translate texts and search english words in a dictionary.

## How To ?

__Hermes Lingo Query__ is based on API Key requests. Normally, to send an API request, `x-api-key` must be provided in headers.
So to use __Hermes Lingo Query__ you have to create an account and get an API Key. Then send a request with `x-api-key` in the headers or in request parameters (it's not recommended to send request with credentials in URL parameters). Or if you're logged in, the system will use your API Key (based on the authenticated in user).

## API endpoints

### /dictionary/

Query parameters:

- `word` : (*required*) Word to look for
- `x-api-key` : (*not required*) YOUR API KEY

### /translate/

- `from` : (*required*) Input language code
- `to` : (*required*) Output language code
- `sentence` : (*required*) Sentence to translate
- `x-api-key` : (*not required*) YOUR API KEY

## Documentation

- Swagger UI like documentation : <http://127.0.0.1:8000/api/docs/ui/>
- ReDoc like documentation : <http://127.0.0.1:8000/api/docs/>

Responses and models are described when accessing UI docs
