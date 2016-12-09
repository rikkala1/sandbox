__author__ = 'jc446932'
valid = False
while not valid:
  name = input("Enter your name:")
  if name !="" or not name.isspace():
      valid = True

print(valid)



l = len(name)
for i in range(0, l, 2):
    print(name[i])