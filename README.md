# My Own Custom Interpreted Language

This is an interpreted language made in python.

**NOTE: As per now the there must be 1 space between each token in the language.**


## Datatypes available:
1. int
2. float
3. string
4. bool

### Comments:
A comment is decalred using ```'``` as a start symbol.
```vb

' This is a comment

```

### print and println:
These commands are used to print an output to the terminal screen.
```vb

print "Hello World"
println "Hello World"

z = 10 + 1

println z

```

### input:
This command is used to take input of a particular data type and the input can be stored in a variable.

syntax and example
```vb
' <variable_name> = input <datatype> <prompt_string> 
num = input int "Enter a num: "
println num
```

### if - endif:
This is used to implement if else logic

syntax and example
```vb
age = input int "Enter your age: "

if age > 18
  println "The person can vote."
endif
```
**if - else - endif not implemted yet**

### while loop:
This is used to implement while loop logic

syntax and example
```vb
n = input int "Enter a number: "
r = 1

while n >= 1
  r = r * n
  n = n - 1
end

print "Factorial is: "
print r

```


---

## Disclaimer

1. **if - else - endif not implemted yet**
2. **As per now the there must be 1 space between each token in the language.**
3. **Block level variable declaration not available yet, so all variables should declared in global scope.**


Made with ❤️ by Vishnu Prasad Korada