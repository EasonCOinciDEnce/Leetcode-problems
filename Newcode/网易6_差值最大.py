'''
С����ʦ�Ƿǳ�������,����Ҫ������ѧ���ڽ������ǰ���ų�һ��,������Ҫ��ѧ��������߲��ݼ���˳�����С���һ��,n��ѧ�����жӵ�ʱ��,С����ʦ����ȥ�������ˡ�ѧ���������л��ᷴ����,����ѧ���Ǿ�����һ�η��Ķ���,���Ƕ���һ�����еķ��ֵΪÿ����������ѧ����߲�ľ���ֵ�ܺ͡����ڰ������˳�����еĶ��еķ��ֵ����С��,���ǵ�Ȼ�������շ��ֵ����˳���������жӡ����ڸ���n��ѧ�������,��������Щѧ���жӵ������ܵķ��ֵ��С����ʦ����һ�������ð����� 
��������:

�����������,��һ��һ������n(1 �� n �� 50),��ʾѧ��������
�ڶ���Ϊn������h[i](1 �� h[i] �� 1000),��ʾÿ��ѧ�������


�������:

���һ������,��ʾn��ѧ���жӿ��Ի�õ����ķ��ֵ��

��������ʾ: 
����������˳����: 25-10-40-5-25, ��߲����ֵ���ܺ�Ϊ15+30+35+20=100��
�������ķ��ֵ�ˡ�
ʾ��1
����

5
5 10 25 40 25
���

100
'''
n=raw_input()
nums=[int(x) for x in raw_input().split(' ')]
nums.sort()
result=[]
result.append(nums[-1])
nums.pop()
while len(nums):
    result.append(nums[0])
    result.insert(0,nums[1])
    result.append(nums[-1])
    result.insert(0,nums[-2])
    nums.pop()
    nums.pop()
    nums.pop(0)
    nums.pop(0)
    if len(nums)<4:
        break
if len(nums)==3:
    result.append(nums[0])
    result.append(nums[2])
    result.insert(0,nums[1])
elif len(nums)==2:
    if abs(result[0]-nums[0])+abs(result[-1]-nums[-1])>abs(result[0]-nums[-1])+abs(result[-1]-nums[0]):
        result.append(nums[-1])
        result.insert(0,nums[0])
    elif abs(result[0]-nums[0])+abs(result[-1]-nums[-1])==abs(result[0]-nums[-1])+abs(result[-1]-nums[0]):
        result.append(nums[0])
        result.append(nums[1])
    else:
        result.append(nums[0])
        result.insert(0,nums[1])
elif len(nums)==1:
    if abs(result[-1]-nums[0])>abs(result[0]-nums[0]):
        result.append(nums[0])
    else:
        result.insert(0,nums[0])
t=0
for i in range(len(result)-1):
    t=t+abs(result[i+1]-result[i])
print t