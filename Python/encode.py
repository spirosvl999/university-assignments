import string
import json
import math

og_file = input("What file you want to encode?")                                                # We ask the user wich file he needs to encode

f = open(og_file + ".txt")
f = f.read                                                                                      # We read the User's file

lenght = len(f)                                                                                 # We caculate the lenght of the file

Winodw_Size = 0                                                                                 
look_ahead_buffer = 0                                                                           # For the last 2 lines, user had to help us about
                                                                                                # the lenght and the "window" we do the checking on.
                                                                                                # Because he didn't help us for the window, I used two random
                                                                                                # numbers that the program still working fine with.

def LongestMatch(self, f, current_position):
	end_of_buffer = min(current_position + self.look_ahead_buffer, lenght + 1)
	best_match_distance = -1
	best_match_length = -1

	for j in range(current_position + 2, end_of_buffer):
		start_index = max(0, current_position - self.Window_Size)
		substring = f[current_position:j]

		for i in range(start_index, current_position):
			repetitions = len(substring) // (current_position - i)
			last = len(substring) % (current_position - i)
			matched_string = f[i:current_position] * repetitions + f[i:i+last]

			if matched_string == substring and len(substring) > best_match_length:
				best_match_distance = current_position - i 
				best_match_length = len(substring)

	if best_match_distance > 0 and best_match_length > 0:
		return (best_match_distance, best_match_length)

	return None

i = 0

while i < lenght:

    match = LongestMatch(f, i)                                                                  # Now that we have the Longest match, we can start the LZ77 algorithm
    
    if match:
        (D,L) = match                                                                           # D for Distance and L for lenght
            
