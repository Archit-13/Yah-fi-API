from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import *
from django.template import RequestContext
#from .webscraping import createCSV

# Create your views here.
from django.http import HttpResponse
from .forms import personalForm
from bs4 import BeautifulSoup as soup


import requests
#import CsvJson
from flask import Flask, jsonify
import csv
import json
app = Flask(__name__)

#import helloworld.py
from bs4 import BeautifulSoup


def home(request):
     form = personalForm(request.POST or None)
     if form.is_valid():
          picked = form.cleaned_data.get('StockName')
          createCSV(picked)
          analysis(picked)
          financials(picked)
          profile(picked)
          
          f= open("historical.csv","r")
          lines = f.readlines()
          linesstr = "\n<br/>".join(lines)
          print(lines)
          return HttpResponse(linesstr)
          
          
     else:
          form = personalForm

     return render(request,'form_template.html', {'form':form })


def createCSV(stockname = "MSFT"):
     url = "https://finance.yahoo.com/quote/%s/history?p=%s"%(stockname, stockname)

     #print(url)
     response = requests.get(url)
     soup = BeautifulSoup(response.text, "html.parser")
     lst = soup.findAll("span")
     megalisa = []
     for items in lst:
          items = str(items)
          lst2 = items.split(">")
          lst3 = []
          lst4 = []
          try:
               for stuff in lst2:

                    if stuff[0] != "<":
                         lst3.append(stuff)
          except:
               pass
          for zuzu in lst3:
               if len(lst3) == 1:
                    lst4.append(lst3[0].split("<")[0])
          megalisa.append(lst4)
          #print(lst4)

     monalisa = megalisa[29::]
     vincci = []
     for smile in monalisa:
          if (smile[0] == "*Close price adjusted for splits."):
               break
          vincci.append(smile)

     lines = vincci[0][0]
     lisa = ["J","F","M","A","S","O","N","D"]
     for stuff in vincci:
          try:
               stuff = float(stuff)
          except:
               pass
     for i in range(1,7):
          lines += "," + vincci[i][0]

     for i in range(7,len(vincci)):
          vincci[i][0] = vincci[i][0].replace(",","")
          if(vincci[i][0][0] in lisa):
               lines += "\n"

          elif(i<len(vincci)-1):

               lines+= ","
          lines+=vincci[i][0]
     #print(lines)
     f = open("historical.csv","w")
     f.write(lines)
     f.close()   
     jsonMaker1()     

def analysis(stockname = "MSFT"):
     url='https://ca.finance.yahoo.com/quote/%s/analysis?p=%s&.tsrc=fin-srch'%(stockname, stockname)
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
     jsonMaker2() 
     

def financials(stockname = "MSFT"):
     url='https://ca.finance.yahoo.com/quote/%s/financials'%(stockname)
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
     jsonMaker3() 
     
     
     
def profile(stockname = "MSFT"):
     url='https://ca.finance.yahoo.com/quote/%s/profile?p=%s&.tsrc=fin-srch'%(stockname, stockname)
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
     jsonMaker4() 

def jsonMaker1():
     # Open the CSV.
     f = open( 'historical.csv', 'r' )
     # Change each fieldname to the appropriate field name. ...
     reader = csv.DictReader( f, fieldnames = ( 'Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'
                                               ))
     # Parse the CSV into JSON.
     finaljson = [ row for row in reader ][1:] 
     out = json.dumps({'value' : finaljson})
     print(out)
     f = open( 'historical.json', 'w' )
     f.write(out)
     f.close()
     
def jsonMaker2():
     # Open the CSV.
     f = open( 'analysis.csv', 'r' )
     # Change each fieldname to the appropriate field name. ...
     reader = csv.DictReader( f)
     # Parse the CSV into JSON.
     finaljson = [ row for row in reader ][1:] 
     out = json.dumps({'value' : finaljson})
     print(out)
     f = open( 'analysis.json', 'w' )
     f.write(out)
     f.close()
     
def jsonMaker3():
     # Open the CSV.
     f = open( 'financials.csv', 'r' )
     # Change each fieldname to the appropriate field name. ...
     reader = csv.DictReader( f)
     # Parse the CSV into JSON.
     finaljson = [ row for row in reader ][1:] 
     out = json.dumps({'value' : finaljson})
     print(out)
     f = open( 'analysis.json', 'w' )
     f.write(out)
     f.close()
     
def jsonMaker4():
     # Open the CSV.
     f = open( 'profile.csv', 'r' )
     # Change each fieldname to the appropriate field name. ...
     reader = csv.DictReader( f)
     # Parse the CSV into JSON.
     finaljson = [ row for row in reader ][1:] 
     out = json.dumps({'value' : finaljson})
     print(out)
     f = open( 'profile.json', 'w' )
     f.write(out)
     f.close()

"""

@app.route("/")
def hello():

     # Open the CSV.
     f = open( 'Historicaldata.csv', 'r' )
     # Change each fieldname to the appropriate field name. ...
     reader = csv.DictReader( f, fieldnames = ( 'Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'
                                               ))
     # Parse the CSV into JSON.
     finaljson = [ row for row in reader ][1:] 
     #out = json.dumps({'value' : finaljson})
     #out = json.dumps(finaljson)
     #print(out)

     return jsonify(finaljson)

@app.route("/hello")
def hiThere():
     return "Hi There!"

"""