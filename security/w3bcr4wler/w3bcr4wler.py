import requests
from bs4 import BeautifulSoup
from urllib import *

# Jag använder alltså requests för att hämta sidan, 
# och BeautifulSoup för att analysera innehållet.

# https://en.wikipedia.org/wiki/Hacker


    


print(r"""
      
        /\  .-"^"-.  /\
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"-"-;///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
    -----------------------
     ---- W3BCR4WLER ----
""")

visited_urls = set()


def spider_urls(url, keyword):
    pass
    #response = requests.get(url)
    #soup = BeautifulSoup(response.content, "html.parser")

















url = input("What URL would you like to cr4wl over: ")
keyword = input("Enter a keyword that should be present in the url: ")

spider_urls(url, keyword):