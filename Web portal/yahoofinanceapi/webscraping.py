import requests
from bs4 import BeautifulSoup
def createCSV(stockname= "MSFT"):
    
    

  

    url = "https://finance.yahoo.com/quote/%s/history?p=MFST"%(stockname)
    
    print(url)
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
    print(lines)
    f = open("Historicaldata.csv","w")
    f.write(lines)
    f.close()    
    
createCSV()