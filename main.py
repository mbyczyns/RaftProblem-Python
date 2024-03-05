import random
import functions
import time


raft_len = 4  # musi być parzyste
raft_wid = 2
pcount = raft_wid*raft_len
passengers = []  # wagi pasażerów, każdy waży losowo od 50 do 120kg
for i in range(pcount):
    x = random.randint(50, 120)
    passengers.append(x)

# F = m * r
# zakładamy że odległość między siedzeniami jest równa 1 m


upperRaft = [[0]*raft_wid for x in range(int(raft_len/2))]  # górna połowa tratwy
lowerRaft = [[0]*raft_wid for x in range(int(raft_len/2))]  # dolna połowa tratwy
fullRaft = upperRaft+lowerRaft

upperRaft[0][0] = 2
upperRaft[0][1] = 1
upperRaft[1][0] = 4
upperRaft[1][1] = 7
lowerRaft[0][0] = 0
lowerRaft[0][1] = 3
lowerRaft[1][0] = 6
lowerRaft[1][1] = 5

# start = time.time()
# disb, raft = functions.bForce(upperRaft,lowerRaft,raft_len,raft_wid,passengers)
# for element in raft:
#     print(element)
# print(disb)
# print(time.time()-start)

print(functions.checkBalance(upperRaft, lowerRaft, passengers))
print(passengers)
for row in upperRaft:
    print(row)
for row in lowerRaft:
    print(row)