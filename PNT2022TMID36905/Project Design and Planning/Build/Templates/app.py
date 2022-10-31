import cv2
import os
import numpy as np
from .utils import download_file
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import time
import numpy as np
from playsound import playsound
import requests
from flask import Flask,request,render_template , redirect ,url_for

from cloudant.client import cloudant
#authentication api key
client= cloudant.iam('706e0078-3ce5-4335-8209-4cc3491785cb-bluemix',"T_ZjtFYJ1hPFRVKqL7QjoMmEwzP2SErsibV6Xt_vGqro",connect = True)
#create db using an initiated client
my_database = client.create_database('my_database')

#default home page or route

@app.route('/')