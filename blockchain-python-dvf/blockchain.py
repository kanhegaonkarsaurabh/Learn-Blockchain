import hashlib
import json
from time import time
from uuid import uuid4

# API framework for the blockchain
from flask import Flask

# The initial class that'll contain the blockchain
class Blockchain(self):
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    
    # Instantiate the initial block - the first block of the chain,
    # called the genesis block
    self.new_block(previous_hash=1, proof=100)

  def new_block(self, proof, previous_hash=None):
    # Add a new block to the blockchain

    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof, 
      'previous_hash': previous_hash or self.hash(self.chain[-1])  
    }

    # Resets the current transactions as the current ones are on a new block now.
    self.current_transactions = []
    
    # Attach the block to the chain
    self.chain.append(block)
    return block
    
  def new_transaction(self, sender, recipient, amount): 
    """ 
    Adds a new transaction to the PREVIOUSLY MINED block 
    :param sender: <str> Address of the sender
    :param recipient: <str> Address of the recipient 
    :param amount: <int> Amount sent in on the transaction
    return : <int> Index of the Block that will hold the transaction
    """
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount,
    })      

    return self.last_block['index'] + 1
    
  @staticmethod
  def hash(block):
    # Hashes a whole block. Use SHA-256 over here.
    
    # We need ordered blocks or else it creates inconsistent hashes
    block_strings = json.dumps(block, sort_keys=True).encode()
    
    return hashlib.sha256(block_string).hexdigest()
     
  @property
  def last_block(self):
    # Returns the last block in the chain
    return self.chain[-1]

  def proof_of_work(self, last_proof):
    proof = 0
    
    while self.valid_proof(last_proof, proof) is False:
      proof += 1
    
    return proof
  
  def valid_proof(last_proof, proof):
    """
      Validates the given Hash to be valid for transaction and approve the Proof-Of-Work
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


# Declare our API webapp
app = Flask(__name__)

# A unique identifier for each of our Nodes
node_identifier = str(uuid4()).replace('-','')

# Instantiate the Blockchain
blockchain = Blockchain()
      
@app.route('/mine', methods=['GET'])
def mine():
  return "We'll mine a new block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  return "New transaction on the block"
  
@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.length),
  }
  return jsonify(response), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)



