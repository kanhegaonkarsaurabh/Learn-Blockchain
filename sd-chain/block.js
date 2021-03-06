const SHA256 = require('crypto-js/sha256');

// Create the initial block class
class Block {
  constructor(timestamp, lastHash, hash, data) {         // Construct the block
    this.timestamp = timestamp;
    this.lastHash = lastHash;
    this.hash = hash;
    this.data = data;    
  }

  toString() {        // Debugging purposes
    return `Block -- 
      Timestamp: ${this.timestamp}
      Lasthash: ${this.lastHash.substring(0,10)}
      Hash: ${this.hash.substring(0,10)}
      Data: ${this.data} `
  }

  // Genesis Block: The first block in every blockchain that starts the chain is called as genesis block
  static genesis() {
    // Syntax: Return an object of the same class this function is declared
    return new this('Genesis Time', '-----', 'f1r57 h45h', []);
  }

  static mineBlock(lastBlock, data) {
    let timestamp = Date.now();
    let lastHash = lastBlock.hash;
    let hash = SHA256(`${timestamp}${lastHash}${data}`).toString();       // The hash of a particular block
    let givenData = data;

    return new this(timestamp, lastHash, hash, givenData);
  }

  static hashC(block) {
    return SHA256(`${block.timestamp}${block.lastHash}${block.data}`).toString();  
  }

}

module.exports = Block;