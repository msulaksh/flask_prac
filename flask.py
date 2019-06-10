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
