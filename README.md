# AOTY-web-scraper
This python script provides basic web scraping capabilities for [albumoftheyear.org](https://www.albumoftheyear.org/) in order to gather data about your favorite albums and artists

### Installation
1. clone the repo
2. ```pip3 install pytest-playwright```
3. run ```pytest install```
4. ```pip3 install beautifulsoup```

### Usage
example usage:
```python3 main.py -AS -ar "artist's name" -al "album name"```

functions:

```-AS     Search for an album```

optional arguments:

```
-ar, --artist     Name of a musical artist
-al, --album      Name of an album
```

