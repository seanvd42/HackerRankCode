'''
2. Question 2
A sewer drainage system is structured as a tree. Water enters the system at n nodes numbered
from 0 to n-1 and flows through the tree to the root, which as the number 0. The tree structure is
defined by an array parent, where parent[i] = j means that water flows from
node i to its direct parent node j. Water exits the system after it flows through the root, so the
root has no parent, represented as parent[0] = -1. The value in input[i] denotes the amount of
water that enters the sewer system at node i. This excludes water that flows into i from its
children. The total flow through a node is thus the flow that enters at that node, plus the sum of
the total flows of all of its children.

Your task is to divide the system into two smaller pieces by cutting one branch so that the total
flows of the resulting subtrees are as close as possible.

Example
parent = [-1, 0, 0, 1, 1, 2]
input = [1, 2, 2, 1, 1, 1]

The structured of the system is shown in the diagram below. The nodes are labeled as <node number>/<input flow>.



Cut the branch between nodes 1 and 0.
The partition {0, 2, 5} has total flow input[0] + input[2] + input[5] = 1 + 2 + 1 = 4.
The partition {1, 3, 4} has total flow input[1] + input[3] + input[4] = 2 + 1 + 1 = 4.
The absolute difference between the total flows of the two new sewer systems is 4 - 4 = 0
It's no possible fro a different division to achieve a smaller difference than 0, so the final answer
is 0.

Function Description
Complete the function drainagePartition in the editor below.

The function has the following parameter(s):
int parent[n]: each parent[i] is the parent node of node i
int input[n]: each input[i] is the direct flow into the system at node i

Returns
int: the minimum (positive) difference in total flow between the two new sewer systems


Constraints
 2 <= n <= 10^5
 1 <= input[i] <= 10^4
 parent[0] = -1
 parent[i] < i for 1 <= i < n
 The depth of the tree is at most 500

Sample Input
STDIN     Function
-----    --------
4     -> parent[] size n = 4
-1    -> parent[] = [-1, 0, 1, 2]
0
1
2
4     -> input[] size n = 4
1     -> input[] = [1, 4, 3, 4]
4
3
4
 
Sample Output
2
 
Explanation

The structure of the system is shown in the diagram below:
 

The optimal value of 2 is achieved by cutting between nodes 1 and 2. The resulting subtrees {0,
1} with total flow 1 + 4 = 5 and {2, 3} with total flow 3 + 4 = 7 differ by | 5 - 7 | = 2

'''

def drainagePartition(parent, input):
    cumSum = [0] * len(input)
    cumSum[0] += input[0]
    for i in range(len(parent)-1,0,-1):
        cumSum[i] += input[i]
        cumSum[parent[i]] += cumSum[i]
    target = cumSum[0] / 2.0
    minDiff = 500 * 10^4 + 1
    for flow in cumSum:
        diff = abs(target - flow)
        if (diff < minDiff):
            minDiff = diff
    return int(2*minDiff)

        
if __name__ == '__main__':
    print ("Sample 0 (Should be 0)")
    parent = [-1, 0, 0, 1, 1, 2]
    input = [1, 2, 2, 1, 1, 1]
    minDiff = drainagePartition(parent, input)
    print (minDiff)
    print ("")
    print ("Sample 1 (Should be 2)")
    parent = [-1, 0, 1, 2]
    input = [1, 4, 3, 4]
    minDiff = drainagePartition(parent, input)
    print (minDiff)