import sys


class Node:
    def __init__(self):
        # each node can have |order - 1| keys
        self.keys = [] # K

        # |order| / 2 <= # of subTree pointers <= |order|
        self.subTrees = [] # P

        self.parent = None
        self.isLeaf = False

        # leaf node has next node pointer
        self.nextNode = None
        self.values = []


class B_PLUS_TREE:
    def __init__(self, order):
        self.order = order
        self.nodeRoot = Node()
        self.nodeRoot.isLeaf = True
        pass

    def insert(self, k):
        # leaf node까지 search
        nodeCurrent = self.nodeRoot
        while not nodeCurrent.isLeaf:
            nodeCurrent = nodeCurrent.subTrees[-1]
            keysLen = len(nodeCurrent.keys)
            for index in range(0, keysLen):
                if k < nodeCurrent.keys[index]:
                    nodeCurrent = nodeCurrent.subTrees[index]
                    break

        # leaf node에서 insert 및 split
        # Insert Case 1
        nodeCurrent.keys.append(k)
        nodeCurrent.keys.sort()
        nodeCurrent.values.append(k)
        nodeCurrent.values.sort()

        if len(nodeCurrent.values) == self.order:
            if len(nodeCurrent.parent) == self.order: # Case 2
                while 1:
                    if nodeCurrent == self.nodeRoot:
                        # Create new root
                        nodeRootNew = Node()
                        nodeRootNew.subTrees.append(nodeCurrent)
                        nodeCurrent.parent = nodeRootNew
                        self.nodeRoot = nodeRootNew

                    # Split
                    nodeRight = Node()
                    nodeRight.parent = nodeCurrent.parent
                    nodeRight.isLeaf = True
                    nodeRight.keys = nodeCurrent.values[self.order / 2:]
                    nodeRight.values = nodeCurrent.values[self.order / 2:]
                    del nodeCurrent.values[self.order / 2:]
                    nodeRight.nextNode = nodeCurrent.nextNode

                    nodeCurrent.nextNode = nodeRight

                    # Propagate
                    MedianValue = nodeRight.values[0]
                    nodeCurrent.parent.keys.append(MedianValue)
                    nodeCurrent.parent.keys.sort()

                    MedianIndex = nodeCurrent.parent.keys.index(MedianValue)
                    nodeCurrent.parent.subTrees.insert(MedianIndex + 1, nodeRight)

                    if not len(nodeCurrent.parent) == self.order: # Case 3
                        break
        pass

    def delete(self, k):
        pass

    def print_root(self):
        l = "["
        for k in self.nodeRoot.keys:
            l += "{},".format(k)
        l = l[:-1] + "]"
        print(l)
        pass

    def print_tree(self):
        pass

    def find_range(self, k_from, k_to):
        pass

    def find(self, k):
        pass


def main():
    myTree = None

    while (True):
        comm = sys.stdin.readline()
        comm = comm.replace("\n", "")
        params = comm.split()
        if len(params) < 1:
            continue

        print(comm)

        if params[0] == "INIT":
            order = int(params[1])
            myTree = B_PLUS_TREE(order)

        elif params[0] == "EXIT":
            return

        elif params[0] == "INSERT":
            k = int(params[1])
            myTree.insert(k)

        elif params[0] == "DELETE":
            k = int(params[1])
            myTree.delete(k)

        elif params[0] == "ROOT":
            myTree.print_root()

        elif params[0] == "PRINT":
            myTree.print_tree()

        elif params[0] == "FIND":
            k = int(params[1])
            myTree.find(k)

        elif params[0] == "RANGE":
            k_from = int(params[1])
            k_to = int(params[2])
            myTree.find_range(k_from, k_to)

        elif params[0] == "SEP":
            print("-------------------------")

if __name__ == "__main__":
    main()