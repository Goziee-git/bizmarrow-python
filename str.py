sent = "  happy holidays to you and your family  "
sep = "-"
#handling strings
#methods
#split(), rsplit() - takes a seperator and an interger representing the number of times to split a string
sent.split() #returns a list with each word as a seperate string
sent.rsplit(' ', 2) #returns a list with the string split according to parameter in rstrip
sent.lstrip() #strip white spaces on the left
sent.rstrip() #strip whitespaces on the right of the string
sent.partition("sep") #sep is the seperator sent.partition(' ') - returns a tuple of (head, sep, tail) otherwise it returns 
#the string an two other empty strings)
sep.join(sent) #more efficient than the concatenation, 
sent.capitalize()
sent.lower()
sent.upper()
sent.title()
sent.center(32,"#") # string.center(width[, fillchar])
sent.ljust(32,"*")
sent.rjust(32,"%")
sent.zfill(32) #pads the width with zero
sent.expandtabs()
#special formatting using string.format()
string = f"how {0} you {2}, my {text}"
string.format("are", "doing", text = "brother")
#also {!s} type string {!r} type repr
#also {0!s:*^3} - means the variable with positional value of 0, is a sting type, ^ aligns to the center
#and padded with three width
#string.find(sub[,start[,end]])
sent.find("hol",5,-1)
sent.rfind("hol",7,-1)
sent.index("e",0,-1) #string.index(sub[,start[,end]]) raises a ValueError when the index of the substring is not found
sent.rindex("o",0,-1) #search for substring form the end
sent.count("s",0, -1)
sent.endswith("s",0,-1)

