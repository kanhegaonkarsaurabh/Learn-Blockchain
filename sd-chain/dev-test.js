const Block = require('./block')      // Import in the block class


let block = new Block('00:11:22', '0x432423132', '0x44212431', [{
  'transactions': []
}])


console.log(block.toString())