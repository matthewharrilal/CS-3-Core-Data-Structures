#!python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        # return ... and ...
        if self.left is None and self.right is None:
            return True
        return False


    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if self.is_leaf() == True:
            return False
        return True

    def height(self):
        """Return the number of edges on the longest downward path from this
        node to a descendant leaf node"""

        # The reason this works is due to the fact that recursive calls dont remember the past calls until it works
        # its way back up

        if not self.root:
            return 0
        return 1 + max(self.height(self.left), self.height(self.right))


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # TODO: Check if root node has a value and if so calculate its height

        if self.root is None:
            self.size = 0
            return self.size
        else:
            return self.size

    def tree_is_empty(self):
        if self.root is None:
            return True
        return False


    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        if self.tree_is_empty() is True:
            return False
        return self.search(item)
#
    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        # node = self._find_node(item)
        # # TODO: Return the node's data if found, or None
        # return node.data if ... else None

        if self.tree_is_empty() is True:
            return None

        current_node = self.root

        if item == current_node.data:
            return current_node.data

        while current_node is not None:

            if current_node.is_leaf() is True and current_node.data != item:
                return None

            elif item > current_node.data:
                current_node = current_node.right

            elif item < current_node.data:
                current_node = current_node.left

            elif item == current_node.data:
                return current_node.data


    def insert(self, item):

        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        if self.tree_is_empty():
            # If the tree is empty and since we know a binary tree starts with the root node the item that the user
            # wants to insert becomes the root node
            self.root = BinaryTreeNode(item)
            self.size += 1
            return

        parent_node = self._find_parent_node(item)

        if item > parent_node.data:
            parent_node.right = BinaryTreeNode(item)

        elif item < parent_node.data:
            parent_node.left = BinaryTreeNode(item)

        self.size += 1

#
    def _find_parent_node(self, item):

        # Start with the root node and keep track of its parent
        current_node = self.root

        # Checking if the root node is the item the user is looking for or if the tree is empty then we return None
        # before we start iterating
        if current_node.data == item or self.tree_is_empty() is True:
            return None

        parent = None

        # No tree is infinite therefore the very bottom level node will be a leaf
        # at_leaf = False


        # at leaf is false will always be true but we will implement a condition that can bring us out
        while current_node is not None:

            # So if on the first iteration if the current nodes data is equal to the item then we return the parent
            # is the root node but if its not then we continue and the parent node will be eqaul to the one above the
            # the current node
            if current_node.data == item:
                return parent


            # If the current nodes data is less than the item then we set the parent node to the current node and move
            # the current node to the right
            elif item > current_node.data:
                parent = current_node
                current_node = current_node.right

            elif item < current_node.data:
                parent = current_node
                current_node = current_node.left

        return parent

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items



    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        #  Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)


    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Visit this node's data with given function
        ...
        # TODO: Traverse left subtree, if it exists
        ...
        # TODO: Traverse right subtree, if it exists
        ...

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        ...
        # TODO: Traverse right subtree, if it exists
        ...
        # TODO: Visit this node's data with given function
        ...

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = ...
        # TODO: Enqueue given starting node
        ...
        # TODO: Loop until queue is empty
        while ...:
            # TODO: Dequeue node at front of queue
            node = ...
            # TODO: Visit this node's data with given function
            ...
            # TODO: Enqueue this node's left child, if it exists
            ...
            # TODO: Enqueue this node's right child, if it exists
            ...


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
