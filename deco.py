def students(var):
    def bio(*args, **kwargs):
        print(f"Student informaation portal")
        result = var(*args, **kwargs)
        print(f"student_info:\n FirstName:{args[0]},\n lastname: {args[1]} \n Course: {kwargs['Course']}")
        return result
    return bio

@students
def info(*args, **kwargs):
    print(f"Positional arguments: {args} \n Keyword arguments: {kwargs}")

@students
def skills(*args, **kwargs):
    print(f"Skill: {kwargs['skill']} \n Level: {kwargs["level"]}")
#names = animlas(names)