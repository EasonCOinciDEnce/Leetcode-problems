'''
С�׽�n�����Ӱڷ���һ�����޴�������ϡ���i�����ӷ��ڵ�x[i]��y[i]�С�ͬһ������������ö�����ӡ�ÿһ�β���С�׿��԰�һ���������𲢽����ƶ���ԭ���ӵ��ϡ��¡����ҵ�����һ�������С�С����֪��Ҫ�������ϳ�����һ��������������i(1 �� i �� n)����������Ҫ�����ٲ�������.

��������:

�����������,��һ��һ������n(1 �� n �� 50),��ʾ���ӵĸ���
�ڶ���Ϊn�����ӵĺ�����x[i](1 �� x[i] �� 10^9)
������Ϊn�����ӵ�������y[i](1 �� y[i] �� 10^9)


�������:

���n������,��i����ʾ��������һ������������i����������Ҫ�Ĳ�����,�Կո�ָ��ĩ�޿ո�

��������ʾ:
����1������: ����Ҫ����
����2������: ��ǰ�������ӷ���(1, 1)��
����3������: ��ǰ�������ӷ���(2, 1)��
����4������: ���������Ӷ�����(3, 1)��
ʾ��1
����

4
1 2 4 9
1 1 1 1
���

0 1 3 10
'''

a=raw_input()
x=[int(i) for i in raw_input().split(' ')]
y=[int(j) for j in raw_input().split(' ')]
def calculatedistance(pinit1x,point1k,point2y,point2k):
    return abs(pinit1x-point1k)+abs(point2y-point2k)
ans=[6553000000]*100
for i in range(len(x)):
    for j in range(len(y)):
        lingshi=0
        tmp=[]
        for k in range(len(y)):
            tmp.append(calculatedistance(x[i],x[k],y[j],y[k]))
        tmp.sort()
        for k in range(len(y)):
            lingshi=lingshi+tmp[k]
            ans[k]=min(ans[k],lingshi)
for i in range(len(x)):
    print ans[i],