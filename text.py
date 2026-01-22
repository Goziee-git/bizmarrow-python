


#TUple

var_tuple = ("string", 2, [])
dir(var_tuple)

variable_dict = {"keys": "value",
                  "name": "prospa",
                  "age": 12,
                  "school": "vaatia college"}


var_list = ["string", 1, 2.000, {"name": "prospa"}, (1, 3), [1, "string"]]



class Person:
   def __init__(ref_name, firstname, lastname, country):
      ref_name.firstname = firstname
      ref_name.lastname = lastname
      ref_name.country = country
   
   def fullname(ref_name):
      print("my name is " + ref_name.firstname + " " + ref_name.lastname)

   def bio(ref_name):
      print("My name is " + ref_name.firstname + " " + ref_name.lastname +  "i am from " + ref_name.country)

student = Person("prospa", "smith", "Nigeria")
uf_student = student.firstname.upper()
ul_student = student.lastname.upper()
uc_student = student.country.upper()

print("My firstname is " + uf_student + " " + "my last name is " + ul_student + " " +  "i am from " + uc_student)
