class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, ele):
        if root is None:
            root = Node(ele)
        else:
            if ele <= root.data:
                if root.left is None:
                    root.left = Node(ele)
                else:
                    self.insert(root.left, ele)
            else:
                if root.right is None:
                    root.right = Node(ele)
                else:
                    self.insert(root.right, ele)

    def buildbst(self, arr):
        self.root = Node(arr[0])
        for i in arr[1:]:
            self.insert(self.root, i)
        return self.root

    def maxdepth(self, root):
        if root is None:
            return 0
        else:
            lf = self.maxdepth(root.left)
            rt = self.maxdepth(root.right)

            if(lf > rt):
                return lf+1
            else:
                return rt + 1


            
            

    def inoder(self, root):
        if root:
            self.inoder(root.left)
            print(root.data)
            self.inoder(root.right)

    

arr = [30, 20, 40, 70, 60, 80]
root = Tree().buildbst(arr)
Tree().inoder(root)
print(Tree().maxdepth(root))