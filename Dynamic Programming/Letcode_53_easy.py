'''
����ָ������ĺ����
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8



#------------------------------------------------------------------------------------
#��׼����--ţ the best way-niu
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
Su_=Solution()
Su_.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


#------------------------------------------------------------------------------------
#�ҵķ��� my way
#coding=utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        if nums==None or len(nums)==0:
            return 0
        global_=nums[0]
        local=nums[0]
        for i in range(1,len(nums)):
            local=max(nums[i],local+nums[i])
            global_=max(local,global_)
        return global_
Su_=Solution()
Su_.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


#���ͣ�
# ��̬�滮����
����һ���ǳ�����Ķ�̬�滮����Ŀ���õ���˼·�����ڱ�Ķ�̬�滮��Ŀ��Ҳ�ܳ��ã��Ժ����ǳ�Ϊ���ֲ����ź�ȫ�����Žⷨ����
����˼·�������ģ���ÿһ��������ά������������һ����ȫ�����ţ����ǵ���ǰԪ��Ϊֹ���ŵĽ��ǣ�һ���Ǿֲ����ţ����Ǳ���
������ǰԪ�ص����ŵĽ⡣������˵˵��̬�滮�ĵ���ʽ�����Ƕ�̬�滮����Ҫ�Ĳ��裬�ݹ�ʽ�����ˣ������ϴ�����Ҳ�ͳ����ˣ���
����������֪��i����global[i]��ȫ�����ţ���local[i]���ֲ����ţ�����ô��i+1���ı��ʽ�ǣ�
local[i+1]=Math.max(A[i], local[i]+A[i])�����Ǿֲ�������һ��Ҫ������ǰԪ�أ����Բ�Ȼ������һ���ľֲ�����local[i]+
��ǰԪ��A[i]����Ϊlocal[i]һ��������i��Ԫ�أ����Բ�Υ�����������������local[i]�Ǹ��ģ���ô�������Ͳ��粻��Ҫ�ģ�����
��Ȼ����ֱ����A[i]��
global[i+1]=Math(local[i+1],global[i])�����˵�ǰһ���ľֲ����ţ���ôȫ�����ž��ǵ�ǰ�ľֲ����Ż��߻���ԭ����ȫ�����ţ�
����������ᱻ���ǽ�������Ϊ���ŵĽ������������ǰԪ�أ���ôǰ��ᱻά����ȫ���������棬���������ǰԪ�أ���ô��������ֲ����ţ���
���������Ƿ���һ�¸��Ӷȣ�ʱ����ֻ��Ҫɨ��һ�����飬����ʱ�临�Ӷ���O(n)���ռ������ǿ��Կ������ʽ��ֻ��Ҫ�õ���һ��local[i]��global
[i]�Ϳ��Եõ���һ���Ľ��������������ʵ���п�����һ������������������������Ҫ��һ�����飬Ҳ�����������ʵ�ֵ����������Կռ临�Ӷ�
������������local��global������O(2)=O(1)��
�������£� 




#�ο���
#https://leetcode.com/problems/maximum-subarray/#/description
#http://blog.csdn.net/linhuanmars/article/details/21314059




#������Ŀ
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description