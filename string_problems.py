__name__ = 'B. Joel'
'''
Monday, May 15, 2023
string_problems
Python functions that manipulate strings 
'''

def count(substring, string):
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    for i in range(str_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            count += 1
    return count

def remove(substring, string):
    sub_len = len(substring)
    str_len = len(string)
    index = -1

    for i in range(str_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            index = i
            break

    if index != -1:
        return string[:index] + string[index + sub_len:]
    else:
        return string

def remove_all(substring, string):
    sub_len = len(substring)
    str_len = len(string)
    result = ""
    i = 0

    while i < str_len:
        if string[i:i + sub_len] == substring:
            i += sub_len
        else:
            result += string[i]
            i += 1
    return result

print('count("is", "Mississippi") =',count("is", "Mississippi"))
print('count("an", "banana") =',count("an", "banana"))
print('count("ana", "banana") =',count("ana", "banana"))
print('count("nana", "banana") =',count("nana", "banana"))
print('count("nanan", "banana") =',count("nanan", "banana"))
print('count("aaa", "aaaaaa") =',count("aaa", "aaaaaa"))

print("\n Remove")
print('remove("an", "banana") =',remove("an", "banana"))
print('remove("cyc", "bicycle") =',remove("cyc", "bicycle"))
print('remove("iss", "Mississippi") =',remove("iss", "Mississippi"))
print('remove ("eggs", "bicycle") =',remove("eggs", "bicycle"))

print("\n Remove all")
print('remove_all("an", "banana") =', remove_all("an", "banana"))
print('remove_all("cyc", "bicycle") =', remove_all("cyc", "bicycle"))
print('remove_all("iss", "Mississippi") =', remove_all("iss", "Mississippi"))
print('remove_all ("eggs", "bicycle") =', remove_all("eggs", "bicycle"))
print('remove_all ("elle", "ellellelle") =', remove_all("elle", "ellellelle"))
print()
