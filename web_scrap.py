# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:18:46 2018

@author: Sebastian
"""


from bs4 import BeautifulSoup
import requests

def analyse(url):
    # Guarantees only "n" links in the dictionary "url"
    if(len(urls['nodes'])< length):
        try:
            # Append to urls["nodes"] to then ensure that urls are not repeated
            urls["nodes"].append(url)
            
            #In urls['graph'][url] are saved all the links to where you can go from this "url"
            urls['graph'][url] = []
            

            #To get the url if the link is in the same directory as the current url
            url_aux = url.split('/')            
            first_url = url_aux[0]+'//'+url_aux[2]


            # Getting the webpage, creating a Response object.
            response = requests.get(url)

            # Extracting the source code of the page.
            data = response.text

            # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
            soup = BeautifulSoup(data, 'lxml')

            # Extracting all the <a> tags into a list.
            tags = soup.find_all('a')

            # Extracting URLs from the attribute href in the <a> tags.
            for tag in tags:
                aux = tag.get('href')
                #Ensure that are external links or not redirects to the same page
                if aux!=None and aux[0]!='#' and aux != '/' and aux != './':
                    array_aux = aux.split('/')
                    
                    #To get the url if the link is in the same directory as the current url                    
                    if array_aux[0]!='https:' and array_aux[0]!='http:':
                        aux = first_url + aux

                    #Ensure that urls are not repeated
                    if aux not in urls['graph']:
                        urls['graph'][url].append(aux)

                    #Ensure that urls are not repeated
                    if aux not in urls["nodes"]:
                        analyse(aux)

        except:
            pass

def get_name(url):
    try:
        # Getting the webpage, creating a Response object.
        response = requests.get(url)

        # Extracting the source code of the page.
        data = response.text

        # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
        soup = BeautifulSoup(data, 'lxml')

        #title of this page
        name = soup.title.string
    except:
        name = 'Not found'
    return name

def Web_scrap(url, num):
    #SAVE THE DATA OF THE URLS
    global urls
    urls = {}
    urls['nodes'] = []
    urls['graph'] = {}

    
    graph =  {}
    graph['nodes'] = []
    graph['links'] = []



    global length
    length = num

    analyse(url)


    #PASS INFORMATION IN URLS TO GRAPH, TO LATER CONVERT THE LATTER INTO A JSON FILE
    for url in urls['nodes']:
        name = get_name(url)

        graph['nodes'].append({
          'id': url,
          'name': name
        })



    #PASS INFORMATION IN URLS TO GRAPH, TO LATER CONVERT THE LATTER INTO A JSON FILE
    for g in urls['graph']:
        for l in urls['graph'][g]:
            if l in urls['nodes']:
                graph['links'].append({
                  'source': g,
                  'target': l
                })

    return graph