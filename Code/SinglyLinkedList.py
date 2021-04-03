class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, arr = None):
        self.head = None

        if arr:
            for i in arr:
                self.append(i)

    def __str__(self):
        return str(self.all())

    def __getitem__(self, pos):
        cur_node = self.head

        for i in range(pos):
            if i == pos:
                break

            cur_node = cur_node.next
            if not cur_node:
                raise Exception("Index out of range")
                return

        return cur_node.data
            

    def __setitem__(self, pos, data):
        cur_node = self.head

        for i in range(pos):
            if i == pos:
                break

            cur_node = cur_node.next
            if not cur_node.next:
                self.append(data)
                return

        cur_node.data = data

    def __call__(self, key):
        cur_node = self.head
        index = 0
        while cur_node:
            if cur_node.data == key:
                return index

            cur_node = cur_node.next
            index += 1

        raise Exception("There's no {} in the list".format(key))

    def __len__(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def __add__(self, data):
        if isinstance(data, LinkedList):
            data = data.all()

        for i in data:
            self.append(i)

        return self

    def __sub__(self, data):
        if isinstance(data, LinkedList):
            data = data.all()

        for i in data:
            self.delete(i)

        return self

    def all(self):
        data = []

        cur_node = self.head
        while cur_node:
            data.append(cur_node.data)
            cur_node = cur_node.next

        return data
                
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, pos, data):
        if not type(pos) is int:
            raise Exception("Position must be an integer")
            return

        new_node = Node(data)
        cur_node = self.head

        if pos == 0:
            new_node.next = cur_node
            self.head = new_node
            return

        prev = None

        for i in range(pos):
            if i == pos:
                break

            prev = cur_node
            cur_node = cur_node.next

            if cur_node is None:
                break

        new_node.next = cur_node
        prev.next = new_node

    def delete(self, key):
        cur_node = self.head
        prev = None

        if cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            raise Exception("Key didn't exist")
            return

        prev.next = cur_node.next
        cur_node = None

    def deleteAt(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                raise Exception("Index out of range")
                return

            prev.next = cur_node.next
            cur_node = None

    def swap(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        curr1.data, curr2.data = curr2.data, curr1.data

    def reverse(self):
        def _reverse(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse(cur, prev)

        self.head = _reverse(cur = self.head, prev = None)

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur

            cur = prev.next

        return self

    def nth_from_last(self, n):
        total_len = self.__len__()

        cur = self.head
        while cur:
            if total_len == n:
                return cur.data

            total_len -= 1
            cur = cur.next

        if cur is None:
            return

    def count_occurences(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1

            cur = cur.next

        return count

    def rotate(self, k):
        if self.head and self.head.next:
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

        return self

    def is_palindrome(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next

        return s == s[::-1]