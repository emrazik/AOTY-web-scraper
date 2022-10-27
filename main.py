from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import argparse
import sys

FUNCTIONS = {'-AS'}

def album_search(args):
    query_list = args.artist.split() + args.album.split()

    format_query = 'https://www.albumoftheyear.org/search/?q=%'
    for item in query_list:
        format_query += item + '+'   
    format_query = format_query[:-1]

    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(format_query)
        page.click('.albumBlock')
        html = page.inner_html('body')
        html_parsed = BeautifulSoup(html, 'html.parser')
        print(html_parsed.find('div', {'class':'albumTitle'}).text)
        print(html_parsed.find('div', {'class':'artist'}).text)
        print(html_parsed.find('a', {'href':'#critics'}).text)
        print(html_parsed.find('a', {'href':'#users'}).text)

def console_output():
    pass

def console_output_verbose():
    pass

def main():
    parser = argparse.ArgumentParser(description='Search for information on albumoftheyear.com')
    parser.add_argument('-AS', action='store_true', help='Search for an album')
    parser.add_argument('-al', '--artist', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of a musical artist', metavar='')
    parser.add_argument('-ar', '--album', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of an album', metavar='')
    args = parser.parse_args()

    if args.AS:
        album_search(args)
 
if __name__ == "__main__":
    main()








