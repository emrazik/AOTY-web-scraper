from bs4 import BeautifulSoup
import config
from playwright.sync_api import sync_playwright

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
        color_code = config.handle_text_color(critic_score)
        print('Critics: ' + color_code + str(critic_score) + config.TextColors.END)
        color_code = config.handle_text_color(user_score)
        print('Users: ' + color_code + str(user_score) + config.TextColors.END)