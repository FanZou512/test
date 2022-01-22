# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:40:16 2021

@author: 18143
"""

def Counter(nums):
    """ This function counts the numbers in the array nums, return the counts in res """
    n=len(nums)
    res=[0]*n # use maximum instead of n
    for k in nums:
        res[k-1]+=1

def BinarySearch(nums,target):
    """ This function finds the target in sorted nums list """
    n=len(nums)
    s1,s2=0,n
    while s1<=s2:
        mid=(s1+s2)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            s2=mid-1
        else:
            s1=mid+1
    return None

""" This is for tree class """
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def traverseInorder(self, root):
        """ traverse function will print all the node in the tree. """
        if root is not None:
            print(root.val)
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)

def TreeCreation(nums,k):
    if k>=len(nums):
        return None
    tree=TreeNode(nums[k])
    tree.left=TreeCreation(nums,k*2+1)
    tree.right=TreeCreation(nums,k*2+2)
    return tree