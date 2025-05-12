import hashlib

class Block():
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hashlib.sha256()
        self.nonce = 0

    def mine(self, difficulty):
        self.hash.update(str(self).encode("utf-8"))
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode("utf-8"))
        

    def __str__(self):
        return f"{self.previous_hash.hexdigest()}{self.data}{self.nonce}"

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []
        self.create_origin_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode("utf-8"))
        return (
            block.hash.hexdigest() == hash.hexdigest()
            and int(hash.hexdigest(), 16) < 2**(256-self.difficulty)
            and block.previous_hash == self.blocks[-1].hash
        )

    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self, data):
        self.pool.append(data)

    def create_origin_block(self):
        hash = hashlib.sha256()
        hash.update("".encode("utf-8"))
        origin = Block("Origin", hash)
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def mine(self) -> str:
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.add_to_chain(block)
            print("**************START*****************")
            print("Hash: " + block.hash.hexdigest())
            print("Previous Hash: " + block.previous_hash.hexdigest())
            print("Nonce:\t\t", block.nonce)
            print("Data:\t\t", block.data)
            print("****************END***************")
            print("")
            return block.hash.hexdigest()
        else:
            return ""