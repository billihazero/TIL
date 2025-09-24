class Node :
    def __init__(self, value=0, next =None):
        self.value = value
        self.next = next

#first = Node(1)
#second = Node(2)
#third = Node(3)
#first.next = second
#second.next = third
#first.value = 6

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         current = self.head
    #         while current.next: # 마지막 node까지 가야하기 때문에(current.next가 none이 될 때까지 ) while을 사용
    #             current = current.next
    #         current.next = new_node
    def append(self, value): # 위의 함수와 다르게 tail을 사용하였고, 이 때 시간복잡도는 O(1)이다.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def insert_at(self, idx, value):
        new_node = Node(value)
        #맨 앞에 노드를 추가하고 싶을때
        #새로운 노드의 다음 노드는 현재 0번째 노드 = self.head 이다.
        #그리고 새로운 노드가 head가 된다.
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next # current를 넣고 싶은 곳 전까지 이동
            new_node.next = current.next
            current.next = new_node
        self.size +=1
    def remove_at(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx -1):
                current = current.next
            current.next = current.next.next
        self.size -= 1






ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert_at(2,9)
