# Doubly linked list is a singly linked list with a reference to a previous pointer

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            # If the next of the node to be added is null
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            # Any other cases
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            # If the prev of the node to be added is null
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            # Any other cases
            elif cur.data == key:
                new_node = Node(data)
                prv = cur.prev 
                prv.next = new_node
                new_node.prev = prv
                new_node.next = cur
                cur.prev = new_node
                return
            cur = cur.next

            cur = cur.next

    def delete_node(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1: delete only one node present
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                
                # Case 2: delete head node with other nodes present
                else: 
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # Case 3: delete non-head node where its next node is not None
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                
                # Case 4: delete non-head node where its next node is None
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next
    # Pointers of the node that is to be deleted also must be negated as well
    # cur.next = None -> cur.prev = None -> cur = None

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
    # Reversing once based on what is connected to the node (switch where prev and next points to of that node)
    # cur = cur.prev is done since the pointers of prev and next are switched

    def remove_duplicates(self):
        cur = self.head 
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
    # the next node to be deleted must be saved since the reference to that node is also deleted

    # Find pairs that add up to sum_val
    def pairs_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs

        

            
