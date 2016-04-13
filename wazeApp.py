
import loaddata
import json
from flask import Flask, render_template, request
nodedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt"
edgedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt"
coordinateDict={}
edgeConnections={}
edgeDistance={}
nodeAdj={}


app = Flask(__name__)

x=None
@app.route('/', methods=['GET', 'POST'])
def index():
    vertices = loaddata.loadNodes(nodedirectory)
    if request.method=='POST':
        global x
        x=(int((request.get_data())))
        setedges()
        return render_template("waze.html", vertices=vertices)
    else:
        return render_template("waze.html", vertices=vertices)


@app.route('/edges', methods=['GET'])
def setedges():
    edgeMapList = loaddata.edgeMap(x, nodedirectory, edgedirectory)
    fullEdgeList=[]
    for coordinate in edgeMapList:
        edgeDic = {}
        edgeDic["lat"]=coordinate[0]
        edgeDic["lng"]= coordinate[1]
        fullEdgeList.append(edgeDic)
    return json.dumps(fullEdgeList, ensure_ascii=False)




if __name__ == '__main__':
    app.run()
    # loaddata.loadPoints("/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt","/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt")
    # edgeMapList = loaddata.edgeMap(4, nodedirectory, edgedirectory)
