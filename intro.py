print("Hello World")
# console.log("Hello World");

# Variables
name = "dani"
age= 138
found = False
name = 12
name = True
# let name = "dani"
# const name = "dani"
print(name)

# if/else statement
if age<100:
    print("don't worry your not that old")
elif age==100:
    print("Whoa, you're kinda up there")
else: 
    print("Well, it seems you're definetly up there")

#functions
def say_Hello():
    print ("Hello there")
    # function say_Hello(){}

#call functions
say_Hello()

print("my age is" + str(age) + "years old")

# array -- list
colors = ["yellow","green","blue"]
print(colors)

# add -- append
colors.append("pink")
print(colors)
# remove -- remove
colors.remove("yellow")
print(colors)
# remove using the index
colors.pop(0)
print(colors)
# remove by slice by index
del colors[1]
print(colors)

print(colors[1])

# for loops
for color in colors:
    print(x)


# for(i=0;i<colors.length;i++){
# let temp = i[0];
# console.log(temp)
# }