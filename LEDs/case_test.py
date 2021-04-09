def one():
    return "January"
 
def two():
    return "February"
 
def three():
    return "March"
 
def four():
    return "April"
 
def five():
    return "May"
 
def six():
    return "June"
 
def seven():
    return "July"
 
def eight():
    return "August"
 
def nine():
    return "September"
 
def ten():
    print("October")
 
def eleven():
    return "November"
 
def twelve():
    return "December"
 
 

# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        'a': ten,
        'b': "one",
        'c': "two",
    }
  
    # get() method of dictionary data type returns 
    # value of passed argument if it is present 
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument,"nothing")
  
# Driver program
if __name__ == "__main__":
    argument='a'
    print (numbers_to_strings(argument))