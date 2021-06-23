class Node:
    def __init__(self,data):
        self.item = data
        self.nref = None
        self.pref = None

class Doublylinkedlist:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        self.list1 = []
        if self.start_node is None:
            print("List has no element")
            return
        n = self.start_node
        while n is not None:
            print(n.item, " ")
            self.list1.append(n.item)
            n = n.nref
    
    def listdata(self):
        return self.list1

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    
    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse(self):
        temp = None
        current = self.start_node
 
        while current is not None:
            temp = current.pref
            current.pref = current.nref
            current.nref = temp
            current = current.pref

        if temp is not None:
            self.start_node = temp.pref

# new_linked_list = Doublylinkedlist()
# new_linked_list.insert_at_start(0)
# new_linked_list.insert_at_end(1)
# new_linked_list.insert_at_end(2)
# new_linked_list.insert_at_end(5)
# new_linked_list.insert_after_item(1,3)
# new_linked_list.insert_before_item(2,4)
# new_linked_list.delete_at_start()
# new_linked_list.delete_at_end()
# new_linked_list.delete_element_by_value(4)
# new_linked_list.traverse_list()
# print(new_linked_list.listdata())
# new_linked_list.reverse()
# new_linked_list.traverse_list()


