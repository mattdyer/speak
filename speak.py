import sys
import json
from os.path import exists

args = sys.argv

del args[0]


prompt = " ".join(args)

print(prompt)

#endOfPrompt = prompt[-10:]

#print(endOfPrompt)

print(max(-5, 0))

def make_memories(prompt, memory):
	prompt_components = get_prompt_components(prompt)
	
	for component in prompt_components:
		add_component_memory(component, memory)
	

def get_prompt_components(prompt):
	components = []
	
	print(len(prompt))
	
	for i in range(-10, len(prompt)):
		print(i)
		start = max(0, i)
		stop = i + 10
		if(stop < len(prompt)):
			print(True)
			print(start)
			print(stop)
			#print(prompt[start:stop])
			components.append({
				'key': prompt[start:stop],
				'value': prompt[stop]
			})
	
	print(components)
	
	return components

def add_component_memory(component, memory):
	if component['key'] in memory.keys():
		if component['value'] in memory[component['key']].keys():
			memory[component['key']][component['value']] = memory[component['key']][component['value']] + 1
		else:
			memory[component['key']][component['value']] = 1
	else:
		memory[component['key']] = {component['value']: 1}

def generate_response(prompt, memory):
	response_and_prompt = prompt
	response = ''
	
	for i in range(1, 50):
		endOfPrompt = response_and_prompt[-10:]
		next_char = get_next_character(endOfPrompt, memory)
		print(next_char)
		
		if(next_char == ''):
			break
		response = response + next_char
		response_and_prompt = response_and_prompt + next_char
	
	return response

def get_next_character(endOfPrompt, memory):
	if endOfPrompt in memory.keys():
		memory_location = memory[endOfPrompt]
		next_char = ''
		
		highest_count = 0
		
		for char_choice in memory_location:
			if memory_location[char_choice] > highest_count:
				next_char = char_choice
				highest_count = memory_location[char_choice]
		
		
	else:
		next_char = ''
	
	return next_char

memory_path = 'memory/memory.json'

def load_memory(memory_path):
	
	if(exists(memory_path)):
		memory_file = open(memory_path,'r')
		
		loaded_memory = json.loads(memory_file.read())
	else:
		loaded_memory = {}
	
	return loaded_memory

def save_memory(memory, memory_path):
	
	serialized_memory = json.dumps(memory)

	saved_archive = open(memory_path, 'w')

	saved_archive.write(serialized_memory)

	saved_archive.close()
	

memory = load_memory(memory_path)

make_memories(prompt, memory)

print('---')
print(memory)

response = generate_response(prompt, memory)

print(response)

save_memory(memory, memory_path)
