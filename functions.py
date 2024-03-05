from itertools import permutations



def checkBalance(upperRaft, lowerRaft,passengers):  # funkcja obliczająca nierównowage pomiędzy stronami tratwy
    halfRaftLen = len(lowerRaft)
    upperForce = 0
    lowerForce = 0
    for i in range(halfRaftLen):
        lowerRowWeight = 0
        for seat in lowerRaft[halfRaftLen+i]:
            lowerRowWeight+=passengers[seat]
        lowerForce += ((i+1)*lowerRowWeight)
        upperRowWeight=0
        for seat in upperRaft[halfRaftLen-1-i]:
            upperRowWeight+=passengers[seat]
        upperForce += ((i+1)*upperRowWeight)
    disbalance = abs(lowerForce-upperForce)
    return disbalance


def bForce(upperRaft, lowerRaft, raft_len, raft_wid, passengers):  # kompletny brute force, testuje wszystkie możliwe kombinacje
    elements = list(range(raft_len * raft_wid))
    potentialDisbalance=10000000
    all_permutations = permutations(elements)
    tempRaft = [[0] * raft_wid for _ in range(raft_len)]
    potentialRaft = [[0] * raft_wid for _ in range(raft_len)]
    halfRaftLen = int(raft_len/2)
    z=0
    for permutation in all_permutations:
        for i in range(raft_len):
            for j in range(raft_wid):
                tempRaft[i][j] = permutation[i * raft_wid + j]
        upperRaft = tempRaft[:halfRaftLen]
        lowerRaft = tempRaft[halfRaftLen:]
        tempDisbalance = checkBalance(upperRaft, lowerRaft, passengers)
        if(tempDisbalance)<potentialDisbalance:
            potentialRaft = tempRaft
            potentialDisbalance = tempDisbalance
        z+=1
        print(z)
    return potentialDisbalance, potentialRaft


def improved_bForce():  # poprawiony brute force, uwzględnione jest to że pasażerowie siedzący w róznych miejscach w tym samym rzedzie nic nie zmieniają

    return 0