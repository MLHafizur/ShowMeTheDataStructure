Problem 6: union and intersection of two lists
=================================================
To find union of two linked lists, I am using an array. First, I add elements of the first linked list to the array. Second, I check if elements of the second linked list are in the array or not. If they are not in the array, the elements are added otherwise ignored. 

Time complexity
---------------------
The time complexity of the union function is quadratic because for each element in the linked list, there is a python `in` operation, which is O(n) by itself, to check if they already exits in the list or not. 

But, the time complexity of the union function is O(n^3) because, there are two while loops that loop over the elements of the two linked lists, plus there is Python `in` operation that checks for each element if they occur in a temporary list or not.

 Other operations are---(1) adding elements from linked list to the array, which is linear. (2) there is another operation that reads elements from the array and add them to a linked list, which is also linear.

 Space complexity
 -------------------
 The space complexity for union (and also for intersection) functions is O(n), because for both operations there is a temporary array called tmp_list, which can grow upto the size of the two input linked lists. Also there are two nodes (i.e. node1 and node2) but these should be O(1). So overall the space complexity of union is O(n), and the space complexity of intersection is O(n) too.
