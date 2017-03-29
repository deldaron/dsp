# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are mutable while tuples are immutable. This means lists have append and extend methods while tuples don't.  Dictionary keys need to be immutable data types so tuples will work while lists will not.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists are both collections of objects.  Lists are ordered, mutable, and can contain duplicates (since the number 5 at index 0 and index 3 can be accessed/treated differently by index).  Sets are unordered and do not allow for duplicates. Both sets and lists are themselves mutable, but the objects contained in a set must be immutable. 

>> Sets can be used for removing duplicates. Sets also support mathematical operations such as union and intersection which can be particularly useful for data manipulation (e.g. isolating a conditional space). 

>> Lists are ordered and allow for duplicates.  This can be useful for counting frequencies using list_name.count(x). 

>> When searching for membership of an element in a list or a set, sets perform faster than lists.  This is because sets use hash tables which store the location of the element in memory. This means that, when searching for membership, only one hash position needs to be checked. Lists on the otherhand must be iterated over until the element is found or not and, especially since lists can contain duplicates, this can be a time consuming process. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Pythons `lambda` is an anonymous single expression function. This allows programmers to nest local functions without explicity    
>>defining and calling them. Thus the following two sets of code have the same result:  
  
```Python
def square(x):  
  return x ** 2  
print(square(2))

square = lambda x: x ** 2  
print(square(2))
```  
>> Even though only the first set of code used the `def` keyword, both sets created a function that multiplies the input by itself  
  
>> Using `lambda` as the `key` in `sorted` allows for sorting in unique ways.  Let's say you had a list of positive and negative numbers  
>> and you wanted to sort them according to their absolute values without changing the value itself. This can be acheived as such:
```Python
example_list = [3,1,-5,2,6,-10,9,-4]  
print(sorted(example_list, key = lambda n: abs(n)))  

#returns [1, 2, 3, -4, -5, 6, 9, -10]
```

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are convenient ways to create lists using computations or expressions. One could create a list of all numbers between one and ten sqaured by iterating over the range 0, 10 and appending each number squared to a blank list.  Alternatively, one could use list comprehension to do this in one line:
```Python
#The first option:
new_list = []
for n in range(11):
  new_list.append(n**2)

#Using list comprehension:
new_list = [n**2 for n in range(11)]
```
  
>>Both iterations of new_list are the same, but using list comprehension allowed for more concise, cleaner code.  This is especially useful for more complex uses than squaring a number.  
  
>>`Map` applies a function over a set of iterables and thus is similar to list comprehension, but less exhaustive (list comprehension is the most exhaustive of the three, since conditionals and functions can be passed into set comprehension). Also, in Python 3 using `map` creates a `map` object instead of a list which must be converted to a list if it needs to be printed, but can stay as a `map` object for iterating over.  

```Python
#Example of using map():
map(lambda n: n**2, range(10))
#This creates a map object with the numbers 0 to 9 (inclusive) squared which can be stored as a variable.
```

>>`Filter` is similar to `map`, but the function passed into `filter` should return a `boolean`. From this `filter` will only add elements to a `list` for which the resulting `boolean` is `True`. `Filter` functions in a similar way to `map` in Python 3 producing a `filter` object.  

```Python
#Example of using filter():
filter(lambda n: n % 2 == 0, range(21)
#This creates a filter object containing all even numbers between 0 and 20 (inclusive).
```
>>`Set` and `dictionary` comprehensions function similarly to `list` comprehensions except they produce `sets` and `dictionarys` respectively. 

```Python
#Example of set comprehension:
set_comp = set([n**2 for n in range(11)])

#Example of dictionary comprehension:
dict_comp = {(k,v) for (k,v) in zip(range(3), ['a','b','c'])}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





