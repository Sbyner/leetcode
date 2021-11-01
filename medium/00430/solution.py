class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            self.flat(head)
        return head
    
    def flat(self, head: 'Node') -> 'Node':
        def last(head: 'Node') -> 'Node':
            if head:
                if head.next:
                    return last(head.next)
                else:
                    return head
        
        #print(last(head).val)

        if not head.child:
            if head.next:
                self.flat(head.next)
        else:
            if head.next:
                nx = head.next
                self.flat(head.child)
                head.next = head.child
                head.next.prev = head
                head.child = None
                ls = last(head.next)
                nx.prev = ls
                ls.next = nx
            else:
                head.next = head.child
                self.flat(head.child)
                head.next.prev = head
                head.child = None


