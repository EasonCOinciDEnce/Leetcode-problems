'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#�ҵķ��� my way
#coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        local_op = 0
        global_op = 0
        for i in range(1, len(prices)):
            local_op = max(prices[i] - prices[i-1] + local_op, prices[i] - prices[i-1])#ע�����ﲻҪд��
            global_op = max(global_op, local_op)
        return global_op


Su_=Solution()
print Su_.maxProfit([7, 1, 5, 3, 6, 4])


#���ͣ�
# ��̬�滮����
����������һ�ν����ܵõ���������������brute force�Ľⷨ���Ƕ�ÿ�齻�׶���һ������ȡ�������ģ�������n*(n-1)/2�����ܽ��ף����Ը��Ӷ���O(n^2)��
�����׸о��������Ƕ�̬�滮����Ŀ����ʵ��Maximum Subarray�ǳ����ƣ��á��ֲ����ź�ȫ�����Žⷨ����˼·��ά������������һ���ǵ�ĿǰΪֹ��õĽ��ף���һ��
���ڵ�ǰһ����������ѽ��ף�Ҳ���Ǿֲ����ţ�������ʽ��local[i+1]=max(local[i]+prices[i+1]-price[i],0), global[i+1]=max(local[i+1],global[i])��
����һ��ɨ��Ϳ��Եõ������ʱ�临�Ӷ���O(n)�����ռ�ֻ��Ҫ������������O(1)�� 




#�ο���
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/solutions
#http://blog.csdn.net/linhuanmars/article/details/23162793




#������Ŀ
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description