mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

try:
    print(mydict["lastname"])
except:
    print("Error")