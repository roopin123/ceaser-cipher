print("enter 0 to exit\nenter 1 for encription \nenter 2 for decryption")
while True:
  k = int(input("Enter the key :"))
  if k == 1:
    c = str(input("word to be encoded :"))
    a = ''
    s = int(input("shift value :")) % 26
    for i in c:
      i = ord(i)
      if i + s > 122 and (i <= 122 and i >= 97):
        a = a + chr((i + s - 96) % 26 + 96)
      elif i + s > 90 and (i <= 90 and i >= 65):
        a = a + chr((i + s - 64) % 26 + 64)

      else:
        a = a + chr(i + s)
    print(a)

  elif k == 2:
    c = str(input("word to be decoded :"))
    a = ''
    s = int(input("shift value :")) % 26
    for i in c:
      i = ord(i)
      if i - s < 97 and (i <= 122 and i >= 97):
        a = a + chr(i - s + 26)
      elif i - s < 65 and (i <= 90 and i >= 65):
        a = a + chr(i - s + 26)

      else:
        a = a + chr(i - s)
    print(a)
  elif k == 0:
    break
  else:
    print("enter a valid number....")
print("......")