import os
import sys
import argparse
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from termcolor import colored
import re
from colorama import init

SEPARATOR='############################################################'

# not used for now
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def get_post_list():
    page = 'https://www.zoso.ro/'
    soup = BeautifulSoup(urlopen(page), 'html.parser')
    post_list = soup.select('h3.post-title a')
    url_list = []
    for post in post_list:
        url_list.append(post['href'])
    for url in url_list[::-1]: # reverse the list
        print(url)
        print(SEPARATOR)
        print()

def get_sorted_comments(url):
    #check if url is ok
    try:
        page = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            print('URL not found !')
            sys.exit()
    except ValueError:
        print("URL format not ok !")
        sys.exit()
    
    soup = BeautifulSoup(page, 'html.parser')

    comment_summary = []
    comment_list = soup.find_all('div', attrs={'class': 'comment-content'})
    # print(comment_list[0].prettify())
    for indx, comment in enumerate(comment_list):
        try:
            body = ''
            for c in comment.find_all('p'):
                body += ''.join(c.find_all(text = True))
            comment_summary.append(
                {
                    'body': body, 
                    'up': comment.span.find('i', attrs={'class': 'icon-thumbs-up'}).text,
                    'down': comment.span.find('i', attrs={'class': 'icon-thumbs-down'}).text
                })
        except Exception as e:
            pass
            # print(e)

    comment_summary_sorted = sorted(comment_summary, key= lambda i: int(i['up']))
    return comment_summary_sorted

def print_sorted_comments(comms_list):
    for com_sorted in comms_list:
        print(com_sorted['body'])
        print(colored(com_sorted['up'], 'green'), end=' / ')
        print(colored(com_sorted['down'], 'red'))
        print(SEPARATOR)
        print()

def ask_for_url():
    url = input('What is the url of the post: ')
    return url


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort comments from https://www.zoso.ro by rating')
    parser.add_argument('--url', help='The url endpoint of the post')
    parser.add_argument('-l', action='store_true', help='The list of posts')
    args = parser.parse_args()
    # os.system('color') #currently using colorama, so this is not useful anymore
    init()
    if args.l is True:
        get_post_list()
        sys.exit()
    if args.url == None:
        post_url = ask_for_url()
    else:
        post_url = str(args.url)
    comms = get_sorted_comments(post_url)
    print_sorted_comments(comms)
