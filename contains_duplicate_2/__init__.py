"""
# PROBLEM ID : CONDUP2
------------------
Problem Statement:
------------------
i/p : array[int] , int k
o/p : True/False

- one array of integers is given
- check if two entries exist in the array such that their value is same and distance between them is 
less than or equal to 'k'

----
# 1.
----
----------------------------------
i/p: array = [1,0,0,1,1] , k = 1
o/p: True
explaination:
array[3] == array[4]
and abs(3-4) is 1 which is <= k
----------------------------------

----
# 2.
----
---------------------------------
i/p: array = [1,2,3,1], k = 3
o/p: True
explaination:
array[0] == array[3]
and abs(0-3) is 3 which is <= k
---------------------------------

----
# 3.
----
---------------------------------
i/p: array = [1,2,3,1,2,3], k = 2
o/p: False
explaination:
array[0] == array[3] 
but abs(0-3) is 3 which is > k
,
array[1] == array[4]
but abs(1-4) is 3 which is > k
---------------------------------

"""