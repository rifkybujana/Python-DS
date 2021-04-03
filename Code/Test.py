from SinglyLinkedList import LinkedList

linked_list1 = LinkedList(["A", "A", "B", "A", "D"])
linked_list2 = LinkedList(["B", "C"])

print("1: {}".format(linked_list1))
print("2: {}".format(linked_list2))

print("")

print(linked_list1 + linked_list2)
print(linked_list1.count_occurences("A"))
print(linked_list1.remove_duplicates())
print(linked_list1.rotate(1))
print(linked_list1 - ["A", "B"])