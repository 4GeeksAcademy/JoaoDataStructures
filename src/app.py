"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure,FamilyMember
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

ribeiroFamily = FamilyStructure("Ribeiro")
myPeopleArray = [FamilyMember(0,"Joao", 29, [0,1,2,3,4,5,6]),
                 FamilyMember(0,"Mike", 29, [0,1,2,3,4,5,6]),
                 FamilyMember(0,"Ajay", 29, [0,1,2,3,4,5,6]),
                 FamilyMember(0,"Deepak", 29, [0,1,2,3,4,5,6])]


for people in myPeopleArray:
        ribeiroFamily.add_member(people)

for member in ribeiroFamily._members:
        print(member)

ribeiroFamily.delete_member(1)
     

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
