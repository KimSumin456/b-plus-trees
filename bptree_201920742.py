import sys
from collections import deque


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
        # Insert
        nodeCurrent.keys.append(k) # Case 1
        nodeCurrent.keys.sort()
        nodeCurrent.values.append(k)
        nodeCurrent.values.sort()

        if len(nodeCurrent.keys) == self.order: # Case 2, 3
            while 1:
                print("=====while")
                if nodeCurrent == self.nodeRoot:
                    print("=====if nodeRoot")
                    # Create new root
                    nodeRootNew = Node()
                    nodeRootNew.subTrees.append(nodeCurrent)
                    nodeCurrent.parent = nodeRootNew
                    self.nodeRoot = nodeRootNew
                print("=====nodeCurrent", nodeCurrent.keys)

                # Split
                nodeRight = Node()
                nodeRight.parent = nodeCurrent.parent
                nodeRight.isLeaf = nodeCurrent.isLeaf
                nodeRight.keys = nodeCurrent.keys[int(self.order / 2):]
                nodeRight.values = nodeCurrent.keys[int(self.order / 2):]
                del nodeCurrent.keys[int(self.order / 2):]
                del nodeCurrent.values[int(self.order / 2):]
                nodeRight.nextNode = nodeCurrent.nextNode

                nodeCurrent.nextNode = nodeRight
                print("=====nodeRight", nodeRight.values)

                # Propagate
                MedianKeys = nodeRight.keys[0]
                nodeCurrent.parent.keys.append(MedianKeys)
                nodeCurrent.parent.keys.sort()
                nodeCurrent.parent.values.append(MedianKeys)
                nodeCurrent.parent.values.sort()

                MedianIndex = nodeCurrent.parent.keys.index(MedianKeys)
                nodeCurrent.parent.subTrees.insert(MedianIndex + 1, nodeRight)

                if not nodeRight.isLeaf:
                    nodeRight.subTrees = nodeCurrent.subTrees[int(self.order / 2 + 1):]
                    del nodeCurrent.subTrees[int(self.order / 2 + 1):]

                    for subTree in nodeRight.subTrees:
                        subTree.parent = nodeRight

                    del nodeRight.keys[0]

                if len(nodeCurrent.parent.keys) == self.order:
                    nodeCurrent = nodeCurrent.parent
                else:
                    break

    def delete(self, k):
        pass

    def print_root(self):
        l = "["
        for k in self.nodeRoot.keys:
            l += "{},".format(k)
        l = l[:-1] + "]"
        print(l)

    def print_tree(self):
        q = deque([self.nodeRoot]) # 그래프 아니고 트리라 visited 필요 없을 듯

        while q:
            nodeCurrent = q.popleft()
            l = "["
            for k in nodeCurrent.keys:
                l += "{},".format(k)
            l = l[:-1] + "]-"
            print(l, end='')

            for subTree in nodeCurrent.subTrees:
                l = "["
                for k in subTree.keys:
                    l += "{},".format(k)
                l = l[:-1] + "],"
                print(l, end='')
                if not subTree.isLeaf:
                    q.append(subTree)
            print("\b")


    def find_range(self, k_from, k_to):
        pass

    def find(self, k):
        # leaf node까지 search
        nodeCurrent = self.nodeRoot
        while not nodeCurrent.isLeaf:
            nodeCurrent = nodeCurrent.subTrees[-1]
            keysLen = len(nodeCurrent.keys)
            for index in range(0, keysLen):
                if k < nodeCurrent.keys[index]:
                    nodeCurrent = nodeCurrent.subTrees[index]
                    break






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