class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates_from_linked_list(linked_list):
    node = linked_list
    while node.next is not None:
        if node.value is not node.next.value:
            print(node.value)
            node = node.next
        else:
            node.next = node.next.next
    return linked_list
