from bs4 import BeautifulSoup
import config
import playwright
from playwright.sync_api import sync_playwright
import sys

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

        # check whether the search returned anything or not
        try:
            page.click('.albumBlock')
        except playwright._impl._api_types.TimeoutError:
            print(config.TextColors.RED + "Time limit exceeded! This search couldn't be completed." + config.TextColors.END)
            sys.exit()

        html = page.inner_html('body')
        html_parsed = BeautifulSoup(html, 'html.parser')
        print('Artist: ' + html_parsed.find('div', {'class':'artist'}).text)
        print('Album: ' + html_parsed.find('div', {'class':'albumTitle'}).text + '\n')
        
        critic_score = html_parsed.find('div', {'class':'albumCriticScore'}).text
        user_score = html_parsed.find('div', {'class':'albumUserScore'}).text

        color_code = config.handle_text_color(critic_score)
        print('Critics: ' + color_code + str(critic_score) + config.TextColors.END)
        color_code = config.handle_text_color(user_score)
        print('Users: ' + color_code + str(user_score) + config.TextColors.END + '\n')

        # only print whats after this comment if the verbose flag is true
        if not args.verbose:
            sys.exit()

        # check whether the track list is available or not
        try:
            track_list_titles = html_parsed.find('table', {'class':'trackListTable'}).find('tbody').find_all('td', {'class':'trackTitle'})
            track_list_ratings = html_parsed.find('table', {'class':'trackListTable'}).find('tbody').find_all('td', {'class':'trackRating'})
        except:
            print(config.TextColors.RED + "No track list available!" + config.TextColors.END)
            sys.exit()

        print('Track List')
        for track in range(len(track_list_titles)):
            track_list_title = track_list_titles[track].find('a').text
            track_list_rating = track_list_ratings[track].text

            print(track_list_title + ': ' +  config.handle_text_color(track_list_rating) + track_list_rating + config.TextColors.END)
            
def top_albums_all_time(args):
    pass