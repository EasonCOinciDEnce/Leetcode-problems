'''
����һ������������д��������ж��ٶ������ĺ͵���������������������������������ֵС��1000��
�磬����Ϊ10, ����Ӧ��������Ϊ2�����������������ĺ�Ϊ10,�ֱ�Ϊ(5,5),(3,7)�� 
�������һ������n,(3 �� n < 1000)
'''
input_=int(raw_input())
nums = [x for x in range(1, input_)]
zhishu = []
for num in nums:
    if num > 1:
        for i in range(2, num/2):
            if (num % i) == 0:
                break
        else:
            zhishu.append(num)

cout_=0
for i in zhishu:
    if 2*i==input_:
        cout_=cout_+1
    if (input_-i) in zhishu:
        cout_=cout_+0.5
print int(cout_)