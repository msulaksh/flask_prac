from flask import Flask, jsonify, request, redirect, render_template
import json
from flask_paginate import Pagination

with open('/home/administrator/Desktop/flask_ex/data_for_rest.json', 'r'
          ) as f:
    data = f.read()

json_formatted_data = json.loads(data)

length = len(json_formatted_data['people'])

##Index page showing full data 

@app.route('/')
def index():
    return jsonify(json_formatted_data)

##Search using email as a argument

@app.route('/search', methods=['GET'])
def search():
    emailid = request.args.get('email')

    for i in range(0, length):
        if emailid in json_formatted_data['people'][i]['email']:
            return jsonify(json_formatted_data['people'][i])

    return jsonify('Not Found')

##Implementing pagination to show limited results.

@app.route('/page/<int:page>', methods=['GET', 'POST'])
def show_users(page):
    try:
        p = []
        i = page * 5 - 5
        while i < page * 5:
            if i >= length:
                p.append(json_formatted_data['people'][i - 1])
            else:
                p.append(json_formatted_data['people'][i])
            i = i + 1
        return jsonify(p)
    except IndexError:
        return jsonify(p)


if __name__ == '__main__':
    app.run(debug=True)
