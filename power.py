input("A set with n elementshas 2^n subsets.")
print(" 3 elements 2^3 =", 2**3, "subsets")
print(" mask 5 = binary", bin(5)[2:], " selects positions 0 and 2")

n = int(input("Enter number of elements(try 4 and 5): "))
guess = input("How many subsets does a set of" + str(n) + "Elements have? ")
input("Each element is in or not - 2 choices of elements. Press Enter")
print(" ", n, "elements subsets:", 2**n, "Your Guess:", guess)