from flask import Flask, jsonify, request, json
from funciones import *
import pandas as pd
app = Flask(__name__)

@app.route('/biseccion', methods=['POST'])
def index():
	global f,xi,xs,tolerancia,niter,pandas, obj
	obj = request.get_json()
	f = f(obj['f'])
	xi = float(obj['xi'])
	xs = float(obj['xs'])
	tolerancia = float(obj['tolerancia'])
	niter = int(obj['niter'])
	fxi = evalfunct(f,xi)
	fxs = evalfunct(f,xs)
	xiList = []
	xsList = []
	xmList = []
	fxmList = []
	eAbList = []
	eRList = []
	if fxi == 0:
	    return jsonify({"message":"its a root", "value":xi})
	elif fxs == 0:
	    return jsonify({"message":"its a root", "value":xs})
	elif (fxi*fxs) < 0:
	    xm = (xi+xs)/2
	    fxm = evalfunct(f,xm)
	    contador = 1
	    eAb = 1
	    eR = 1
	    while eAb > tolerancia and fxm != 0 and contador < niter:
	        xiList.append(xi)
	        xsList.append(xs)
	        xmList.append(xm)
	        fxmList.append(fxm)
	        if (fxi*fxm) < 0:
	            xs = xm
	            fxs = fxm
	        else:
	            xi = xm
	            fxi = fxm
	        xaux = xm
	        xm = (xi+xs)/2
	        fxm = evalfunct(f,xm)
	        eAb = abs(xm - xaux)
	        eR = eAb/xm
	        eAbList.append(eAb)
	        eRList.append(eR)
	        contador = contador + 1
	        pandas = {'Xinf':xiList,'Xsup':xsList,'Xm':xmList,'f(xm)':fxmList,'Absolute Error':eAbList,'Relative Error':eRList}
	    if fxm == 0:
	    	return jsonify({"message":"its a root", "value":xm})
	    elif eAb < tolerancia:
	    	return jsonify({"message":"its a aproximation of a root", "value":xm, "error": eAb})
	    elif eR < tolerancia:
	        return jsonify({"message":"its a aproximation of a root", "value":xm, "error": eR})
	    else:
	        return jsonify({"message": "failed with iterations", "value": niter})
	else:
	    return jsonify({"message":"wrong interval"})     

if __name__ == '__main__':
	app.run(debug=True)
	