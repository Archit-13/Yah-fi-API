import requests
from bs4 import BeautifulSoup as soup
url='https://ca.finance.yahoo.com/quote/GOOGL/analysis?p=GOOGL&.tsrc=fin-srch'
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
    if (lists[i]=="Earnings Estimate"):
        lists.pop(i+1)
        lists.pop(i+3)
        lists.pop(i+5)
        lists.pop(i+6)
        lists[i+1]=lists[i+1].replace('.','/')
        lists[i+3]=lists[i+3].replace('.','/')
        lists[i+1]+=lists[i+2]
        lists[i+3]+=lists[i+4]
        lists.pop(i+2)
        lists.pop(i+3)        
        j=i
    elif (lists[i]=="Earnings Estimate"):
        lists.pop(i+1)
        lists.pop(i+3)
        lists.pop(i+5)
        lists.pop(i+6)
        lists[i+1]=lists[i+1].replace('.','/')
        lists[i+3]=lists[i+3].replace('.','/')
        lists[i+1]+=lists[i+2]
        lists[i+3]+=lists[i+4]
        lists.pop(i+2)
        lists.pop(i+3)        
        
    elif (lists[i]=="Revenue Estimate"):
        lists.pop(i+1)
        lists.pop(i+3)
        lists.pop(i+5)
        lists.pop(i+6)
        lists[i+1]=lists[i+1].replace('.','/')
        lists[i+3]=lists[i+3].replace('.','/')
        lists[i+1]+=lists[i+2]
        lists[i+3]+=lists[i+4]
        lists.pop(i+2)
        lists.pop(i+3)        
    elif (lists[i]=="EPS Trend"):
        lists.pop(i+1)
        lists.pop(i+3)
        lists.pop(i+5)
        lists.pop(i+6)
        lists[i+1]=lists[i+1].replace('.','/')
        lists[i+3]=lists[i+3].replace('.','/')
        lists[i+1]+=lists[i+2]
        lists[i+3]+=lists[i+4]
        lists.pop(i+2)
        lists.pop(i+3)        
    elif (lists[i]=="EPS Revisions"):
        lists.pop(i+1)
        lists.pop(i+3)
        lists.pop(i+5)
        lists.pop(i+6)
        lists[i+1]=lists[i+1].replace('.','/')
        lists[i+3]=lists[i+3].replace('.','/')
        lists[i+1]+=lists[i+2]
        lists[i+3]+=lists[i+4]  
        lists.pop(i+2)
        lists.pop(i+3)

    elif lists[i]=="":
        break

csv=[]
#print(i)
while j<i:
        csv.append([lists[j],lists[j+1],lists[j+2],lists[j+3],lists[j+4]])
        j+=5
finalcsv=''
for x in csv :
    for i in x:
        finalcsv+=i.replace(","," ")+","
    finalcsv+="\n"
f=open('analysis.csv','w')
f.write(finalcsv)
f.close()
for x in csv:
    print(x)
