import json
import requests
import webbrowser
import sys
from rich import print
#sort by upvotes?
if len(sys.argv) == 2:
    r = requests.get("https://www.reddit.com/r/"+ str(sys.argv[1]) + "/hot.json",headers = {'User-agent': 'tha bot'})
else:
    r = requests.get("https://www.reddit.com/r/python/hot.json",headers = {'User-agent': 'tha bot'})
#r = requests.get("https://api.github.com")
#json.dumps(r.json(),indent = 4)
linklist = json.loads(r.text)
#print(linklist["data"])
links = []
linkstitle = []
upvotesamount = []
commentsamount = []
for x in range(0,20):
    links.append(json.dumps(linklist["data"]["children"][x]["data"]["permalink"],indent = 4))
    linkstitle.append(json.dumps(linklist["data"]["children"][x]["data"]["title"],indent = 4))
    upvotesamount.append(json.dumps(linklist["data"]["children"][x]["data"]["ups"],indent = 4))
    commentsamount.append(json.dumps(linklist["data"]["children"][x]["data"]["num_comments"],indent = 4))
    #print(json.dumps(linklist["data"]["children"][x]["data"]["permalink"],indent = 4),json.dumps(linklist["data"]["children"][x]["data"]["title"],indent = 4))
#print(links)
#sort
for x in range(len(upvotesamount)-1):
    for y in range(0,len(upvotesamount)-x-1):
        if int(upvotesamount[y]) < int(upvotesamount[y+1]):
            upvotesamount[y], upvotesamount[y+1] = upvotesamount[y+1], upvotesamount[y]
            links[y], links[y+1] = links[y+1], links[y]
            linkstitle[y], linkstitle[y+1] = linkstitle[y+1], linkstitle[y]
            commentsamount[y], commentsamount[y+1] = commentsamount[y+1], commentsamount[y]
for x,title in enumerate(linkstitle):
    print(f'{x}:Upvotes: {upvotesamount[x]} Comments: {commentsamount[x]} Title: {title}')
choice = 0
chosenlinks = []
while choice >= 0:    
    print("Please enter the corresponding number to the link you would like to open you can enter many numbers type -1 to stop")
    try:
        choice = int(input())
    except ValueError:
        print("That's not an int!")
    if choice >= 0:
        chosenlink = 'https://www.reddit.com' + links[int(choice)].strip('"')
        if chosenlink not in chosenlinks:    
            chosenlinks.append(chosenlink)
        print(chosenlink)
for x in chosenlinks:
    webbrowser.open(x)
#print(json.dumps(linklist["data"]["children"][0]["data"],indent = 4))
#next step could either be send over the title data to see if it is interesting and then open the browser if so
#for x in range(2,20):
#    print(json.dumps(linklist["data"]["children"][x]["data"]["permalink"],indent = 4))
