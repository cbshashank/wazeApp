
import loaddata
from flask import Flask, render_template, request

coordinateDict={}
edgeConnections={}
edgeDistance={}
nodeAdj={}


app = Flask(__name__)




@app.route('/')
def index():
    return render_template("waze.html")



if __name__ == '__main__':
    app.run()
    loaddata.loadPoints("/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt", "/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt")
