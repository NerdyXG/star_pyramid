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
      *
    * * *
  * * * * *
* * * * * * *

    *
  * * *
* * * * *
	 I printed n number of stars

	whitespace = +ve step CONSTANT
	num_of_whitespace = VARIES INCREMENTALLY OR DECREMENTALLY
"""



def bottom_top(n):
	num_of_whitespace = 0
	for i in range(n, 0, step):
		print(num_of_whitespace * " ", end="")
		for j in range(i):
			print("*", end=" ")
		num_of_whitespace -= whitespace
		print()


def top_down(n):
	num_of_whitespace = n - 1
	for i in range(1, n + 1, step):
		print(num_of_whitespace * " ", end="")
		for j in range(i):
			print("*", end=" ")
		num_of_whitespace += whitespace
		print()



print("n = the maximum number of stars in a row, usually the first or last row")
print("step = by how many digits should the stars decrease or increase")
print("floating point numbers are rounded down to their nearest int")
print("use +ve step for a top-down pyramid, and -ve step for a bottom_top pyramid")
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
		if step > n:
			print(f"step must be lesser than n, {n}")
		elif step == 0:
			print("step cannot be zero (0)")
		else:
			break


whitespace = step
# decision tree to decide the printing style
if step > 0:
	if __name__ == "__main__":
		top_down(n)

else:
	if __name__ == "__main__":
		bottom_top(n)
