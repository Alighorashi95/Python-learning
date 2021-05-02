from itertools import groupby
persons = [{"name" : "Tim", "age" : 25}, {"name" : "Dan", "age" : 25},
           {"name" : "Lisa", "age" : 27}, {"name" : "Claire", "age" : 28}]
a = [1, 2, 3, 4]
group_obj = groupby(persons, key= lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))