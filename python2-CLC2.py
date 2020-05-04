#!/usr/bin/python3


"""
    Name: Spencer Goldwin
    Date: 04/22/2020
    Course: CIT 29900 
    Description: Python homework 2 -- covering types, operators, loops, collections, and classes
    Points: ?/44

    Instructions: Complete each numbered task below. Use the space below each task to complete your work.
                  Most of the tasks will require multiple lines of code so adjust your spacing as needed.
                  Please be sure to leave at least 1 empty line above and below each numbered task.

                  This assignment is worth 44 points broken down as 2 points per task and 10 points simply
                  by submitting a completed script that runs without needing to be modified/corrected.
"""


#--------------------------------------------------------------------------------------------------------------


import nmap
import pprint
import nmap
import pprint

video_games = ("Fallout", "Skyrim", "Zelda", "Fortnite", "WoW", "Final Fantasy", "Halo", "Animal Crossing")
view_askew = {"Jay", "Silent Bob", "Randal", "Dante", "Holden", "Banky", "Schooner"}
villians = ["Darth Vader", "Hans Gruber", "Voldemort", "Sauron", "Thanos", "Rick Astley"]
best_sellers = {"Douglas Adams": "The Hitchhiker's Guide to the Galaxy", 
                "Robert Jordan": "The Wheel of Time",
                "J. R. R. Toklien": "The Hobbit",
                "Brent Weeks": "The Black Prism",
                "Brandon Sanderson": "The Way Of Kings",
                "Winnie the Pooh": "How To Get Away With Murder"}
nm = nmap.PortScanner()
pp = pprint.PrettyPrinter(indent=4)

#--------------------------------------------------------------------------------------------------------------


### 1. Create 2 variables called fnamdfe and lname, then assign them your first and last names (strings).
fname = "Spencer"
lname = "Goldwin"


### 2. Write a print statement that concatenates and prints your first and last names with a space between them.
print(fname,"",lname)


### 3. Create a function that accepts 2 arguments. Inside the function, use a print statement to print the
###    sum of the 2 arguments.
def add(x = 0,y = 0):
    result = x + y
    return result
print(add())

### 4. Call the function above and pass it 2 numbers -- 1 whole number (integer) and 1 decimal number (float).

def add(x,y):
    result = x + y
    return result
print(add(5,2.5))

### 5. Create another function, but this time make it accept 1 argument. Have this function square the value
###    that passed into it and then return it (not print it).

def square(x):
    result = x * x
    return result


### 6. Call the function above, pass it an integer or float, and then print its the returned value.
def square(x):
    result = x * x
    return result

print(square(6))


### 7. Create a new variable and cast its value, the integer 42, into a string. Print the variable contents.
num1 = '42'
print(num1)


### 8. Prove that the variable above was correctly cast to a string by using the type() function. Print this
###    result to the screen in the same statement.
print('Type of num1 is :', type(num1))


### 9. Create a function that accepts 1 argument. Inside this function write an if statement that compares
###    the length of the string "Python is a lot of fun" against the argument. If the argument is larger,
###    return the boolean true. Otherwise, return false.
def compare (narg):
   str_leng = len("python is a lot of fun")
   if  narg > str_leng:
       return True
   else:
       return False


### 10. Call the function above and pass it an integer. Print the result.

def compare (narg):
   str_leng = len("python is a lot of fun")
   if ( narg > str_leng):
       return True
   else:
       return False

print(compare(32))

### 11. Use a single print statement to print the data types of the 4 collection objects at the top of this
###     script. Those objects are videos_games, view_askew, villians, and best_sellers.
print(type(video_games), type(view_askew), type(villians), type(best_sellers))


### 12. Create a while loop that prints each item inside the object video_games so long as the length of
###     the object is less than or equal to a new counter that you initialize outside the loop (which you
###     must decrement inside the loop).


### 13. Use one of the methods to remove "Rick Astley" from the villians object. Then use a different method
###     to remove "Schooner" from the view_askew object. In separate print statements, print each of the
###     objects to show that the items have been removed.
villians.remove("Rick Astley")
print(villians)


### 14. Use a for loop to loop through each item in the best_sellers object. Print both the key and
###     the value for each item.

for x, y in best_sellers.items():
    print(x, y)


### 15. Near the top of this script, nmap and pprint have been imported. Several lines below, a class from each
###     module has been instantiated (PortScanner and PrettyPrinter) resulting in the nm and pp objects. These
###     items can work together, but must be used in a specific order. First, use the nmap scan method to scan
###     your localhost and port 22 by passing the arguments 'localhost' and '22' (both strings) into the scan
###     method (i.e., call the nm object and use the scan method that's part of this object).
nm.scan('localhost','22')




### 16. As a point of reference, you're now going to print the results of the scan. The nmap scan results are
###     nested Python objects. For this example, you're going to print the results of the single host and port
###     scan you initiated above. To do that, you must print the nm object at the index of '127.0.0.1' which
###     is the IP address for localhost (the loopback address). You'll do this using [] to reference the index.
print(nm(['127.0.0.1'])


### 17. Lastly, the printed scan results above come out as a heap of information that's not very attractive. Use
###     the pprint method of the pp object to prettify the scan results. (Hint: replace your print method with
###     the pp.pprint() method. This will give you a much cleaner view of the nest object types inside the nmap
###     scan results so that you can figure out how to work with that data.
pp.pprint(nm(['127.0.0.1'])