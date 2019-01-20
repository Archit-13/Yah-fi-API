import requests
from bs4 import BeautifulSoup as soup
url='https://ca.finance.yahoo.com/quote/GOOGL/financials'
obj=requests.get(url)
souppage=soup(obj.text,"html.parser")
tableithink=souppage.findAll("span")
lists=[]
for row in tableithink:
    lists.append(row)
for  i in range(len(lists)):
    lists[i]=str(lists[i]).split(">")[1].replace("</span","")
    #print(lists[i])
for  i in range(len(lists)):
    if (lists[i]=="Revenue"):
        j=i
    elif lists[i]=="":
        break
csv=[]
#print(i)
while j<i:
    if (any(k.isdigit() for k in lists[j+1])):
        csv.append([lists[j],lists[j+1],lists[j+2],lists[j+3],lists[j+4]])
        j+=5
    else:
        csv.append([lists[j]," "," "," "," "])
        j+=1
finalcsv=''
for x in csv :
    for i in x:
        finalcsv+=i.replace(","," ")+","
    finalcsv+="\n"

f=open('financials.csv','w')
f.write(finalcsv)
f.close()
for x in csv:
    print(x)