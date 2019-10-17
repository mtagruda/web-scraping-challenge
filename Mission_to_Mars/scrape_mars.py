from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = { 'executable_path': '/Users/melissaagruda/bin/chromedriver-2'}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit https://mars.nasa.gov/news/
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)

    time.sleep(3)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_titles = soup.find('div', class_="content_title")
    news_title = news_titles.text
    print(news_title)

    time.sleep(3)


    news_ps = soup.find('div', class_="article_teaser_body")
    news_p = news_ps.text
    print(news_p)

#Find the src for the featured image
    url2 = 'http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    time.sleep(2)

    html2 = browser.html
    soup = BeautifulSoup(html2, 'html.parser')

    img = soup.find_all('a', class_="button fancybox")

    for a in img:
        print(a["data-fancybox-href"])
    
    url9 = "http://www.jpl.nasa.gov/"
    featured_image_url = url9 + a["data-fancybox-href"]

    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)

    time.sleep(3)

    soup = BeautifulSoup(browser.html, 'html.parser')

    mars_weather = soup.find(class_='tweet-text').text

    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)

    time.sleep(10)

    html4 = browser.html
    soup = BeautifulSoup(html4, 'html.parser')

    marsfacts = soup.find_all('table', class_="tablepress tablepress-id-p-mars")
    marsfacts

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    time.sleep(5)

    html5 = browser.html
    soup = BeautifulSoup(html5, 'html.parser')

    hemis_search = soup.find_all('a', class_="itemLink product-item")
    url10 = "https://astrogeology.usgs.gov"
    img_url =  []

    for a in hemis_search:
        print(a['href'])
        img_url.append(a['href'])

    url11 = url10 + img_url[0]
    url12 = url10 + img_url[2]
    url13 = url10 + img_url[4]
    url14 = url10 + img_url[6]

    browser.visit(url11)
    html11 = browser.html

    time.sleep(5)
    soup = BeautifulSoup(html11, 'html.parser')
    hemis_search2 = soup.find_all('img', class_="wide-image")
    for a in hemis_search2:
        print(a['src'])
    url15 = url10 + (a['src'])
    print(url15)

    browser.visit(url12)
    html12 = browser.html
    time.sleep(5)
    soup = BeautifulSoup(html12, 'html.parser')
    hemis_search3 = soup.find_all('img', class_="wide-image")
    for a in hemis_search3:
        print(a['src'])
    url16 = url10 + (a['src'])
    print(url16)

    browser.visit(url13)
    html13 = browser.html
    time.sleep(5)
    soup = BeautifulSoup(html13, 'html.parser')
    hemis_search4 = soup.find_all('img', class_="wide-image")
    for a in hemis_search4:
        print(a['src'])
    url17 = url10 + (a['src'])
    print(url17)

    browser.visit(url14)
    html14 = browser.html
    time.sleep(5)
    soup = BeautifulSoup(html14, 'html.parser')
    hemis_search4 = soup.find_all('img', class_="wide-image")
    for a in hemis_search4:
        print(a['src'])
    url18 = url10 + (a['src'])
    print(url18)


    hemisphere_image_url = [
    {"title": "Cerberus Hemisphere", "img_url": url15}, 
    {"title": "Schiaparelli Hemisphere", "img_url": url16},
    {"title": "Syrtis Major Hemisphere", "img_url": url17},
    {"title": "Valles Marineris Hemisphere", "img_url": url18}
    ]

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "url15": url15,
        "url16": url16,
        "url17": url17,
        "url18": url18       
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

