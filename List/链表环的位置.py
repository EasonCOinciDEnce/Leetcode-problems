'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):#���ַ�����յģ����Ա�����ֳ����Ҳ�����һ��λ�õ����
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=head
        while True:
            if fast==None:
                return None
            elif fast.next==None:
                return None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

	

