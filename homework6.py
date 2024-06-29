my_dict={"Ivan":2003,"Inna":1998, "Irina":2000,"Anna":2005}
print("Dict: " , my_dict)
print("Existing value: ", my_dict["Ivan"])
print("Not existing value: ", my_dict.get("Masha"))
my_dict.update({"Olga":1988, "Vasya": 1990})
print("Modified_dict: " , my_dict)
print("Deleted value: " , my_dict ["Inna"])
del my_dict["Inna"]
print("Modified_dict2: " , my_dict)

my_set= {1,2,3,1,2, "Малина", 3.16, 3.16}
print("Set: ", my_set)
my_set.add( (7,8,9))
my_set.add( "Яблоко")
my_set.discard( 3.16)
print("Modified set: ", my_set)