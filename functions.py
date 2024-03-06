from itertools import permutations



def checkBalance(upperRaft, lowerRaft,passengers):  # funkcja obliczająca nierównowage pomiędzy stronami tratwy
    halfRaftLen = len(lowerRaft)
    upperForce = 0
    lowerForce = 0
    for upperRow in upperRaft:
        rowWeight=0
        for seat in upperRow:
            rowWeight+=passengers[seat]
        dist = halfRaftLen - upperRaft.index(upperRow)
        lever = dist*rowWeight
        upperForce+=lever

    for lowerRow in lowerRaft:
        rowWeight=0
        for seat in lowerRow:
            rowWeight+=passengers[seat]
        dist = lowerRaft.index(lowerRow) + 1
        lever = dist * rowWeight
        lowerForce+=lever

    return abs(lowerForce-upperForce)


def bForce(raft_len, raft_wid, passengers):  # kompletny brute force, testuje wszystkie możliwe kombinacje
    elements = list(range(raft_len * raft_wid))
    potentialDisbalance = 10000000
    all_permutations = permutations(elements)
    potentialRaft = [[0] * raft_wid for _ in range(raft_len)]
    halfRaftLen = raft_len//2
    for permutation in all_permutations:
        tempRaft = [[0] * raft_wid for _ in range(raft_len)]
        for i in range(raft_len):
            for j in range(raft_wid):
                tempRaft[i][j] = permutation[i * raft_wid + j]
        for row in tempRaft:
            print(row)
        upperRaft = tempRaft[:halfRaftLen]
        lowerRaft = tempRaft[halfRaftLen:]
        tempDisbalance = checkBalance(upperRaft, lowerRaft, passengers)
        print(tempDisbalance)
        print("----------------")
        if(tempDisbalance<potentialDisbalance):
            potentialRaft = tempRaft
            potentialDisbalance = tempDisbalance
    print("=============")
    for row in potentialRaft:
        print(row)
    return potentialDisbalance, potentialRaft


def improved_bForce():  # poprawiony brute force, uwzględnione jest to że pasażerowie siedzący w róznych miejscach w tym samym rzedzie nic nie zmieniają

    return 0