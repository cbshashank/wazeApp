
import loaddata
from flask import Flask, render_template, request
nodedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt"
edgedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt"
coordinateDict={}
edgeConnections={}
edgeDistance={}
nodeAdj={}


app = Flask(__name__)



@app.route('/')
def index():
    vertices = loaddata.loadNodes(nodedirectory)
    return render_template("waze.html", vertices=vertices)


@app.route('/test')
def test():
    vertices = loaddata.loadNodes(nodedirectory)
    return render_template("test.html", vertices=vertices)



if __name__ == '__main__':
    app.run()
