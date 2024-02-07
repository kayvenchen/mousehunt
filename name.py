'''
Answer for Question 5. Kids' Friendly.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''

# you can make more functions or global read-only variables here if you please!

'''
This part should be your solution from Assignment 1, 3. Functions.
'''
def is_valid_length(name: str) -> bool:
    '''check to see if name is between 1 and 9 characters (9 inclusive)'''
    is_valid_length = True
    if len(name) > 9 or len(name) < 1:
        is_valid_length = False
    return is_valid_length


def is_valid_start(name: str) -> bool:
    '''check if the first character of name is a alphabetical character'''
    is_valid_start = True
    if name != "":
        if name[0].isalpha() == False:
            is_valid_start = False
    return is_valid_start


def is_one_word(name: str) -> bool:
    '''check that the name is one word 
       (ie does not have spaces between, or leading/trailing spaces)'''
    is_one_word = True
    # .find() returns -1 if string searched for is not found
    if (name.find(" ") != -1 or 
        name.isspace() == True or 
        name.strip() != name):
        is_one_word = False
    return is_one_word


def is_valid_name(name: str) -> bool:
    '''check to see if all name requirements are met'''
    is_valid_name = True
    if (is_one_word(name) == False or 
        is_valid_length(name) == False or 
        is_valid_start(name) == False or
        is_profanity(name) == True):
        is_valid_name = False
    return is_valid_name


def is_profanity(word: str, database='/home/files/list.txt', 
                 records='/home/files/history.txt') -> bool:
    '''
    Checks if `word` is listed in the blacklist `database`.
    '''
    result = False
    try:
        profanity = open(database, 'r')
    except:
        print("Check directory of database!")
        return result
    i = 0
    lines = profanity.readlines()
    while i < len(lines):
        if word.strip() == lines[i].strip(): # no no word detected
            result = True
            history = open(records, 'a+')
            history.write(word + "\n")
            history.close()
            break
        i += 1
    profanity.close()
    return result


def count_occurrence(word: str, file_records="/home/files/history.txt", start_flag=True) -> int:
    '''
    Count the occurrences of `word` contained in file_records.
    '''
    count = 0
    try:
        f = open(file_records, 'r')
    except:
        print("File records not found!")
        return count
    
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if type(word) != str:
            print("First argument must be a string object!")
            break
        elif word == "":
            print("Must have at least one character in the string!")
            break
        else:
            if start_flag == False:
                if word.lower().strip() == lines[i].lower().strip():
                    count += 1
            elif start_flag == True:
                if word.lower().strip()[0] == lines[i].lower().strip()[0]:
                    count += 1
        i += 1
    f.close()
    return count


def generate_name(word: str, src="/home/files/animals.txt", 
                  past="/home/files/names.txt") -> str:
    '''
    Select a word from file `src` in sequence depending on the number of times 
    word occurs.
    '''
    new_name = "Bob"
    try:
        animals = open(src, 'r')
        past_names = open(past, 'r')
    except FileNotFoundError:
        print("Source file is not found!")
        return new_name
    if type(word) != str:
        print("First argument must be a string object!")
        return new_name
    elif word == "":
        print("Must have at least one character in the string!")
        return new_name
    
    # find all names that start with the character
    first_char = word[0].lower()
    possible_names = []
    while True:
        animal_line = animals.readline()
        if animal_line == "":
            break
        elif first_char == animal_line[0].strip().lower():
            possible_names.append(animal_line.strip().lower())


    # find used names
    used_names = []
    while True:
        past_names_lines = past_names.readline()
        if past_names_lines == "":
            break
        used_names.append(past_names_lines.strip().lower())

    # check to see which names are unused
    i = 0
    count = 0
    while i < len(used_names):
        j = 0
        while j < len(possible_names):
            if used_names[i] == possible_names[j]:
                count += 1
            j += 1
        i += 1

    new_name = possible_names[count % len(possible_names)]

    f = open(past, "a")
    f.write(new_name + "\n")
    f.close()

    return new_name


def main():
    while True:
        name = input("Check name: ")
        if name == "s":
            break
        elif is_valid_name(name) == True:
            print(f"{name} is a valid name!")
        elif is_valid_name(name) == False:
            new_name = generate_name(name)
            print(f"Your new name is: {new_name}")


if __name__ == "__main__":
    main()

