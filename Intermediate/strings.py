
my_list = ["a"] * 6
print(my_list)
# bad
my_string = ""
for i in my_list:
    my_string += i
print(my_string)

#good
my_string = "".join(my_list)
print(my_string)