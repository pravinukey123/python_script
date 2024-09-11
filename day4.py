# Dictionary & Sets

# info = {
#     "key" : "value",
#     "subjects" : ["python", "C", "Java"],
#     "age" : 35, 
#     "name" : "Pravin",
# }

# info["name"] = "Pappu" #overwrite
# info["surname"] = "ukey"
# print(info)

# null_dict = {}
# null_dict["name"] = "apnacollage"
# print(null_dict)

student = {
    "name" : "rahul kumar",
    "subjects" :{
        "phy" : 97,
        "chem" : 99,
        "bio" : 90,
    }
}
#Nested Dictionary
# print(student["subjects"] ["chem"])

# print(len(student))
# print(list(student.keys()))

# print(list(student.values()))
# pairs = list((student.items()))
#print(student["subjects"]["phy"])

# print(student["name"])
# print(student.get("name"))

# student.update({"city" : "delhi"})
# new_dict = {"city" : "Nagpur", "food" : "Pualv"}
# student.update(new_dict)

# print(student)

#Set in Python

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add((1,2,3))
# collection.add("apna collage")
# collection.clear()

# print(collection)
# print(len(collection))

# Set Methods

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) #It will remove common of both set 
# print(set1.intersection(set2)) #It will shows the common number of both sets

# guide = {
    
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal",
# }
# print(guide)

# subjects = {
#     "english", "marathi", "hindi", "telgu", "tamil",
#     "hindi", "marathi", "english",
#     }
# print(len(subjects))



# marks = {}

# x = int(input("marks of chem : "))
# marks.update({"chem" : x})

# y = int((input("marksof math: " )))
# marks.update({"math" : y})

# print(marks)

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)

