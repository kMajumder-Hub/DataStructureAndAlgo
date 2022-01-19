import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8') + str(self.timestamp).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return f"Data: {self.data} \nTimestamp: {self.timestamp} \nHash: {self.hash}"




class BlockChain:
    def __init__(self):
        self.tail = None

    def append(self,data):
        """Append an element to the blockchain"""

        if self.tail is None:
            self.tail = Block(self.get_utc_time(), data)
        else:
            self.tail = Block(self.get_utc_time(), data, self.tail)
        
    def get_utc_time(self):
        """Get the UTC timestamp"""
        return datetime.datetime.utcnow()

    def size(self):
        """Return the size of the blockchain"""
        size = 0
        node = self.tail
        while node:
            node = node.previous_hash
            size += 1

        return size
    
    def to_list(self):
        """Transforms the BlockChain content into a list"""
        l = []
        block = self.tail
        while block:
            l.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return l
    
    def search(self, data):
        """Search element within blockchain"""

        if self.tail is None:
            return "Blockchain is empty"
        else:
            node = self.tail

            while(node):
                if node.data == data:
                    return node
                node = node.previous_hash
            return "Data not present"


#Test Preparation
blockchain = BlockChain()

blockchain.append('India')
blockchain.append('United States Of America')
blockchain.append('Canada')

#Test Case 1
print(blockchain.size())  # should return 3

#Test Case 2
print(blockchain.to_list())

#[['Canada', datetime.datetime(2022, 1, 13, 7, 22, 31, 292923), '50f5df1c1dbc6082015b1e7ebcb3e60394a162f54ba06da74c3376fc25328608'], 
#['United States Of America', datetime.datetime(2022, 1, 13, 7, 22, 31, 292923), '9aff7dbb2a2c37be62e33ecea18939723ceb22daff07dfd69a75ee3248787255'], 
#['India', datetime.datetime(2022, 1, 13, 7, 22, 31, 292923), 'f2840de6c50bad5409a718ff58458530451e065335dde2e8b6f4133d6ff2fccf']]

#Test Case 3
print(blockchain.search('India'))

# Data: India 
# Timestamp: 2022-01-13 07:22:31.292923 
# Hash: f2840de6c50bad5409a718ff58458530451e065335dde2e8b6f4133d6ff2fccf

# Test Case 4 (Edge Case)
print(blockchain.search('XYZ')) # Data not present

# Test Case 5 (Edge Case)
blockchain2 = BlockChain()
print(blockchain2.size())    # should return 0
print(blockchain2.to_list()) # []