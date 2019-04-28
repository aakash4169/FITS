from flask import Flask, redirect, url_for, request, jsonify, make_response
import json
import uuid
import pymongo
import datetime
from flask_mail import Mail, Message
from flask_cors import CORS
from flask import Response
from flask import render_template,send_file
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.son import SON
from flask import Flask, Response,session                                                      
from flask import Flask, Response,request                                                      
from flask import Flask, render_template                                                       
import requests
import json
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

con = pymongo.MongoClient("mongodb://localhost:27017/")
collection = con.ssdi

@app.route('/requestForData', methods=["POST"])
def requestForData():
    print ("-~-~-~-~-~-~-~ requestForData -~-~-~-~-~-~-~-~")
    d = request.data
    print(d)
    total = []
    final = []
    cursor = collection.tread_depth


    # df=pd.read_csv('tread_depth.csv')
    
    # if d=='2':
            
    #         print(len(df))
    #         df1=df['tacho'].dropna()
    #         print(len(df1))
        
    
    if d=="tisize_rim":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$tisize_rim",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        
        for i in rims:
            total.append({
                "name":str(i['_id']),
                "value":int(i['count'])
            })
            
        for i in range(0, 10):
            final.append(total[i])

    elif d=="mileage":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$mileage",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        
        p = 0
        for i in rims:
            if p <= 10:
                total.append({
                    "name":str(i['_id']),
                    "value":int(i['count'])
                })
                p += 1
                
        for i in range(0, 10):
            final.append(total[i])

    elif d=="td_min":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$td_min",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        
        for i in rims:
            total.append({
                "name":str(i['_id']),
                "value":int(i['count'])
            })
            
        for i in range(0, 10):
            final.append(total[i])

    elif d=="td_mean":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$td_mean",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        
        for i in rims:
            total.append({
                "name":str(i['_id']),
                "value":int(i['count'])
            })
            
        for i in range(0, 10):
            final.append(total[i])

    elif d=="tacho":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$tacho",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        for i in rims:
            total.append({
                "name":str(i['_id']),
                "value":int(i['count'])
            })
        for i in range(0, 10):
            final.append(total[i])

    elif d=="tisize_width":
        pipeline = [
            {"$group" : 
                {
                    "_id" : "$tisize_width",           
                    "count": { "$sum": 1 }
                }
            },
            {"$sort": SON([("count", -1)]) }
        ]
        rims = cursor.aggregate(pipeline)
        
        for i in rims:
            total.append({
                "name":str(i['_id']),
                "value":int(i['count'])
            })
            
        for i in range(0, 10):
            final.append(total[i])

    
    
    print(final)
    return dumps(final), 200
    
if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')