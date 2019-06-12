from flask import Flask, jsonify, request, redirect, render_template
import json
from flask_paginate import Pagination

with open('/home/administrator/Desktop/flask_ex/data_for_rest.json', 'r'
          ) as f:
    data = f.read()

json_formatted_data = json.loads(data)

length = len(json_formatted_data['people'])


@app.route('/')
def index():
    return jsonify(json_formatted_data)

@app.route('/search', methods=['GET'])
def search():
    emailid = request.args.get('email')

    for i in range(0, length):
        if emailid in json_formatted_data['people'][i]['email']:
            return jsonify(json_formatted_data['people'][i])

    return jsonify('Not Found')



if __name__ == '__main__':
    app.run(debug=True)
