# Task 1

def hello():
    return "Hello!"

# Task 2

def greet(name):
    return f"Hello, {name}!"

# Task 3

def calc(a, b, c="multiply"):
    try:
        if c=="add":
            return a+b
        elif c=="multiply":
            return a*b
        elif c=="subtract":
            return a-b
        elif c=="divide":
            return a/b
        elif c=="modulo":
            return a%b
        elif c=="int_divide":
            return a//b
        elif c=="power":
            return a**b    
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
    
print (calc("1","0","divide"))

# Task 4

def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "str":
            return str(value)
        elif type == "float":
            return float(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
print(data_type_conversion(5, "float"))


# Task 5

def grade(*args):
    if len(args) == 0:
        return "Invalid data was provided."
    
    try: 
        average = sum(args)/len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."
    

    # Task 6

def repeat(string, count):
    try:
        result = ""
        for i in range(count):
            result += string
        return result
    except:
        return "Invalid data."

    # Task 7

def student_scores(positional, **kwargs):
    try:    
        if positional == "best":
            name, score = "", 0
            for key, value in kwargs.items():
                if value > score:
                    name, score = key, value
            return name
        elif positional == "mean":
            return sum(kwargs.values())/len(kwargs)
        else:
            return f"Your {positional} was not accepted" 
    except TypeError: 
        return "Invalid"
    
    
   # Task 8
   
def titleize(string):
    try: 
        little_words= ["a", "on", "an", "the", "of", "and", "is", "in"]
        words = string.lower().split()
        
        for i, word in enumerate (words):
            if i == 0 or i == len(words) -1 or word not in little_words:
                words[i] = word.capitalize()
            else: 
                words[i] = word.lower()
                
        return " ".join(words);
            
    except TypeError:
        return "Invalid"


# Task 9

def hangman(secret, guess):
    try: 
        guessed_word = ""
        for letter in secret
            if letter in guess:
                guessed_word += letter
            else:
                guessed_word += "_"
        return guessed_word
    except: 
        return "Invalid"
        
        
        
       
            
#Task 10

def pig_latin(sentence):
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    
    try: 
        words = sentence.lower().split()
        
        for word in words:
            if word[0] in vowels:
                result.append(word+"ay")
            elif word.startswith("qu"):
                result.append(word[2:]+"quay")
            elif word[1:3] == "qu":
                result.append(word[3:] + word[:3] + "ay")
            else:
                for i, char in enumerate(word):
                    if char in vowels:
                        result.append(word[i:]+word[:i]+"ay")
                        break
                    else:
                        result.append(word+"ay")
                        
        return " ".join(result)
    
    except Exception as e:
        return f"An error occured: {str(e)}"

print(pig_latin("hello world"))