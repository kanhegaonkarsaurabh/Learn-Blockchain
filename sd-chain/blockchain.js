const Block = require('./block');

class Blockchain {
  constructor() {                 // At the core our chain would be an array of blocks
    this.chain = [];
    this.chain.push(Block.genesis());     // Genesis block is the 1st block in a chain always. 
  }

  addBlock(data) {
    const lastBlock = this.chain[this.chain.length - 1];      // New block is based off of hash values of previous one.
    const block = Block.mineBlock(lastBlock, data);       // this is what takes agess on the big chains like Bitcoin
    
    this.chain.push(block);

    return block;
  }

  isValidChain(chain) {
    // First check: first block is always genesis block
    if (JSON.stringify(chain[0]) !== JSON.stringify(Block.genesis())) {
      return false;  
    }

    // Loop through the whole block and check for hashes
    for (let i = 0;i < chain.length; i++) {
      const block = chain[i];
      const lastBlock = chain[i-1];

      if (block.lastHash !== lastBlock.hash) {
        return false;
      }
    
      if (block.hash !== Block.hashC(block)) {
        return false;
      }  
    }

    return true;
  }
}

module.exports = Blockchain;