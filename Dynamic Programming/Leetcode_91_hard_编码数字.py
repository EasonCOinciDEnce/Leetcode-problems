'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
�������ֵı��� �ٸ�����
1234����Ϊ   1 2 3 4     1 23 4      12 3 4   ������������
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#����һ
class Solution(object):
    def Decode(self, s):
        # dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        if s == "": return 0
        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i != 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":  # "01"ways = 0
                dp[i] += dp[i - 2]
        return dp[len(s)]

slu_=Solution()
print slu_.Decode('1211')

#������ ���ķ�ʽ
