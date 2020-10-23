from flask import Flask, jsonify, request
import json
from infra_api import Infra

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def read_infra():
    try:
        with open("infra.json", "r") as f:
            content = f.read()
    except:
        raise Exception("Impossible d'ouvrir le fichier en lecture!")
    return json.loads(content)

def write_infra(data):
    try:
        with open("infra.json", "w") as f:
            content = f.write(json.dumps(data))
    except Exception as e:
        raise Exception("Impossible d'ouvrir le fichier en écriture! %s" % e)

@app.route("/reinit")
def reinit():
    infra = Infra("https://dismorphia.info/apiformation")
    write_infra(infra.list_allinfo())
    return ""

def get_machines():
    response = []
    for item in read_infra():
        print(item)
        response.append(item)
    return response

@app.route("/machines/<name>")
def api_get_machine_by_name(name):
    machines = get_machines()
    for machine in machines:
        if machine["name"] == name:
            return jsonify(machine)
    return "Machine inconnue", 404
    #return jsonify([machine for machine in get_machines() if machine["name"] == name])

@app.route("/machines")
def api_get_all_machines():
    return jsonify(get_machines())

@app.route("/machines", methods=['POST'])
def api_create_machine():
    try:
        data = json.loads(request.data)
        assert isinstance(data, dict), "Json must be a dictionary"
        assert "name" in data, "You must provide name"
        assert "owner" in data, "You must provide owner"
        assert "os" in data, "You must provide os"
        assert "ram" in data, "You must provide ram"
        assert data["name"].isalnum(), "The name has to be alphanumeric"
        assert data["owner"].isalnum(), "The owner has to be alphanumeric"
        assert data["os"].isalnum(), "The os has to be alphanumeric"
        assert isinstance(data["ram"],(int,float)), "The ram has to be a float or int"
        assert data["ram"] <= 64.0, "The ram can't be more than 64 GB"
    except Exception as e:
        return "Data must be Json: %s" % str(e), 400
    infra = get_machines()
    for machine in infra:
        if machine["name"] == data["name"]:
            return f"Machine with name {data['name']} already exists", 400
    infra.append(data)
    write_infra(infra)
    
    return request.data
    
@app.route("/machines", methods=['DELETE'])
def api_delete_machine():
    try:
        data = json.loads(request.data)
        assert isinstance(data, dict), "Json must be a dictionary"
        assert "name" in data, "You must provide name"
        assert data["name"].isalnum(), "The name has to be alphanumeric"
    except Exception as e:
        return "Data must be Json: %s" % str(e), 400
    infra = get_machines()
    for machine in infra:
        if machine["name"] == data["name"]:
            infra.remove(machine)
            write_infra(infra)
            return ""
    return f"Machine with name {data['name']} doesn't exists", 400
    
    
    
