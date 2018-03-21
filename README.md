# CS50-FINAL-PROJECT
This project used web-scraping to create a directed graph with pages that you can go since one page via links.

## REFERENCES
Other codes that I used: 
  * https://codepen.io/miroot/pen/qwIgC?editors=1100
  * https://codepen.io/guzmonne/pen/VrJQQw
  * https://bl.ocks.org/iamkevinv/0a24e9126cd2fa6b283c6f2d774b69a2
  
 
## REQUIREMENTS
  * Python 3
  * Flask (Python Library) --> $ pip install Flask
  * Requests (Python Library) --> $ pipenv install requests
  * BeautifulSoup Version 4 (Python Library) --> pip install beautifulsoup4
  
## IDEA OF PROJECT
  Given a web page, you can go to others via links. 
  With this idea, this application given a url (indicating the web page) and the number of links you want to "visit" 
  (I put a limit, because from any web page you can go to almost any other page on the internet), create a directed 
  graph where the number of links is the number of nodes in the graph.
