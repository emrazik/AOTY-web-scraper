from cgitb import text
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import argparse
import sys

FUNCTIONS = {'-AS'}

class textcolors:
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    END = '\u001b[0m'

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
        print('Artist: ' + html_parsed.find('div', {'class':'artist'}).text)
        print('Album: ' + html_parsed.find('div', {'class':'albumTitle'}).text + '\n')
        
        critic_score = int(html_parsed.find('a', {'href':'#critics'}).text)
        user_score = int(html_parsed.find('a', {'href':'#users'}).text)
        color_code = handle_text_color(critic_score)
        print('Critics: ' + color_code + str(critic_score) + textcolors.END)
        color_code = handle_text_color(user_score)
        print('Users: ' + color_code + str(user_score) + textcolors.END)

def handle_text_color(score):
    if score > 70:
        return textcolors.GREEN
    elif score > 50:
        return textcolors.YELLOW
    else:
        return textcolors.RED
    
def console_output():
    pass

def console_output_verbose():
    pass

def main():
    parser = argparse.ArgumentParser(description='Search for information on albumoftheyear.com')
    parser.add_argument('-AS', action='store_true', help='Search for an album')
    parser.add_argument('-ar', '--artist', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of a musical artist', metavar='')
    parser.add_argument('-al', '--album', type=str, required=any(func in sys.argv for func in FUNCTIONS), help='Name of an album', metavar='')
    args = parser.parse_args()

    print(args)
    if args.AS:
        album_search(args)
 
if __name__ == "__main__":
    main()








