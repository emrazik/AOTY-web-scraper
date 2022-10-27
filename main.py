from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def album_search(artist_name, album_name):
    with sync_playwright() as p:
        format_query = f'https://www.albumoftheyear.org/search/?q={artist_name}+{album_name}'
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
    artist_name = input("What artist? ")
    album_name = input("What album? ")
    album_search(artist_name, album_name)
 
if __name__ == "__main__":
    main()








