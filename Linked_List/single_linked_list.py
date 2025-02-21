class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node | None = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.last: Node | None = None

    def add(self, data: int) -> None:
        new_node: Node = Node(data=data)

        if self.head is not None:
            self.last.next = new_node  # type: ignore
            self.last = new_node
        else:
            self.head = new_node
            self.last = new_node

    def traversal(self) -> None:
        node: Node | None = self.head

        while node is not None:
            print(node.data, end=" ")

            node = node.next

        print("\n")

    def search(self, data: int) -> bool:
        node: Node | None = self.head

        while node is not None:
            if node.data == data:
                return True

            node = node.next

        return False

    @property
    def length(self) -> int:
        count: int = 0
        node: Node | None = self.head

        while node is not None:
            count += 1

            node = node.next

        return count


if __name__ == "__main__":
    # Initialize the linked list
    linked_list: SingleLinkedList = SingleLinkedList()

    # Add nodes to the linked list
    linked_list.add(data=1)
    linked_list.add(data=2)
    linked_list.add(data=3)
    linked_list.add(data=4)
    linked_list.add(data=5)

    # Print the elements in linked list
    linked_list.traversal()

    # Find a element in a linked list
    print("Found 4.\n" if linked_list.search(data=4) else "Did not find 4.\n")

    print("Found 13.\n" if linked_list.search(data=13) else "Did not find 13.\n")

    print(f"Length: {linked_list.length}\n")
