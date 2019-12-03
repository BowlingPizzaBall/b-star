import numpy as np

# grammar_list : Simple function to properly list many strings
def grammar_list(listed):
	if len(listed) > 2:
		first_list = ", ".join(listed[:-1])
		listed = first_list + ", and " + str(listed[-1])
	elif len(listed) == 2:
		listed = " and ".join(listed)
	elif len(listed) == 1:
		listed = "".join(listed)
	else:
		listed = "none"
	return listed

# word_count : Returns a response's word count
def word_count(response):
	words = 0
	for piece in response.split(" "):
		for character in piece:
			if character.isalnum():
				words += 1
				break
	return words

# elim_prize : Returns how many contestants should prize and be eliminated (based on Dark's formulas)
def elim_prize(count):
	numbers = []

	if count == 2:
		numbers.append(1)
	else:
		numbers.append(round(count / 5))
	
	numbers.append(np.floor(np.sqrt(count) * np.log(count) / 3.75))
	return numbers