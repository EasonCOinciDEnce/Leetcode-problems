'''
��һ���������������������㰴�����һ��һ��ش����������α�ţ��������Ϊ1���������������a��b�������һ���㷨�����a��b�������������ȵı�š�
��������int a,b��Ϊ�������ı�š��뷵��a��b������������ȵı�š�ע�������㱾��Ҳ����Ϊ�������ȡ�
����������
'''
# coding=utf-8
# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        while a!=b:
            if a>b:
                a/=2
            elif a<b:
                b/=2
            else:
                break
        return a
lca_=LCA()
print lca_.getLCA(10,18)
#https://www.nowcoder.com/practice/70e00e490b454006976c1fdf47f155d9?tpId=8&&tqId=11017&rp=1&ru=/activity/oj&qru=/ta/cracking-the-coding-interview/question-ranking