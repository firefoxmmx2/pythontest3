#!/usr/bin/env python

'''
Created on 2012-12-5

'''

a = (45,13,12,16,9,15)

class Node(object):
    def __init__(self,weight=None,parent=None,left=None,
                 right=None):
        self.weight=weight
        self.parent=parent
        self.left=left
        self.right=right
        
def huffman_tree():
    HuffNode=[]
    
    #input weight
    for n in range(len(a)):
        HuffNode.append(Node(a[n],-1,-1,-1))
    n=len(HuffNode)
    for i in range(n):
        m1=m2=1000
        x2=x1=0
        for j in range(n+1):
            if HuffNode[j].weight<m1 and HuffNode[j].parent==-1:
                m2=m1
                x2=x1
                m1=HuffNode[j].weight
                x1=j
            elif HuffNode[j].weight<m2 and HuffNode[j].parent==-1:
                m2=HuffNode[j].weight
                x2=j
                
            HuffNode[x1].parent=HuffNode[x2].parent=n+i
            HuffNode.append(Node(HuffNode[x1].weight+HuffNode[x2].weight,
                                 -1,x1,x2))
            print('x1.weight and x2.weight in round %d: %d, %d'%(i+1,
                    HuffNode[x1].weight,HuffNode[x2].weight))
            
if __name__ == '__main__':
    huffman_tree()        