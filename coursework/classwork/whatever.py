# Defines a "repeat" function that takes 2 arguments
def repeat(s, exclaim):
    '''
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    '''
    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result

# String literals
s = 'hi'
print s[1] ## i
print len(s) ## 2
print s + ' there' ## hi there

pi = 3.14
##test = 'The value of pi is ' + pi ## NO, does not work
text = 'The value of pi is ' + str(pi) ## yes

## String Methods
s.lower(), s.upper() # -- returns the lowercase or uppercase V of the String
s.strip() #-- returns a string with whitespace removed from the start and end
s.startswith('other'), s.endswith('other') # -- tests if the string starts or ends with the given other string
s.find('other') #-- searches for the given other string
#returns the first index where it begins or -1 if not found
s.replace(old, new) #-- returns a string where all occurences of old have
# been replaced by new
s.split('delim') #--
s.join(iterable) #-- joins the elements in the given list

#for and in
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print sum ##0

lst = ['fidelia', 'obi', 'uchenna']
if 'uchenna' in lst:
    print("OKAY")

for i in range(100):
    print i
#while loop
# while loop gives you total control over the index numbers
## Access every 3rd element in a list
i = 0
while i < len(a):
    print a[i]
    i += 3

## List Methods
list.append() #add single elements to the end of the list while changing the original
list.insert(index, object) #-- inserts the element at the given index
list.extend(iterable)
list.index()#-- searches for the given element and returns its index
list.remove()#-- searches for the first instance and removes it (throws valueError if not present)
list.sort()# doesn't returns
list.reverse()#reverses the list in place (does not return it)
list.pop()# removes and returns the element at the given index

#Python Sorting
#sorted function takes a list and sorts it in order but doesn't change the list
a = [5, 1, 4, 3]
print sorted(a)
print a


#Tuples
tuple = (1, 2, 'hi')
print len(tuple)
print tuple[2]
tuple[2] = 'bye' ## NO, tuples cannot be changed
tuple = (1, 2, 'bye') ## this works

#List Comprehesion is a way to write an expression that expands to whole list
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ] ##[1, 4, 9, 16]

#strings
strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

# Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2] ## [2, 1]
## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ f.upper() for f in fruits if 'a' in f]

##Python Dict and file
# dict is a key/value hash table
#-- looking up or setting a value uses square brackets
## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

#iterating through a dictionary
## Methods
dict.keys(), dict.values(), dict.items() ## returns a list of (key, value) tuples
for key in dict: print key

for key in dict.keys(): print key

print dict.keys()
print dict.values()

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print key, dict[key]

## .items() is the dict expressed as (key, value) tuples
  print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]


## Regular Expresions
##Regular expressions are used for matching text patterns.
'''
    '\d' = 0-9
    '\d\w' = 0s or 1f or 4n
    '3n'
    '4m'
    '6g'
    if '6g' in whatever:
        do something
    if '4m' in whatever:
        do something
    if '\d\w' in whatever:
        do something
    ''
'''
