import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Jag använder alltså requests för att hämta sidan, 
# och BeautifulSoup för att analysera innehållet.

#Skapa en meny där man kan välja olika funktioner
    # sök efter comments
    #   


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

# Function that takes an url and a keyword that must be present in the url.
def spider_urls(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"Request failed {url}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        
    else:
      print(f"Got status code {response.status_code} from {url}")

    for urls2 in urls:
        if urls2 not in visited_urls:
            visited_urls.add(urls2)
            url_join = urljoin(url, urls2)
            if keyword in url_join:
                print(url_join)


url = input("What URL would you like to cr4wl over: ")
keyword = input("Enter a keyword that should be present in the url: ")

spider_urls(url, keyword)