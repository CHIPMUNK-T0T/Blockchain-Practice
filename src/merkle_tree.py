from hashlib import sha256

class MerkleTree(object):
    def __init__(self):
        pass

    def __generate_pair(self, transaction):
        # トランザクションの中から2個づつ取り出しペアを生成する
        pair_num = 2
        for i in range(0, len(transaction), pair_num):
            if i == len(transaction) - 1:
                transaction.append(transaction[-1])
            yield transaction[i:i+pair_num]

    def merkle_tree(self, transaction):
        # 関数に渡された全てのトランザクションを表現するマークルツリーハッシュを求める
        # トランザクションのリストから2個づつのハッシュ値を算出し、それを繰り返し最終的に1つのハッシュを生成する

        parent_layer = []
        child_layer = transaction

        while True:
            for pair in self.__generate_pair(child_layer):
                hash = sha256(str(pair[0] + pair[1]).encode()).hexdigest()
                parent_layer.append(hash)

            if len(parent_layer) == 1:
                break

            child_layer = parent_layer
            parent_layer = []


if __name__=="__main__":
    transactions = ["a","b","c","d","e","f","g","h","i"]
    merkle_tree =  MerkleTree()
    merkle_tree.merkle_tree(transaction=transactions)