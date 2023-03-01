name = input("Tell me your name: ")
print("Hello, %s" % name)
itIsText = True

while itIsText:
    value = int(input("What is your age? Numbers only"))
    itIsText = not itIsText

if not itIsText:
    print("haha i fucking hate python")
