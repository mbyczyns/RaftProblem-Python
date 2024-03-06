import random
import functions
import time


raft_len = 2  # musi być parzyste
raft_wid = 2
pcount = raft_wid*raft_len
passengers = []  # wagi pasażerów, każdy waży losowo od 50 do 120kg
for i in range(pcount):
    x = random.randint(50, 120)
    passengers.append(x)

# F = m * r
# zakładamy że odległość między siedzeniami jest równa 1 m

start = time.time()
disb, bestraft = functions.bForce(raft_len,raft_wid,passengers)
print("Best raft:")
for element in bestraft:
    print(element)
print(disb)
print(time.time()-start)

