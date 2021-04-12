import scrapp as scrap
import json
import os

if os.path.isfile('scrap_top_mylist1.json') :
#    print("I got this .....",scrap_top_mylist.json )
    myRecord = json.load(open('scrap_top_mylist1.json'))
    print("got1",myRecord)
    
else:
    scrap_top_mylist1=scrap.scrap_top_list()
    #print(scrap_top_mylist1)
    
    j = json.dumps(scrap_top_mylist1)
    with open ('scrap_top_mylist1.json', 'w') as f:
        f.write(j)
        f.close()
    
def mycache():
    if os.path.isfile('scrap_top_mylist1.json') :
#        print("I got this .....",scrap_top_mylist.json )
        myRecord = json.load(open('scrap_top_mylist1.json'))
        print("got1",myRecord)
    else:
        scrap_top_mylist5 = scrap_top_list()
        j = json.dumps(scrap_top_mylist5)
        with open ('scrap_top_mylist5.json', 'w') as f:
            f.write(j)
            f.close()