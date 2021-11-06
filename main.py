import json
import requests
from flask import Flask, request
from app.blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({
        "length": len(chain_data),
        "chain": chain_data
    })

@app.route('/mine', methods=['GET'])
def mine():
    index = blockchain.mine()
    return json.dumps({
        "index": index
    })

app.run(debug=True, port=5000)
