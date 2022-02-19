''' Excercise 7 '''
import sys

# Program to find most frequent
# element in a list
def most_frequent(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	return num

def onlyLettersDigitsCharacters(Str):
  
    # If the string is empty
    # then print No
    if(len(Str) == 0):
        print("No")
        return False
 
    # Print Yes If the string matches
    if Str.isdigit() or Str.isalpha():
        return True        
    else:
        return False

 
fname = 'testfile.txt'
    
''' Define a dictionary with the available keys '''
available_keys = {}

''' Retrive the available keys and check if file is valid '''
''' r means read mode '''
with open(fname, 'r', encoding="ascii") as f:
    first_line = f.readline()    
    for word in first_line.split():
        if not onlyLettersDigitsCharacters(word):
            sys.exit("Not valid word found " + word)    
        available_keys[word] = word
        
    num_keys_first_line = len(available_keys)    
        
    for n,line in enumerate(f):
        for word in line.split():
            available_keys[word] = word
            if len(available_keys) != num_keys_first_line:
                sys.exit("file is not valid")
    ''' close file '''
    f.close()
    
print("The available keys are " +  str(available_keys.keys()))
provided_key = input("Please provide the key you are interested\n:")
print("You are interested on " + provided_key)

occurences = []
with open(fname, 'r', encoding="ascii") as f:
    for n,line in enumerate(f):
        count = line.count(available_keys[provided_key])
        occurences.append(count)
    ''' close file '''
    f.close()
    
print("Key " + provided_key + " occurences " + str(occurences))
print("The maximum value is " + str(max(occurences)))        
print("The minimum value is " + str(min(occurences)))
print("The most frequent value is " + str(most_frequent(occurences)))
