# Python-Goof
Snyk's vulnerable playground for exploring vulnerabilities in Python code, modules and containers.



### Python Bottle Web Cache Poisoning
#### GET parameter cloaking example
This is a proof-of-concept demonstration that closely follows the narrative in https://snyk.io/blog/cache-poisoning-in-popular-open-source-packages/ 

1. `docker-compose up --build`

This will build container images and start up the vulnerable Python bottle example
fronted by an Nginx pass-through-proxy with caching keyed on the `q` argument of any request passed into it.

2. In a browser (or via curl/wget) open `http://localhost/search/?q=cat`

As expected, this should return:
```
Your search query: cat`
```

3. Now open `http://localhost/search/?q=dog&utm_content=1;q=snake!`

Notice that now you've gotten a `snake!` back instead of a `dog`:
```
Your search query: snake!
```
This is because the `;` character is treated by Bottle like an `&` in most URI parsers
and when you pass an argument twice in a URI, the last one overrides any earlier ones.

4. Finally, open `http://localhost/search/?q=dog`

And note that you are still getting a `snake!` back, even though the URI clearly 
only has `q=dog` in it.
```
Your search query: snake!
```
Here we are seeing the result of the cache poisoning.  The nginx cache is keyed off
of the `q=` argument which, when it first saw `q=dog` cached the `snake!` response.
Until the cache expires, it will continue to return that _poisoned_ cache data.
The flaw is in the application, Bottle, which should not be treating the non-standard `;`
character as an argument seperator.

This is fixed in Bottle version 0.12.19 or newer.
