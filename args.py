def create_args(*args):
   print(args)
#define args
a = 1
b = ['thin', 'tall']
c = {"name": 'value'}


print("+++++++++++_________________++++++++++++")
#takes no positional args **kwargs, args must be a keyword like keywalue of a dictionary(key=word)
def collect(**kwargs):
   print(kwargs)

#call function collect()
collect(a=300, b=400)

print("+++++++__________________________+++++++++++++")
def collect_args(b, e, f, c = 512, *args, **kwargs):
   print (f, b, c, e)
   print("+++++++++")
   print (args)
   print("+++++++++")
   print (kwargs)

collect_args(100, 200, 340, 500, 400, 1000, first = 450, second = 600)

