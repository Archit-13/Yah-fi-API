import requests
from bs4 import BeautifulSoup as soup
url='https://ca.finance.yahoo.com/quote/YAHOY/profile?p=YAHOY&.tsrc=fin-srch'
obj=requests.get(url)
souppage=soup(obj.text,"html.parser")
tableithink=souppage.findAll("span")
lists=[]
for row in tableithink:
    lists.append(row)
i=0
for  i in range(len(lists)):
    lists[i]=str(lists[i]).split(">")
    if(len(lists[i])==5):
        lists[i]=lists[i][2].replace("<!-- /react-text --",'').replace("</span",'').replace("amp; "," ")
    #print(lists[i])
i=0
done = 1
while i <(len(lists)):
    if  ("Mr" or "Ms") in lists[i] and done:
        j=i
        done = 0
        i+=1
    elif (lists[i]=="N/A"):
            lists.pop(i+1)
            i+=1
    else:
        i+=1
    

csv=[]

k=j+25
while j<k:
    csv.append([lists[j],lists[j+1],lists[j+2],lists[j+3],lists[j+4]])
    j+=5
#print(csv)

finalcsv=''
for x in csv :
    for i in x:
        finalcsv+=i.replace(","," ")+","
    finalcsv+="\n"
f=open('profile.csv','w')
f.write(finalcsv)
f.close()
print("")
paraithink=souppage.findAll("p")
print(paraithink[2].text)
print("")


for x in csv:
    print(x)

print("")
