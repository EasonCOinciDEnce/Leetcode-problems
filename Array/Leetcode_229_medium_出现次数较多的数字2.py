'''
Given an integer array of size n, find all elements that appear more than ? n/3 ? times. The algorithm should run in linear time and in O(1) space.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#ţ�ķ���
#�����ҵķ�����ʱ���ﲻ��
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ctr=collections.Counter()
        for n in nums:
            ctr[n]+=1
            if len(ctr)==3:
                ctr-=collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n)>len(nums)/3]


slu=Solution()
t=slu.majorityElement([1,1,1,2,3,3,4,5])
print t




#�ο���
#https://leetcode.com/problems/majority-element-ii/#/description