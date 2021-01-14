# There are singly linked lists, doubly linked lists, and circular linked lists

# All linked list consists of nodes which have ...
#   - Data, storing an element of data such as string or number
#   - Next, pointer that points from one node to another
# Head refers to the start of the linked list (pointer that points to beginning of list)
# None refers to the null object that the last node in singly linked list points to

#                           Array       Linked List
# Insertion/Deletion        O(n)        O(1)
# (at the beginning)
# Accessing an element      O(1)        O(n)
# Contiguous memory         Yes         No

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Add at the end of the list
    def append(self, data):
        new_node = Node(data)
        # Empty Linked List
        if self.head is None:
            self.head = new_node
            return
        # Non-empty Linked List
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # Add at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Add at a certain position of the list
    def insert_after_node(self, prev_node, data):
        if not prev_node: 
            print("Previous node does not exist")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete when node data matches value
    def delete_node(self, key):
        cur_node = self.head
        
        # Delete if the value is at the head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        # Delete if the value is not at the head
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Delete at a certain position of the list
    def delete_node_at_pos(self, pos):
        # Check if list empty or not
        if self.head:
            cur_node = self.head
            # Delete if position 0
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            
            # Delete if position not 0
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    # Length count by iterative approach
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
        
    # Length count by recursive approach
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # Swap two nodes
    def swap_nodes(self, key_1, key_2):
        # Node 1 and Node 2 are not head nodes
        # Either Node 1 or Node 2 is a head node

        if key_1 == key_2: 
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return
        
        if prev_1: 
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    # Reverse list by iterative approach
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # Reverse list by recursive approach
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    # Merge two sorted linked lists
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        # If one linked list is empty, return the either
        if not p:
            return q
        if not q:
            return p

        # Choose the first node
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        # new_head keeps the beginning of s linked list
        # while s moves down and accumulates through p and q
        new_head = s

        # Choose the next nodes
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q: 
            s.next = p
        return new_head

    # Remove duplicates from the linked list
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            # Remove node if element is there
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            # Add element if not encountered 
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    # Method 1 of getting the nth node from the last
    def print_nth_from_last_1(self, n):
        total_len = self.len_iterative()
        
        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return
    
    # Method 2 of getting the nth node from the last
    def print_nth_from_last_2(self, n):
        p = self.head
        q = self.head

        count = 0
        while q:
            count += 1
            if (count >= n):
                break
            q = q.next

        if not q:
            print(str(n) + " is greater than the number of nodes in the list.")
            return
        
        while p and q.next:
            p = p.next
            q = q.next

        return p.data 

    # Count occurrences of a value by iterative approach
    def count_occurrences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    # Count occurrences of a value by recursive approach
    # Must have self as it is a class method
    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)

    # Rotate the nodes by a pivot
    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None
        
    # Method 1 of checking palindrome by using a string
    def is_palindrome_1(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        # s[::-1] is shorthand for reversing a string
        return s == s[::-1]

    # Method 2 of checking palindrome by using a stack
    def is_palindrome_2(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if data != p.data:
                return False
            p = p.next
        return True
    
    # Method 3 of checking palindrome by using two pointers
    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q: 
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i - 1]

            count = 1

            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True
    
    # Move the tail as the head
    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last

    # Add two lists together
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        i = 0
        j = 0

        while p or q:
            if not p:
                i = 0
            else: 
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                s -= 10
                carry = 1
                sum_llist.append(s)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist
