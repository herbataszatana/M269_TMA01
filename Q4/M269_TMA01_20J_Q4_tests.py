"""
Test file for M269 20J TMA01 Question 4.

Student version 4: 22/04/20
"""


from M269_TMA01_20J_Q4 import WaitingList

# tests for part (e)
print("tests for part (e)")

def testStillWaiting(waitingList,destination):
    numberWaiting = w.stillWaiting(destination)
    print(numberWaiting, " waiting to fly to ", destination)

w=WaitingList()
print("Waiting list empty")
testStillWaiting(w,"Milan")

w.put(2,"Rome")
print("only one group in waiting list")
testStillWaiting(w,"Rome")

w.put(3,"Rome")
w.put(2,"Naples")
w.put(1,"Pisa")
w.put(1,"Florence")
w.put(25,"Rome")
print("longer waiting list")
testStillWaiting(w,"Rome")
testStillWaiting(w,"Naples")
testStillWaiting(w,"Pisa")
testStillWaiting(w,"Florence")
testStillWaiting(w,"Milan")

w.take(4,"Rome")
print("removed a group")
testStillWaiting(w,"Rome")
