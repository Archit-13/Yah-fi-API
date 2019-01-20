from flask import Flask, jsonify
import csv
import json
app = Flask(__name__)


@app.route("/historical")
def hello():
    
    # Open the CSV.
    f = open( 'historical.csv', 'r' )
    # Change each fieldname to the appropriate field name. ...
    reader = csv.DictReader( f, fieldnames = ( 'Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'
     ))
    # Parse the CSV into JSON.
    finaljson = [ row for row in reader ][1:] 
    #out = json.dumps({'value' : finaljson})
    #out = json.dumps(finaljson)
    #print(out)
    
    return jsonify(finaljson)

@app.route("/profile")
def hello():
    
    # Open the CSV.
    f = open( 'profile.csv', 'r' )
    # Change each fieldname to the appropriate field name. ...
    reader = csv.DictReader( f, fieldnames = ( 'Names', 'Position', 'Salary', 'N/A', 'Year'))
    # Parse the CSV into JSON.
    finaljson = [ row for row in reader ][1:] 
    #out = json.dumps({'value' : finaljson})
    #out = json.dumps(finaljson)
    #print(out)
    
    return jsonify(finaljson)

@app.route("/analysis")
def hello():
    
    # Open the CSV.
    f = open( 'analysis.csv', 'r' )
    # Change each fieldname to the appropriate field name. ...
    reader = csv.DictReader( f)
    # Parse the CSV into JSON.
    finaljson = [ row for row in reader ][1:] 
    #out = json.dumps({'value' : finaljson})
    #out = json.dumps(finaljson)
    #print(out)
    
    return jsonify(finaljson)

@app.route("/financials")
def hello():
    
    # Open the CSV.
    f = open( 'financials.csv', 'r' )
    # Change each fieldname to the appropriate field name. ...
    reader = csv.DictReader( f)
    # Parse the CSV into JSON.
    finaljson = [ row for row in reader ][1:] 
    #out = json.dumps({'value' : finaljson})
    #out = json.dumps(finaljson)
    #print(out)
    
    return jsonify(finaljson)

@app.route("/hello")
def hiThere():
    return "Hi There!"
