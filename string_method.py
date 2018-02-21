#@ 1.concatination
# s = "hello"
# s1 = " world"
# print(s+s1)

#@ 2. String Replication / Multiplication (*)

# s = "hello "
# print(s * 5)

#@ 3. lenth (len)

# s = "Hello"
# print(len(s))

# *********************String Method***********************#

# @ 1. Capitalize()

# s = "hello"
# print(s.capitalize())

# @ 2. count(substring)
#it shows How maney Times Char is repited

# s = "hello"
# print(s.count('l'))

# @ 3. endswith

# s = 'hello'
# print(s.endswith('llo'))
# print(s.endswith("he"))

# @ 4.Find (substring)

# s = "hello"
# print(s.find('h'))

# @ 5.Index(substring)
# s = "Hello"
# print(s.index("o"))

# @ 6.format(*args, **kwargs)

# sub = "Python"
# marks = 80
# # s = ("Subject %s and marks is %d")%(sub, marks)
# s = ("Subject {} and marks is {}").format(sub, marks)
# print(s)


# @ 7.isalnum()

# a = "abc" #true
# b = "123" #true
# c = "abc@123" #false
#
# print(a.isalnum(), b.isalnum(), c.isalnum())

# @ 8. isalpha()

# a = "ABC"
# b = "123"
# print(a.isalpha(), b.isalpha())


# @ 9. isdecimal()

# a = "abc"
# b = "123"
# c = "12.0"
# print(a.isdecimal(), b.isdecimal(), c.isdecimal())


# @ 10. isdigit()


# a = "abc"
# b = "123"
# c = "abc123"
# print(a.isdigit(), b.isdigit(), c.isdigit())


# @ 11. islower()

# a = "ABC"
# c = "abc"
# b = "AbC"
# print(a.islower(), b.islower(), c.islower())


# @ 12. isupper()

# a = "ABC"
# c = "abc"
# b = "AbC"
# print(a.isupper(), b.isupper(), c.isupper())


# @ 13. isspace()
# a = "hello World"
# b = "    "
# print(a.isspace(), b.isspace())

# @ 14. istitle() # needs each and every words first letter is Capital

# a = "this is title"
# b = "This is title"
# c = "This Is Title"
# print(a.istitle(), b.istitle(), c.istitle())

# @ 15. lstrip()

# a = "sssssssssssssssssssangram"
# b = "       sangram" #with blank space
#
# print(a.lstrip(), b.lstrip())

# @ 16. rstrip()

# a = "sangram                    "#with blank space
# b = "sangram"
# print(a.rstrip(), b.rstrip())


# @ 17. strip()

# a = "        sangram       "
# b = "sangram"
# print(a.strip(), b.strip())


# @ 18. replace(old string, new string, count)

# a = "sangrak"
# print(a.replace('k', 'm', 1))

# @ 19. split()

# a = "hello, sangram welcome to the world of pyton"
# print(a.split())

#
# a = "You are Invited"
# a.split()
# l = a.split()
# l[::-1]
# " ".join(l)
# l[::-1]
# " ".join(l)
# q = l [::-1]
# " ".join(q)
# print(q)

#  @ 19. join(seq)

# a = "hello"
# b = "world"


# @ 20. title()

# s = "hello, sangram welcome to the world of pyton"
# print(s.title())

# # @  21. join() *********************************InComplete********************
# a = "hello, sangram welcome to the world of pyton"
# b = " ".join(a)
# print(b)


# @ 21. title()

# a = 'hello, sangram welcome to the world of pyton'
# print(a.title())


# @ 22. swapcase()

# a = "sangram"
# b = "Sangram"
# c = "SANGRAM"
# print(a.swapcase(), b.swapcase(), c.swapcase())


# @ 23. lower()
# a = "SANGRAM"
# b = "Sangram"
# c = "sangram"
# print(a.lower(), b.lower(), c.lower())




# @ 23. upper()
# a = "SANGRAM"
# b = "Sangram"
# c = "sangram"
# print(a.upper(), b.upper(), c.upper())





subjects = ('Python', 'Coding', 'Tips')

for i, subject in enumerate(subjects):
    print(i, subject)
