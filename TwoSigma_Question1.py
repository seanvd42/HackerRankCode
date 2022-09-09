'''
Question 1

An Initial public offering (IPO) refers to the process of offering shares of a private corporation to
the public in a new stock issuance. Public share issuance allows a company to raise capital from
public investors. IPO process can go through a typical auction, and an IPO price is not set before
the auction. Potential buyers are able to bid for the shares they want and the price they are
willing to pay. The bidders who were willing to pay the highest price are then allocated the
shares available.

Before the auction ends, potential buyers can submit bids containing: user Id, number of shares,
bidding price, timestamp. Once all the bids are submitted, the allotted placement is assigned to
the bidders from the highest bids down, until all of the allotted shares are assigned. The auction
assigns shares in multiple rounds until all shares are allocated or no more bids.. In each round, it
finds the bids with the highest prices, assigns the shares, and removes the assigned bids:

1. If the bid (with the highest price) has only 1 bidder, the bidder gets shares he/she bids for (or
gets whatever is left if the unallocated shares are less than the bid shares);

2. If the bids (with the highest price) have multiple bidders, the bidders are assigned shares as
follows:

Shares are distributed round robin style to bidders in the same price group, with the bidders
sorted by timestamp. Once a bidder gets the number of shares they bid for, they will be removed
from the above Iterative process and the process which then continues until all bidders are
removed or the shares get exhausted, whichever comes first.

Find out all bidders (user IDs) with no share allocation.


Function Description
Complete the function getResults in the editor below. The function must return a list of integers,
each an id for those bidders who receive no shares, sorted ascending.

getResults has following parameter(s):
bids[bids[0],...bids[n-1]]: a 2D array of arrays of Integers, Id, shares, price, timestamp named u,
sc, bp, ts going forward
totalShares: an Integer, the total shares to allocate

Constraints
1 <= n < 10^4
1 <=u, sc, bp, ts, totalShares < 10^8

Sample Input 0
3
4
1 2 5 0
2 1 4 2
3 5 4 6
3

Sample Output 0
3

Explanation 0
There are totalShares = 3 shares among the 3 bidders. The first 2 shares are allotted to the user
with Id 1 as it has the highest bidding price. The 3rd share is allotted to the user with Id 2 as it is
the first user, based on timestamp, in the bidding group having the bidding price 4. The only
bidder who doesn't receive shares has the user Id of 3.

Sample Input 1
4
4
1 3 1 9866
2 1 2 5258
3 2 4 5788
4 2 4 6536
2


Sample Output 1
1
2

Explanation 1
There are totalShares = 2 shares among the 4 bidders. The users with Id 3 and 4 have the highest
bidding price. The totalShares are given out 1 by 1 cycling between the user Ids 3 and 4 until
there are no more shares. The result is user Id of 3 and 4 both receive a single share and the users
with Id 1 and 2 are left with no shares.
'''

#Coding Section
#!/bin/python3

#
# Complete 'the getResults' function below
#
# The function is expected to return a list of user ids with no shares
# The function accepts following parameters
#  1. 2D_INTEGER_ARRAY bids
#  2. INTEGER totalShares
#

def getResults(bids, totalShares):
    noShares = set()
    bidsDict,sortedKeys = getBidsDict(bids, noShares)
    while (totalShares > 0):
        awardShare(bidsDict, sortedKeys, noShares)
        totalShares -= 1

    for user in noShares:
        print(user)

def getBidsDict(bids, noShares):
    sBids = sorted(bids, key = lambda x: (x[2], -x[3]), reverse=True)
    bidsDict = {}
    sortedKeys = []
    for bid in sBids:
        if(bid[2] in bidsDict):
            bidsDict[bid[2]].append(bid)
        else:
            bidsDict[bid[2]] = [bid]
            sortedKeys.append(bid[2])
        noShares.add(bid[0])
    return bidsDict,sortedKeys

def awardShare(bidsDict, sortedKeys, noShares):
    bid = bidsDict[sortedKeys[0]].pop(0)
    noShares.discard(bid[0])
    if (bid[1] > 1):
        bid[1] -= 1
        bidsDict[sortedKeys[0]].append(bid)
    elif not bidsDict[sortedKeys[0]]:
        del sortedKeys[0]




if __name__ == '__main__':
    print ("Sample 0")
    bids1 = [
            [1,2,5,0],
            [2,1,4,2],
            [3,5,4,6]
            ]
    totalShares1 = 3
    getResults(bids1, totalShares1)
    print ("")
    print ("Sample 1")
    bids2 = [
            [1,3,1,5258],
            [2,1,2,9866],
            [3,2,4,5788],
            [4,2,4,6536]
            ]
    totalShares2 = 4
    getResults(bids2, totalShares2)