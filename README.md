# MyDictionary version 2

Recreate MyDictionary with sophisticated structures.  
My Goals are to create readable main.py flow, and pythonic classes, APIs.

## Flow

1. create cache_dir
   Cache.create_cache_dir()

2. get user inputs called 'word_name'
   if fail to get user inputs, END :^)
   word_name = user_input(sys.argv)

3. cache flow
   3.1 try to find 'word_name'.cache,
   if Cache.has_cache(word_name):
   if cache file is found, show this cache END :^)

   3.2 while not found 'word_name'.cache,
   create 'word_name'.cache

4. create cache flow
   4.1 get fetch data from WEBLIO API
   fetch_data('word_name')
   fetch_data = api.fetch_word(word_name)

   4.1.1 if fail to fetch, END :^)
   4.1.2 if success to fetch, parse fetch data (HTML data)

   4.2 success to parse fetch data,
   create 'word_name'.cache using parsed HTML

   4.3 show this cache END :^)

## cache json file structure

```json
{
  "word_name": "spell",
  "main_meaning": "綴り",
  "type_of_speech": {
    "verb": {
      "": ""
    },
    "adj": {
      "": ""
    },
    "noun": {
      "": ""
    }
  }
}
```
