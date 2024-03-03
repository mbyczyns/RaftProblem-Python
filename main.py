import random

pcount = 32
passengers = [] #wagi pasażerów, każdy waży losowo od 50 do 120kg
for i in range(pcount):
    x = random.randint(50,120)
    passengers.append(x)

# F = m * r
# zakładamy że odległość między siedzeniami jest równa 1 m
raft_len = 8 # musi być parzyste
raft_wid = 4
upperRaft =[[0]*raft_wid for x in range (int(raft_len/2))] # górna połowa tratwy
lowerRaft = [[0]*raft_wid for x in range (int(raft_len/2))] # dolna połowa tratwy

def checkBalance(upperRaft, lowerRaft): # funkcja obliczająca nierównowage pomiędzy stronami tratwy
    halfRaftLen = int(len(lowerRaft))
    upperForce=0
    lowerForce=0
    for i in range (halfRaftLen):
        lowerForce+= i*sum(lowerRaft[i])
        upperForce+= (halfRaftLen-i)*sum(upperRaft[halfRaftLen-i])
    disbalance = abs(lowerForce-upperForce)
    return disbalance


def bForce(): # kompletny brute force, testuje wszystkie możliwe kombinacje

    return 0

def improved_bForce(): # poprawiony brute force, uwzględnione jest to że pasażerowie siedzący w róznych miejscach w tym samym rzedzie nic nie zmieniają

    return 0