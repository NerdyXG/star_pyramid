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
	for i in range(n, 0, -2):
		print(whitespace * " ", end="")
		for j in range(i):
			print("*", end=" ")
		whitespace += 2
		print()

print_stars(7)