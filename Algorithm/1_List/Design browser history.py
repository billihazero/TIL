
# 앞과 뒤로 이동하는 선형구조 = linked list 중 doubly linked list를 이용해야한다.

class ListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)
    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None
    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            steps -=1
            self.current = self.current.prev
        return self.current.val
    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -=1
            self.current = self.current.next
        return self.current.val
