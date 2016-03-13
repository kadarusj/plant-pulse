#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import json
import jinja2
import webapp2
import logging
from datetime import datetime

from models import Plant

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+ "/htmls"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class DateTimeEncoder(json.JSONEncoder):
   def default(self, obj):
      if isinstance(obj, datetime):
         # format however you like/need
         return obj.strftime("%Y-%m-%d %H:%M:%S")
      # pass any other unknown types to the base class handler, probably
      # to raise a TypeError.   
      return json.JSONEncoder.default(self, obj)


class PlantHandler(webapp2.RequestHandler):
    
    def post(self):
        plant_body = self.request.body
        plant_json = json.loads(plant_body)

        nu_plant = Plant(pod_id=plant_json['pod_id'], node_id=int(plant_json['node_id']),
                         node_location=plant_json['node_location'], lux=int(plant_json['lux']), 
                         broadband=int(plant_json['broadband']), infrared=int(plant_json['infrared']),  
                         air_temp=float(plant_json['air_temp']), humidity=float(plant_json['humidity']), 
                         heat_index=float(plant_json['heat_index']), soil_temp=float(plant_json['soil_temp']), 
                         soil_moist1=int(plant_json['soil_moist1']), soil_moist2=int(plant_json['soil_moist2']), 
                         plant_volt=float(plant_json['plant_volt']), batt_volt=float(plant_json['batt_volt']))	
        nu_plant.put()
        
    def get(self):
        dt_start = self.request.get("dt_start")
        dt_end = self.request.get("dt_end")
        
        ##plant_datas = Plant.query_all()
        plant_datas = {
            "data": [p.to_dict() for p in Plant.query_all()]
        }
        
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(json.dumps(plant_datas, cls=DateTimeEncoder))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = { 
            "title": "Plant Pulse"
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/plant-data', PlantHandler)
], debug=True)
