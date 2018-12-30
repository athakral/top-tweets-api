from flask import Flask, jsonify, make_response
from twitterclient import client

app = Flask(__name__)


@app.route('/twitter/api/v1.0/tweets/<query>', methods=['GET'])
def get_tasks(query):
    # make response, since we have to set the mimetype correctly
    resp = make_response(client.search(query,client.login()))
    # set the correct mimetype
    resp.mimetype = 'application/json';
    return resp



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def app_error(error):
    return make_response(jsonify({'error': 'Error while getting data from twitter, please check your parameter'}), 500)


