from linked_list import LinkedList

list = LinkedList(head=None)

list.insert_first(key=1, data=10)
list.insert_first(key=2, data=20)
list.insert_first(key=4, data=40)
list.insert_first(key=6, data=60)
list.print_list()
list.insert_after(after_key=1, key=3, data=30)
list.print_list()
list.insert_before(before_key=6, key=5, data=50)
list.print_list()
print list.size()
list.reverse()
list.print_list()
