import json
from flask import Flask, jsonify
from scrape import main
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify(main())


app.run()