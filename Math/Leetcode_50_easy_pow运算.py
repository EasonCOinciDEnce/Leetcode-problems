'''
mplement pow(x, n).������һ�����Ķ��ٴη���Ԥ��


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#coding=utf-8
def myPow(x, n):
    if n < 0:
        x = float(1) / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow
cc=myPow(4,16)
print cc


#�������
#https://leetcode.com/problems/powx-n/description/
