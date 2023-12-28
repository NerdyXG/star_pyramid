"""
	Print n number of stars
	A white space comes after each star
	As the number of lines increases n reduces by 2
	eg
	* * * * *
	 *  *  *
	    *
* * * * *
  * * *
    *

	 What did I do?

	 I printed n number of stars
"""

def print_stars(n):
	whitespace = 0
	for i in range(n, 0, step):
		print(whitespace * " ", end="")
		for j in range(i):
			print("*", end=" ")
		whitespace += num_of_whitespace
		print()


print("n = the maximum number of stars in a row, usually the first row")
print("step = by how many digits should the stars decrease")
print("floating point numbers are rounded down to their nearest int")
print("------------------------")



# validates the value of n
while True:
	try:
		n = int(input("n = "))
	except ValueError:
		print("Non-numeric symbols are not supported!")
	else:
		if n < 1:
			print("n must be a number greater than zero (0)")
		else:
			break

# validates the step value
while True:
	try:
		step = int(input("step = "))
	except ValueError:
		print("Non-numeric symbols are not supported!")
	else:
		if step >= n:
			print(f"Step must be lesser than n, {n}...")
		else:
			break


# ensures that step is negative
if step > 0:
	num_of_whitespace = step
	step = 0 - step

else:
	num_of_whitespace = 0 - step

print_stars(n)