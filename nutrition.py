import json
from flask import Flask, render_template, request, redirect, url_for, session
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import wolframalpha
client=wolframalpha.Client('API_KEY')
authenticator = IAMAuthenticator('API_KEY')

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/80c78105-880f-4bb7-b79c-93764795ee73') 
url="https://media.self.com/photos/606ccf537369ccb45ca42214/4:3/w_384/DiGiorno-Gluten-Free-Pizza-Pepperoni.jpg"
classes = visual_recognition.classify(url=url,classifier_ids='food').get_result()	
data=json.dumps(classes,indent=4)
data2=json.loads(data)
query=data2["images"][0]['classifiers'][0]["classes"][0]["class"]
print(query)
res=client.query(query+" nutrition")  
output=next(res.results).text
print(output)
