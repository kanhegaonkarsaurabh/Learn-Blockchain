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
}

module.exports = Block;