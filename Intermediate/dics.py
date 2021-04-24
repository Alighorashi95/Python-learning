mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

mydict_cpy = mydict.copy()


mydict_cpy["email"] = "max@xyz.com"
print(mydict)
print(mydict_cpy)