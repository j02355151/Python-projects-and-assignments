
class BinaryTreeArray:
    def __init__(self):
        self.tree = [None] * 111  # Assuming the array size based on the Java code

    def insert(self, value, position, parent_index):
        if position == "root":
            self.tree[parent_index] = value
        elif position == "left":
            left_index = 2 * parent_index + 1
            if left_index < len(self.tree):
                self.tree[left_index] = value
        elif position == "right":
            right_index = 2 * parent_index + 2
            if right_index < len(self.tree):
                self.tree[right_index] = value

    def __str__(self):
        return str([node for node in self.tree if node is not None])


if __name__ == "__main__":
    binary_tree_array = BinaryTreeArray()
    binary_tree_array.insert("/", "root", 0)
    binary_tree_array.insert("*", "left", 0)
    binary_tree_array.insert("+", "right", 0)
    binary_tree_array.insert("4", "right", 1)
    binary_tree_array.insert("+", "left", 1)
    binary_tree_array.insert("2", "right", 2)
    binary_tree_array.insert("-", "left", 2)
    binary_tree_array.insert("1", "right", 3)
    binary_tree_array.insert("3", "left", 3)
    binary_tree_array.insert("5", "right", 5)
    binary_tree_array.insert("9", "left", 5)
    binary_tree_array.insert("@", "root", 110)

    print(binary_tree_array)


