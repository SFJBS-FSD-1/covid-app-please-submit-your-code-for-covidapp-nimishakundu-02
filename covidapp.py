import json
import datetime
import requests
from flask import Flask,render_template,request
import os
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def covid():
    if request.method == 'POST':
        country=request.form["countrys"]
        print('country')
        url= "https://api.covid19api.com/summary"
        print(url)
        resp=requests.get(url)
        resp=resp.json()
        print(resp)

        dictdata={}
        rescountrydata = resp["Countries"]

        for countrydata in rescountrydata:
            if countrydata['Country'] == country:
                dictdata={'covid':countrydata['Country'],'TotalCases':countrydata['TotalConfirmed'],
                          'TotalDeaths':countrydata['TotalDeaths']}
                break

        return render_template('covidinfo.html',covidinfo=dictdata)
    else:
        dictdata= None
        return render_template('covidinfo.html',covidinfo=dictdata)

port = int(os.environ.get("PORT",5000))

if __name__ == "__main__":
    app.run(port=port)
















