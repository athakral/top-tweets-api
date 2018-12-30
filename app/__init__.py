from flask import Flask, jsonify, make_response
from twitterclient import client

app = Flask(__name__)


@app.route('/twitter/api/v1.0/tweets/<query>', methods=['GET'])
def get_tasks(query):
    return client.search(query, client.login())



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def app_error(error):
    return make_response(jsonify({'error': 'Error while getting data from twitter, please check your parameter'}), 500)


