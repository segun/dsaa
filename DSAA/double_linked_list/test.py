from linked_list import LinkedList

list = LinkedList(head=None)

list.insert_last(key=2, data=20)
list.insert_last(key=3, data=30)
list.insert_first(key=1, data=10)
list.insert_first(key=0, data=0)
list.insert_last(key=9, data=90)
list.print_forward()
list.print_backward()
list.delete_first()
list.print_forward()
list.print_backward()
list.delete_last()
list.print_backward()
list.print_forward()
list.delete(key=2)
list.print_forward()
list.print_backward()
list.delete(key=3)
list.print_forward()
list.print_backward()
list.insert_last(key=2, data=20)
list.insert_last(key=5, data=50)
list.insert_after(after_key=2, key=3, data=30)
list.print_forward()
list.print_backward()
list.insert_after(after_key=5, key=7, data=70)
list.print_forward()
list.print_backward()
list.insert_before(before_key=1, key=0, data=0)
list.print_forward()
list.print_backward()
list.insert_before(before_key=7, key=6, data=60)
list.print_forward()
list.print_backward()
