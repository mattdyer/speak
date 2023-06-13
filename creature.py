import sys
import json
from os.path import exists

args = sys.argv

del args[0]


prompt = " ".join(args)

print(prompt)

creature = {}

#creature = {
#	32: {
#		'next': 92,
#		'multiplier': 0,
#		'next_multiplier': 1
#	}
#}


def generate_response(creature, prompt, loop_function):
	prompt_values = convert_text_to_values(prompt)
	
	print(prompt_values)
	
	response_values = get_response_values(creature, prompt_values, loop_function)
	
	print(response_values)
	
	response = convert_values_to_text(response_values)
	
	return response


def get_response_values(creature, prompt_values, loop_function):
	
	response_values = []
	
	response_values = loop_function(creature, prompt_values, response_values, loop_function, 1)
	
	return response_values
		
	
def loop_values(creature, prompt_values, response_values, loop_function, call_count):
	
	call_again = True
	
	for index, value in enumerate(prompt_values):
		modify_response(creature, prompt_values, response_values, value, index)
		
	
	if call_count > 5:
		call_again = False
	
	if call_again:
		response_values = loop_function(creature, prompt_values, response_values, loop_function, call_count + 1)
	
	return response_values
		

def modify_response(creature, prompt_values, response_values, value, index):
	if value in creature.keys():
		if creature[value] != 0:
			response_values.append(creature[value] * value)
	else:
		creature[value] = 1
	

# def get_response_values(creature, prompt_values):
	
# 	response_values = []
	
# 	for index, value in enumerate(prompt_values):
# 		if value in creature.keys():
# 			calculated_next = creature[value]['next'] * creature[value]['next_multiplier']
# 		else:
			
# 			if len(prompt_values) >= index + 1:
# 				next_value = prompt_values[index + 1]
# 			else:
# 				next_value = 0
			
# 			creature[value] = {
# 				'next': next_value,
# 				'multiplier': 0,
# 				'next_multiplier': 1
# 			}
			
# 			calculated_next = next_value
		
# 		if(calculated_next == 0):
# 			break
		
# 		response_values.append(round(calculated_next))
		
	
# 	return response_values


def convert_text_to_values(prompt):
	prompt_values = []

	for character in prompt:
		prompt_values.append(ord(character))
	
	return prompt_values


def convert_values_to_text(values):
	result = ''
	
	for value in values:
		result = result + chr(value)
	
	return result


response = generate_response(creature, prompt, loop_values)

print(creature)
print(response)
