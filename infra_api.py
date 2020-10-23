import requests
import json

class Infra():
    
    def __init__(self,url):
        self.url = url
        
    def list(self):
        machines = []
        response = requests.get(self.url+"/machines")
        if (response.status_code) != 200:
            raise Exception(response.text)
        for item in json.loads(response.text):
            machines.append(item["name"])
        return machines
    
    def get(self,name):
        response = requests.get(self.url+"/machines/"+name)
        if (response.status_code) != 200:
            raise Exception(response.text)
        return json.loads(response.text)
    
    def create(self,name,owner,os,ram):
        payload = {"name": name, "os": os, "ram": ram, "owner": owner}
        response = requests.post(self.url+"/machines", data=json.dumps(payload))
        if (response.status_code) != 200:
            raise Exception(response.text)
        return json.loads(response.text)
        
        
    def delete(self,nom):
        response = requests.request("DELETE", self.url+"/machines/"+nom)
        if (response.status_code) != 200:
            raise Exception(response.text)
        
    def start(self,nom):
        response = requests.post(self.url+"/machines/"+nom+"/start")
        if (response.status_code) != 200:
            raise Exception(response.text)
    
    def stop(self,nom):
        response = requests.post(self.url+"/machines/"+nom+"/stop")
        if (response.status_code) != 200:
            raise Exception(response.text)
    
    def restart(self,nom):
        response = requests.post(self.url+"/machines/"+nom+"/restart")
        if (response.status_code) != 200:
            raise Exception(response.text)
        
    def list_allinfo(self):
        machines = []
        response = requests.get(self.url+"/machines")
        if (response.status_code) != 200:
            raise Exception(response.text)
        for item in json.loads(response.text):
            machines.append(item)
        return machines
        
