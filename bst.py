class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def mirror(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)

def main():
    tree = BST()
    root = None
    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            val = int(input("Enter value: "))
            root = tree.insert(root, val)
        elif ch == 2:
            val = int(input("Enter value to delete: "))
            root = tree.delete(root, val)
        elif ch == 3:
            val = int(input("Enter value to search: "))
            print("Found!" if tree.search(root, val) else "Not Found!")
        elif ch == 4:
            print("Inorder Traversal: ", end="")
            tree.inorder(root)
            print()
        elif ch == 5:
            print("Tree Depth:", tree.depth(root))
        elif ch == 6:
            tree.mirror(root)
            print("Tree mirrored.")
        else:
            break

if __name__ == "__main__":
    main()
