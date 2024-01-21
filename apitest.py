import requests 
import json

URL = "http://127.0.0.1:8000/weatherapi/"

def get_data(id=None):
    data = {}
    if id is not None:
     data ={'id':id}
    json_data = json.dumps(data)
    r= requests.get(url= URL , data= json_data)
    data = r.json()
    print(data)

# get_data(1)
# get_data()


def post_data():
   data = {
      'city' : "cheetakeda",
      'temperature': -10,
       'humidity': -10,
       'weather_description':'bhot thand hai bhai' 
   }
   json_data = json.dumps(data)
   r= requests.post(url= URL , data= json_data)
   data = r.json()
   print(data)
# post_data()


#updateapi #put #patch #patialupdate #humidity is not change

def update_data():
   data = {
      'id' : 3,
      'city' : "indore",
      'temperature': 40,
       'weather_description':'bhot garmi hai bhai' 
   }
   json_data = json.dumps(data)
   r= requests.put(url= URL , data= json_data)
   data = r.json()
   print(data)
# update_data()

#delete

def delete_data():
   data = {
      'id' : 2
}
   json_data = json.dumps(data)
   r= requests.delete(url= URL , data= json_data)
   data = r.json()
   print(data)
delete_data()


