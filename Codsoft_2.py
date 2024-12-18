import string
import random
wtc = "y"
while wtc == "y":
    if __name__ == "__main__":
      s1 = string.ascii_letters
      s2 = string.ascii_lowercase
      s3 = string.ascii_uppercase
      s4 = string.digits
      s5 = string.punctuation
      plen = int(input("Enter password length: \n"))
      s = []
      s.extend(s2)
      s.extend(s3)
      s.extend(s4)
      s.extend(s5)
      random.shuffle(s)
      
      password = "".join(s[0:plen])
      print(f"This is your password: {password}")
      wtc = input("Want to create more passwords? (y/n): ")
