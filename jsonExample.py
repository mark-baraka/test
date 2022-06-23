#how to use jsonify for dictionary objects
from flask import jsonify
@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'Kenya'})
    