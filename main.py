import random
from itertools import permutations


pcount = 32
passengers = []  # wagi pasażerów, każdy waży losowo od 50 do 120kg
for i in range(pcount):
    x = random.randint(50, 120)
    passengers.append(x)

# F = m * r
# zakładamy że odległość między siedzeniami jest równa 1 m

raft_len = 8  # musi być parzyste
raft_wid = 4
upperRaft = [[0]*raft_wid for x in range(int(raft_len/2))]  # górna połowa tratwy
lowerRaft = [[0]*raft_wid for x in range(int(raft_len/2))]  # dolna połowa tratwy
fullRaft = upperRaft+lowerRaft
for x in fullRaft:
    print(x)


def checkBalance(upperRaft, lowerRaft,passengers):  # funkcja obliczająca nierównowage pomiędzy stronami tratwy
    halfRaftLen = int(len(lowerRaft))
    upperForce = 0
    lowerForce = 0
    for i in range(halfRaftLen):  # obliczam sile dolnej polowy tratwy
        rowWeight=0
        for seat in lowerRaft[i]:
            rowWeight+=passengers[seat]
        lowerForce += i*rowWeight

        rowWeight=0
        for seat in lowerRaft[halfRaftLen-i]:
            rowWeight+=passengers[seat]
        upperForce += i*rowWeight

    disbalance = abs(lowerForce-upperForce)
    return disbalance


def bForce():  # kompletny brute force, testuje wszystkie możliwe kombinacje
    elements = list(range(raft_len * raft_wid))
    all_permutations = permutations(elements)
    tempRaft = [[0] * raft_wid for _ in range(raft_len)]
    halfRaftLen = int(raft_len/2)
    for permutation in all_permutations:
        for i in range(raft_len):
            for j in range(raft_wid):
                tempRaft[i][j] = permutation[i * raft_wid + j]
        upperRaft = tempRaft[:halfRaftLen]
        lowerRaft = tempRaft[halfRaftLen:]
        checkBalance(upperRaft, lowerRaft, passengers)
    return 0


def improved_bForce():  # poprawiony brute force, uwzględnione jest to że pasażerowie siedzący w róznych miejscach w tym samym rzedzie nic nie zmieniają

    return 0