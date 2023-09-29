#!/usr/bin/python3
"""Blueprints"""
from flask import jsonify

from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Returns status of the API"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats():
    """Returns the number of objects"""
    stats = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
            }
    return jsonify(stats)
