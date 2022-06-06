# MyDictionary version 2

Recreate MyDictionary with sophisticated structures.


## TODO

- src
  - main.py
    - 1. find cache, when found it, show this.
    - 2. if cached word_info not found, fetch WEBLIO HTML
    - 2.1. create cached file 

  - api.py
    - fetch WEBLIO HTML 

  - cache.py
    - cache WEBLIO HTML
    - but not cached HTML file directly
    - after convert HTML to smart data structure, then create cached files.
    
  - parse.py (core feature)
    - parsing fetched WEBLIO HTML
    - The display of Weblio HTML varies depending on the part of speech of the Engligh word.
    - verb, adjective, noun, ...

  - prettify.py
    - show word info using colored, bold, underlined string :^)
    - but not must, I wish I could

