[The Complete Python Bootcamp From Zero to Hero in Python](https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388530#overview)

### Resources
Resources for More Basic Practice

Basic Practice: http://codingbat.com/python

More Mathematical (and Harder) Practice: https://projecteuler.net/archives

List of Practice Problems: http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems: https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and tough problems (Not for beginners but still interesting): http://www.pythonchallenge.com/

### Sets
sets are are a container of unique values. Notice that values are not duplicated in the below examples.
```
myset=set()
type(myset)
<class 'set'>
myset.add(1)
myset
{1}
myset.add(2)
myset
{1, 2}
myset.add(2)
myset
{1, 2}
mylist=[1,1,1,1,3,3,3,3,3,4,4,8,4,5,5,6,9,7,7,7,0]
set(mylist)
{0, 1, 3, 4, 5, 6, 7, 8, 9}
```

### Booleans
Operator to represent True or False statements.

```>>> a in mylist
False
>>> 1 in mylist
True
>>> 1 in myset
True
>>> 4 in myset
False
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> True
True
>>> type(True)
<class 'bool'>
>>> 1>2
False
>>> 1==1
True
```
#### None Type
```
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> b = None
>>> b
>>> type(b)
<class 'NoneType'>
```

### File Operations
#### Character	Meaning
- 'r'	open for reading (default)
- 'w'	open for writing, truncating the file first
- 'x'	create a new file and open it for writing
- 'a'	open for writing, appending to the end of the file if it exists
- 'b'	binary mode
- 't'	text mode (default)
- '+'	open a disk file for updating (reading and writing)
- 'U'	universal newline mode (deprecated)

The default mode is 'rt' (open for reading text). For binary random access, the mode 'w+b' opens and truncates the file to 0 bytes, while 'r+b' opens the file without truncation. The 'x' mode implies 'w' and raises an FileExistsError if the file already exists.

#### Reading a file
```
>>> with open(os.getcwd()+'/myfile.txt') as my_new_file:
...     contents=my_new_file.read()
... 
>>> contents
'Hello this is a text file\nthis is the second line\nthis is the third line'
```
#### Writing a file
```
>>> with open('myfile2.txt',mode='x') as my_new_file:
...     my_new_file.writelines('ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'myfile2.txt'
>>> with open('myfile2.txt',mode='a') as my_new_file:
...     my_new_file.writelines('ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')
... 
>>> with open('myfile2.txt',mode='a') as my_new_file:
...     my_new_file.writelines('\nFOUR ON FOURTH')
```

### Quick Recap of Data Structures
```
>>> 27**(1/3)
3.0
>>> 27**(1/2)
5.196152422706632
>>> 25**(1/2)
5.0
>>> 3**3
27
>>> s[::-1]
'olleh'
>>> s[::2]
'hlo'
>>> s[::-2]
'olh'
>>> s[::-3]
'oe'
>>> s[::-5]
'o'
>>> [0]*3
[0, 0, 0]
>>> list3=[1,2,[3,4,'hello']]
>>> list3=[1,2,[3,4,'hello']]
>>> list3[2][2]
'hello'
>>> list3[2][2]='goodbye'
>>> list[3]
list[3]
>>> list3
[1, 2, [3, 4, 'goodbye']]
>>> list4=[5,3,7,1,9,32]
>>> list4.sort()
>>> list4
[1, 3, 5, 7, 9, 32]
>>> list4=[5,3,7,1,9,32]
>>> sorted(list4)
[1, 3, 5, 7, 9, 32]
>>> list4
[5, 3, 7, 1, 9, 32]
>>> d={'simple_key':'hello'}
>>> d['simple_key']
'hello'
>>> d={'k1':{'k2':'hello'}}
>>> d['k1']['k2']
'hello'
>>> d={'k1':[{'nest_key':['this is deep',['hello']]}]}
>>> d['k1'][0]['nest_key'][1][0]
'hello'
```

### Methods 
