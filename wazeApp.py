
import loaddata
import json
from flask import Flask, render_template, request
from directions import getDirections
nodedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt"
edgedirectory="/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt"
coordinateDict={}
edgeConnections={}
edgeDistance={}
nodeAdj={}


app = Flask(__name__)
vertices = loaddata.loadNodes(nodedirectory)
x=None
@app.route('/', methods=['GET', 'POST'])
def index():
    global vertices
    if request.method=='POST':
        global x
        x=(int((request.get_data())))
        setedges()
        return render_template("waze.html", vertices=vertices)
    else:
        return render_template("waze.html", vertices=vertices)

directionNodes=[]
paths=[]
@app.route('/directions', methods=['GET', 'POST'])
def directions():
    global vertices
    global paths
    if request.method=='POST':
        global directionNodes
        if (len(directionNodes)>1):
            directionNodes=[]
        directionNodes.append(((request.get_data())))
        if (len(directionNodes) ==2 ):
            paths = getDirections(directionNodes[0], directionNodes[1])
            path1()
            path2()
            path3()
            return render_template("directions.html", vertices=vertices)
    else:
        return render_template("directions.html", vertices=vertices)

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



@app.route('/distance', methods=['GET'])
def distance():
    global paths
    path1list = []
    path1list.append(paths[0]['cost'])
    path1list.append(paths[1]['cost'])
    path1list.append(paths[2]['cost'])
    return json.dumps(path1list, ensure_ascii=False)


@app.route('/path1', methods=['GET'])
def path1():
    global paths
    path1list=[]
    for edge in paths[0]['path']:
        path1list.append(vertices[int(edge)])
    fullpathlist=[]
    for coordinate in path1list:
        edgeDic = {}
        edgeDic["lat"] = coordinate[0]
        edgeDic["lng"] = coordinate[1]
        fullpathlist.append(edgeDic)
    return json.dumps(fullpathlist, ensure_ascii=False)

@app.route('/path2', methods=['GET'])
def path2():
    global paths
    path2list=[]
    for edge in paths[1]['path']:
        path2list.append(vertices[int(edge)])
    fullpathlist=[]
    for coordinate in path2list:
        edgeDic = {}
        edgeDic["lat"] = coordinate[0]
        edgeDic["lng"] = coordinate[1]
        fullpathlist.append(edgeDic)
    return json.dumps(fullpathlist, ensure_ascii=False)


@app.route('/path3', methods=['GET'])
def path3():
    global paths
    path3list=[]
    for edge in paths[2]['path']:
        path3list.append(vertices[int(edge)])
    fullpathlist=[]
    for coordinate in path3list:
        edgeDic = {}
        edgeDic["lat"] = coordinate[0]
        edgeDic["lng"] = coordinate[1]
        fullpathlist.append(edgeDic)
    return json.dumps(fullpathlist, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
    # loaddata.loadPoints("/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cnode.txt","/Users/shashank/Documents/school/Spring2016/ds2/wazeApp/cal.cedge.txt")
    # global vertices
    #
    # print pathlist
    # paths = getDirections('1', '4')
    # path1list = []
    # for edge in paths[0]['path']:
    #     path1list.append(vertices[int(edge)])
    # print path1list
    # fullpathlist = []
    # for coordinate in path1list:
    #     edgeDic = {}
    #     edgeDic["lat"] = coordinate[0]
    #     edgeDic["lng"] = coordinate[1]
    #     fullpathlist.append(edgeDic)