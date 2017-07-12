'''
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''


'''
�������������һ��������Ƭ��˵���˾����ҵȲ����У��޶��˵Ȳ����еĳ�������Ϊ3����ô[1,2,3,4]����3����������Ϊ3��������Ƭ������������[1,2,3,4,5]�ж��ٸ���:
len = 3: [1,2,3], [2,3,4], [3,4,5]
len = 4: [1,2,3,4], [2,3,4,5]
len = 5: [1,2,3,4,5]
��ô���ǿ����ҳ�����ʽ������Ϊn�ĵȲ������к��г�������Ϊ3��������Ƭ�ĸ���Ϊ(n-1)(n-2)/2����ô��Ŀ�ͱ������ԭ�����еȲ����еĳ��ȣ�Ȼ����빫ʽȥ��������ɣ��μ��������£�
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#�ҵķ��� my way
#coding=utf-8
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        opt, i = [0, 0], 1
        for j in xrange(2, len(A)):
            if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                opt.append(opt[j - 1] + i)
                i += 1
            else:
                opt.append(opt[j - 1])
                i = 1
        return opt[-1]

    def numberOfArithmeticSlices2(self, A):
        if len(A)<3:return 0
        dp=len(A)*[0]
        if A[2]-A[1]==A[1]-A[0]:
            dp[2]==1
        result=dp[2]
        for i in range(3,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
            result=result+dp[i]
        return result
    def numberOfArithmeticSlices3(self, A):
        if len(A)<3:return 0
        total=0
        dp=[0]*(len(A)+1)
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
            total=total+dp[i]
        return total

slu_=Solution()
t=slu_.numberOfArithmeticSlices3([1,2,3,4,5,6,88,9,10,11])
print t





#�ο���
#https://leetcode.com/problems/arithmetic-slices/#/description
#http://www.cnblogs.com/grandyang/p/5968340.html


