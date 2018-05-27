const Block = require('./block')      // Import in the block class


const block1 = Block.mineBlock(Block.genesis(), [{
  'transactions': [],
}]);

console.log(block1.toString())