# import pandas as pd
# # Q1. Create variables for:

# # name
# # age
# # city
# # percentage
# # is_student
# # name="Tirth"
# # age=20
# # city="Ahmedabad"
# # percentage=80
# # is_student="Yes"
# # print(name)
# # print(age)
# # print(city)
# # print(percentage)
# # print(is_student)

# # Print all of them.

# # Q2. Check the data type of each variable using type().
# # print(type(name))
# # print(type(age))
# # print(type(city))
# # print(type(percentage))
# # print(type(is_student))

# # Q3. Create two numbers and perform:
# # a=10
# # b=20
# # # addition
# # print(a+b)
# # # subtraction
# # print(a-b)
# # # multiplication
# # print(a*b)
# # # division
# # print(a/b)
# # # modulus
# # print(a%b)
# # # power
# # print(a**2)
# # 2️⃣ Strings
# # Learn
# name = "Tirth Dabhi"
# m="t"

# # print(name.upper())
# # print(name.lower())
# # print(len(name))

# # Learn:

# # indexing
# # print(name[0])
# # # slicing
# # print(name[0:3])
# # # upper()
# # print(name.upper())
# # # lower()
# # print(name.lower())
# # # strip()
# # print(name.strip())
# # # replace()
# # print(name.replace("Tirth","Arav"))
# # # split()
# # print(name.split())
# # # join()
# # print(join(name,m))
# # 📝 Questions

# # Q4. Given:

# text = "Python Data Engineering"

# # # Find:

# # # length
# # print(len(text))
# # # first character
# # print(text[0])
# # # last character
# # print(text[-1])
# # # first 6 characters
# # print(text[0:6])

# # Q5. Convert the string to uppercase and lowercase.
# # abc="tefr"
# # print(abc.upper())
# # print(abc.lower())
# # Q6. Replace "Python" with "AI".
# # print(text.replace("Python","AI"))
# # Q7. Split:

# # "Python,SQL,Pandas,Spark"

# # into a list.

# # 3️⃣ Lists ⭐
# # Learn
# # numbers = [10, 20, 30, 40, 50]

# # # Practice:

# # # append()
# # numbers.append(90)
# # print(numbers)
# # # insert()
# # numbers.insert(2,250)
# # print(numbers)
# # # remove()
# # numbers.remove(30)
# # print(numbers)
# # # pop()
# # numbers.pop(4)
# # print(numbers)
# # # sort()
# # numbers.sort()
# # print(numbers)
# # # reverse()
# # numbers.reverse()
# # print(numbers)
# # # len()
# # print(len(numbers))
# # 📝 Questions

# # Q8. Create a list of 10 numbers.

# # Find:
# numbers = [10, 20, 30, 40, 50,60,70,80,90,100]
# # maximum
# print(max(numbers))
# # minimum
# print(min(numbers))
# # sum
# print(sum(numbers))
# # average
# # print(pd.avg(numbers))

# # Q9. Add a new number to the list.
# numbers.append(1000)
# print(numbers)

# # Q10. Remove a number from the list.
# numbers.remove(20)
# print(numbers)


# Q11. Sort the list ascending and descending.
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# Q12. Create a list of student marks and print students having marks greater than 75.

# 4️⃣ Tuples
# Learn
# student = ("Tirth", 22, 85)

# Understand:

# tuple indexing
# print(student[0])
# unpacking
# why tuples are immutable
# 📝 Questions

# Q13. Create a tuple containing:

# name
# age
# city
# marks
# t=("Tirth",20,"Ahmedabad",100)
# print(t)
# Print each value.

# Q14. Unpack the tuple into four variables.
# print(t.split())

# Q15. Explain why you cannot modify a tuple.

# 5️⃣ Sets
# Learn
numbers = {1, 2, 3, 3, 4}

# Understand that duplicates are removed.

# Learn:

# add()

# numbers.add(5)
# print(numbers)
# # # remove()
# numbers.remove(2)
# print(numbers)
# # union()

# # 📝 Questions

# Q16.

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # Find:

# # union
# print(a.union(b))
# # intersection
# print(a.intersection(b))
# # difference
# print(a.difference(b))
# print(b.difference(a))

# Q17. Remove duplicate values from:

numbers = [10, 20, 10, 30, 20, 40, 30]
# print()
# 6️⃣ Dictionaries ⭐⭐⭐

# This is very important for Data Engineering.

# Learn
# student = {
#     "name": "Tirth",
#     "age": 22,
#     "marks": 85
# }

# Learn:

# keys()
# values()
# items()
# get()
# update()
# 📝 Questions

# Q18. Create a dictionary containing:

# name
# age
# email
# city
# course
t={
    'name':'Tirth',
    'age':20,
    'email':'tirthdabhi221@gmail.com',
    'city':'Ahmedabad',
    'course':'IMSC-IT'
}
# print(t)
# Print all values.

# Q19. Add:

# "marks": 85
# print(t.update('Marks',70))

# Q20. Change the marks to 90.