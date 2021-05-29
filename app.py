#from flask import Flask, request, render_template, url_for, redirect, jsonify, json
from flask import *
import request as rqt

app = Flask(__name__)



@app.route('/nodes',methods=['GET'])
def nodes():
    nodes = rqt.get_nodes()
    return Response(jsonify(nodes),status=200)



@app.route("/nodes/<id>",methods=['GET'])
def get_node_info(id):
    node_info = rqt.get_node_info(id)
    return Response(jsonify(node_info),status=200)



@app.route("/nodes/<id>/deploy/<program>",methods=['POST'])
def node_deploy(id,program):
    success, error = rqt.deploy_node(id)
    if success:
        return Response(status=200)
    else:
        return Response(jsonify(error),status=404)


@app.route("/nodes/<id>/start",methods=['POST'])
def start_node(id):
    return Response("started node with ID="+str(id),status=200)



@app.route("/nodes/<id>/stop",methods=['POST'])
def stop_node(id):
    return Response("stopped node with ID="+str(id),status=200)



@app.route("/nodes/<id>/pause",methods=['POST'])
def pause_node(id):
    return Response("paused node with ID="+str(id),status=200)



@app.route("/nodes/<id>/resume",methods=['POST'])
def resume_node(id):
    return Response("resumed node with ID="+str(id),status=200)



@app.route("/nodes/<id>/restart",methods=['POST'])
def restart_node(id):
    return Response("restarted node with ID="+str(id),status=200)


@app.route("/nodes/<id>/logs",methods=['get'])
def get_node_logs(id):
    return Response("Some logs",status=200)



@app.route("/network",methods=['GET'])
def get_network_info():
    return Response("Some info",status=200)



if __name__ == "__main__":
    app.run(port=4444,debug=True)