import json
import os
import requests

from bs4 import BeautifulSoup
URL = "https://www.imdb.com/india/top-rated-indian-movies/"
sample=requests.get(URL)
soup=BeautifulSoup(sample.text,"html.parser")
#lister = soup.select('.titleColumn')
def scrap_top_list():
    h=[]
    keys=['name','year','position','rating','url']
    d={key: None for key in keys}
    h=[]
    table= soup.find_all('tr')
    
    for ele in table:
        result = ele.find_all('td', {'class': 'titleColumn'} )
        rating = ele.find_all('td', {'ratingColumn imdbRating'})
        for link in result:
            a=link.find('a')
            l1=(a.get('href'))
            l2=(link.get_text())
            l2=l2+l1

            for link1 in rating:
                l3 = link1.get_text()
                l2=l2+l3

            l2=l2.strip()
            l2=((l2.split('\n')))
            mystr=['0']*len(l2)
            x=l2[0].replace('.','')
            mystr[2]=int(x)
            mystr[0]=l2[1].strip()
            y=l2[2][1:5]
            mystr[1]=int(y)

            mystr[3]=float(l2[4])
            mystr[4]='https://www.imdb.com'+l2[3]
            
            for i in range(len(mystr)):
                d[keys[i]]=mystr[i]
            d1=d.copy()
            h.append((d1))
    return h

def movies_by_year():
    movies=scrap_top_list()
    mov_year=[]
    for mov in movies:
        mov_year.append(mov['year'])
    mov_year=sorted(mov_year)
    #print(mov_year)
     
    mov_d={key: [] for key in mov_year}
    #print(mov_d)
    
    for mov in movies:
        mov_d[mov['year']].append( mov)
    return (mov_d)

def movies_by_decade():
    mov_by_year=movies_by_year()
    year=list(mov_by_year.keys())
    first_decade=year[0]//10 *10
    if (year[len(year)-1]%10 ==0):
        last_decade= year[len(year)-1]
    else:
        last_decade = year[len(year)-1]//10*10 + 10
    
    decade_list=[]
    for i in range(first_decade,last_decade+1,10):
        decade_list.append(i)
    
    decade_d={key: [] for key in decade_list}
    for i in range(first_decade,last_decade+10,10):  
        for j in year:
            if j>=i and j < i+10:
                decade_d[i].append(mov_by_year[j])
                
    return (decade_d)
    
def scrape_movie_details(URL):
    sample=requests.get(URL)
    soup=BeautifulSoup(sample.text,"html.parser")
    
    title= soup.find('h1')
    title=title.get_text()
    name=title[:len(title)-8]
    print(name)
    
    subpart = soup.find_all('div',{'subtext'})
    items=(subpart[0].get_text())
    items=items.split('|')
    item_runtime=items[1].strip()
    item_gener=(items[2].strip().split())
    
    story = soup.find('div', {'summary_text'})
    story=(story.get_text().strip())
    Director = soup.find('div', {'credit_summary_item'})
    Director=(Director.get_text()).split(":")
    Director=Director[1].strip().split(",")
    
    poster= soup.find('div',{'poster'})
    poster=(poster.find('a').find('img'))
    poster=poster.get('src')
    
    bhasha= soup.find_all('div',{'txt-block'})
    for b in bhasha:
        m=(b.find_all())
        if (m[0].get_text()) == ('Language:'):
            audio = (m[1].get_text()).split(" ")
            
        if (m[0].get_text()) == 'Country:' :
            item_country = (m[1].get_text())  
    
    keys=['name','director','country','language','poster_image_url','bio','runtime','gener']
    h={key: None for key in keys}
    
    h['name']=name
    h['director']=Director
    h['country'] = item_country
    h['language'] = audio
    h['poster_image_url'] = poster
    h['bio'] = story
    h['runtime'] = item_runtime
    h['gener'] = item_gener
    
#    print(h)
    
    return h
url = "https://www.imdb.com/title/tt0066763/"

def movie_details():
    get_movie_list_details=[]
    top_movies = scrap_top_list()[:10]

    for mov in top_movies:
        if mov['name'] != 'Thevar Magan':
            u=scrape_movie_details((mov['url']))

            get_movie_list_details.append(u)
    return (get_movie_list_details)

def count_language():
    hmap={}
    movies_list=movie_details()

    for mov in movies_list:
        list1=mov['language']
        for item in list1:
            if item in hmap:
                hmap[item] +=1
            else:
                hmap[item] =1
    return (hmap)

def count_director():
    hmap={}
    director_list=movie_details()
#    print(movies_list)
    for mov in director_list:
        list1=mov['director']
        for item in list1:
            if item in hmap:
                hmap[item] +=1
            else:
                hmap[item] =1
    return hmap
 
a = scrap_top_list()
# b = movies_by_year()
# c = movies_by_decade()
# d = movie_details()
# e = count_language()
# f = count_director()
# g = scrape_movie_details()  #need to provide the url of movie page

print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
        