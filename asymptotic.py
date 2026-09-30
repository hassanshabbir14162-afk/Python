n=10

guess = input("Double looop at n=10 checks n x n pairs. How many?")

input("Formula: one calculation, done. Press enter to run")
steps = 1
print(" steps =", steps, "->0(1) constant time-> steps never change")

input("Loop, one step per item. Please press enter to run")
steps=0
for i in range(n):
    steps += 1
print(" steps =", steps, "->0 (n) linear time -> steps grow with n")

input("Double loops: checks every pair. Press enter to run ")
steps=0
for i in range(n):
    for j in range(n):
        steps +=1
print("steps =", steps, "Your guess", guess, "-> 0(n^2) quadratic time")
