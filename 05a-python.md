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

>> REPLACE THIS TEXT WITH YOUR RESPONSE

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





