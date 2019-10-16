import random
from visualize import Visual


# Input is the length of the pipes in the sequence in which they appear
def water(pipes):
	"""
	Your answer to the problem here
	"""

	# Will display all test cases visualization
	screen = Visual(pipes, 1600, 1000)
	screen.show()
	# Comment out lines above to stop visulation 

	# If length is less than 3 than nothing can be contained
	if len(pipes) < 3:
		return 0 
	
	area = 0
	ind = 0

	while ind < len(pipes)-1:
		for x in range(ind+1, len(pipes)):
			pipe = pipes[x]
			if pipe >= pipes[ind]:  # look for a pipe that is greater than or equal to last tallest pipe
				num_pipes = x-ind -1  # how many pipes we are finding area for
				area += (min(pipe, pipes[ind]) * num_pipes) - sum(pipes[ind+1:x])  # add area of all pipes inbetween these pipes
				ind = x  # change the last tallest pipe to be the one we found
				break
		else:
			# if we couldn't find a pipe taller than the last tallest pipe
			p = max(pipes[ind+1:])  # find the tallest one we can
			pipe_ind = pipes[ind+1:].index(p) + ind + 1  # calculate the index in the list of that pipe
			num_pipes = pipe_ind-ind-1  # how many pipes we are finding area for
			area += (p * num_pipes) - sum(pipes[ind+1:pipe_ind])  # add area of all pipes inbetween those two pipes
			ind = pipe_ind  # change last tallest pipe to be the pipe we found
		
	return area  # return answer

# Run the test_cases.py file to test your answer, make sure you have your function named water
# To see the solution, look at Solution.py
