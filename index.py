#! /home/songwei/anaconda3/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import sys

import numpy as np
import io
import os
import scipy
import sklearn
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from QQScore import *
from qqJsonParse import *


QQJson = [
"SVMpredict",
"SVMscore",
"SVMdecision",
"RFpredict",
"RF0prob",
"RF1prob"
]

print("Status: 200 OK")
print ("Content-type:text/html")
print ()

#print ('<html>')
#print ('<head>')
#print ('<title>Hello</title>')
#print ('</head>')
#print ('<body>')
#print ('<h2>Hello Word! This is my first CGI program</h2>')
#print ('</body>')
#print ('</html>')

#totalByte = int(os.environ.get('HTTP_CONTENT_LENGTH'))
totalByte = os.environ.get('HTTP_CONTENT_LENGTH')
reqbin = io.open(sys.stdin.fileno(), "rb").read(totalByte)
reqstr=reqbin.decode("utf-8")
#print ("<h2>", reqstr, "</h2>")

'''
lineArr = reqstr.strip().split("|")
#        print (lineArr)
#dataMat = []
linelist=[]
for i in range(len(lineArr)):
    b = lineArr[i].strip()
    linelist.append( float(b) )
     #       print (linelist, len(lineArr))
#dataMat.append(linelist)
#print ("<h2>", linelist, "</h2>")
#end

#
'''

qqjson = qqJsonParse(reqstr)

linelist = qqjson.getData()

#print ("<h2>", linelist, "</h2>")


sc = joblib.load('../anacondaprj/qqml_sc.pkl')
clf_svm = joblib.load('../anacondaprj/qqml_svm.pkl')
clf_rf = joblib.load('../anacondaprj/qqml_rf.pkl')


X_test_std = np.mat(linelist)
X_test_std = sc.transform(X_test_std)

#print ("<h2>", X_test_std[0], "</h2>")
predict = clf_svm.predict(X_test_std[0])
qqscore = QQScore()

decision = clf_svm.decision_function(X_test_std[0])[0]
score = qqscore.score(decision)

ret = clf_rf.predict(X_test_std[0])
prob = clf_rf.predict_proba(X_test_std[0])
#'''
#print ("<h2>", predict, "</h2>")
#print ("<h2>", decision, "</h2>")
#print ('<h2> QQScore : %d  </h2'%(score) )
#print ("{", QQJson[0], ":\"", predict, "\",", QQJson[0], ":\"", qqscore.score(decision), "\"")
rfstr = "%d, %f, %f "%(ret[0], prob[0][0], prob[0][1])
#print ("<h2>RF:", rfstr,"</h2>")
#'''
retstr = "{\"%s\":\"%d\",\"%s\":\"%d\",\"%s\":\"%f\",\"%s\":\"%d\",\"%s\":\"%f\",\"%s\":\"%f\"}"%(QQJson[0], predict[0], QQJson[1], score,
                                                                                                  QQJson[2], decision, QQJson[3], ret[0],
                                                                                                  QQJson[4], prob[0][0], QQJson[5], prob[0][1])
print (retstr)
#'''

#'''