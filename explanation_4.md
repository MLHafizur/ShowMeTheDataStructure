Problem 4: active directory
=============================
A binary search tree is used to store users in a given group. 

Time complexity
------------------
The is_user_in_group function has two primary operations---(1) adding users in a group/subgroup to a binary search tree. (2) searching a user in the tree.  The time complexity to build the tree is O(nlog(n)), and searching a user in the binary tree is O(log(n)). In worst-case scenario, the time complexity of the function is O(nlog(n)) +O(log(n)),which will be ~ O(nlogn)

Space complexity
------------------
The space complexity is O(n) beucase the user information is stroed in a binary search tree, which is linearly dependent on the users (input size)
