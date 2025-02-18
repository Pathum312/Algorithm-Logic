class Node:
    """
    A class representing a node in a binary search tree

    Attributes:
        key (int): The key of the node.
        left (Node | None): The left child of the node.
        right (Node | None): The right child of the node.
        parent (Node | None): The parent of the node.
    """

    def __init__(self, key: int) -> None:
        """
        Initialize the node with the given key

        Parameters:
            key (int): The key of the node.

        Returns:
            None
        """
        self.key: int = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class BST:
    """
    A class representing a binary search tree

    Attributes:
        root (Node): The root node of the tree.
    """

    def __init__(self, key: int) -> None:
        """
        Initialize a root node with the given key

        Parameters:
            key (int): The key of the root node.

        Returns:
            None
        """
        self.root: Node = Node(key=key)

    def insert(self, key: int) -> None:
        """
        Insert a new node with the given key into the tree

        Parameters:
            key (int): The key of the new node.

        Returns:
            None
        """
        node: Node = self.root

        while True:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key=key)
                    node.left.parent = node
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(key=key)
                    node.right.parent = node
                    break
                node = node.right

    def search(self, node: Node | None, key: int) -> Node | None:
        """
        Search for a node with the given key in the tree

        Parameters:
            node (Node): The node to start the search from.
            key (int): The key to search for.

        Returns:
            Node: The node with the given key if found, otherwise None
        """
        if node is None or node.key == key:
            return node  # type: ignore

        if node.key > key:
            return self.search(node=node.left, key=key)
        else:
            return self.search(node=node.right, key=key)

    def remove(self, key: int) -> None:
        """
        Remove a node with the given key from the tree

        Parameters:
            key (int): The key of the node to remove.

        Returns:
            None
        """
        found_node: Node | None = self.search(node=self.root, key=key)

        if found_node is None:
            print(f"\n{key} not found in the tree.")
            return

        if found_node.left and found_node.right:
            self._remove_two_children(node=found_node)
        elif found_node.left or found_node.right:
            self._remove_one_child(node=found_node)
        else:
            self._remove_leaf(node=found_node)

    def _remove_leaf(self, node: Node) -> None:
        """
        Remove a leaf node from the tree

        Parameters:
            node (Node): The node to remove.

        Returns:
            None
        """
        parent: Node = node.parent  # type: ignore
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    def _remove_one_child(self, node: Node) -> None:
        """
        Remove a node with one child from the tree

        Parameters:
            node (Node): The node to remove.

        Returns:
            None
        """
        parent: Node = node.parent  # type: ignore
        child: Node = node.left if node.left else node.right  # type: ignore

        if parent:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child

            child.parent = parent
        else:
            self.root = child
            self.root.parent = None

    def _remove_two_children(self, node: Node) -> None:
        """
        Remove a node with two children from the tree

        Parameters:
            node (Node): The node to remove.

        Returns:
            None
        """
        parent: Node = node.parent  # type: ignore
        successor: Node = self._get_successor(node=node if parent else node.right)  # type: ignore
        successor_parent: Node = successor.parent  # type: ignore

        node.key = successor.key

        if successor_parent.left == successor:
            successor_parent.left = successor.right
        elif successor_parent.right == successor:
            successor_parent.right = successor.right

        if successor.right:
            successor.right.parent = successor_parent

    def _get_successor(self, node: Node) -> Node | None:
        """
        Get the successor node for the node being removed

        Parameters:
            node (Node): The node to get the successor of.

        Returns:
            Node: The successor node
        """
        current: Node = node
        while current.left:
            current = current.left
        return current

    def visualize(
        self,
        node: Node | None,
        level: int = 0,
        prefix: str = "\nL - Left child node\nR - Right child node\n\nRoot--- ",
    ) -> None:
        """
        Visualizes the BST tree.

        Attributes:
            node (Node): Always pass the root node.
            level (int): Default is 0.
            prefix (str): Is set to Root.

        Returns:
            None
        """
        if node:
            print(" " * (level * 4) + prefix + str(object=node.key))
            self.visualize(node=node.left, level=level + 1, prefix="L--- ")
            self.visualize(node=node.right, level=level + 1, prefix="R--- ")


if __name__ == "__main__":
    # Create a binary search tree
    tree: BST = BST(key=20)
    # Insert keys into the tree
    tree.insert(key=10)
    tree.insert(key=30)
    tree.insert(key=9)
    tree.insert(key=15)
    tree.insert(key=25)
    tree.insert(key=35)

    # Visualize the tree
    print("\nInitial")
    tree.visualize(node=tree.root)

    print("\nFound 30" if tree.search(node=tree.root, key=30) else "\n30 not found")
    print("\nFound 28" if tree.search(node=tree.root, key=28) else "\n28 not found")

    tree.remove(key=25)

    print("\nRemove 25")
    tree.visualize(node=tree.root)

    tree.remove(key=30)

    print("\nRemove 30")
    tree.visualize(node=tree.root)

    tree.remove(key=20)

    print("\nRemove 20")
    tree.visualize(node=tree.root)
