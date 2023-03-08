age =  18

# if age > 18:
#     adult = True
# else:
#     adult = False

 
 #allows testing a condition in a single line 
 # replacing the multiline if-else making the code compact
adult = True if age >= 18 else False

print("you are an adult" if adult else "you are not an adult")

# if adult:
#     print("you are ADULT")
# else:
#     print("youre not ADULT")


number = 10

print("this number is large" if  number > 1000 else "its not as large" if number > 100 else "this number is boof" if number < 100 else "were done")