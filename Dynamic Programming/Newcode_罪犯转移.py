#�������
'''
C������Ҫת��һ���ﷸ��D�У�C����n���ﷸ����������ʱ����˳������ÿ���ﷸ��һ������ֵ��ֵԽ����Խ�ء�����Ϊ�˷�������г�����ת������ʱ��������c�����ˣ�ͬʱҪ��ת�Ʒ��˵�����ֵ֮�Ͳ�����t�����ж�����ѡ��ķ�ʽ�� 
��������:
��һ��������������:n��t��c(1��n��2e5,0��t��1e9,1��c��n)���ڶ��а�����ʱ�����ÿ�����˵�����ֵai(0��ai��1e9)
�������:
һ������𰸡�
ʾ��1
����

3 100 2
1 2 3
���

2
'''
# coding=utf-8
n,t,c=map(int,raw_input().strip().split())
nums=[int(x) for x in raw_input().split()]
ways=0
if len(nums)>c:
    s=sum(nums[:c])
    if s<=t:
        ways=ways+1
    for i in range(c,len(nums)):
        s+=nums[i]-nums[i-c]  #����ļ���Ƚ�����
        if s<=t:
            ways+=1
print ways


#https://www.nowcoder.com/practice/b7b1ad820f0a493aa128ed6c9e0af448?tpId=49&&tqId=29287&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking