print("INTERPOL Syntax Checker")
print("Input CREATE to begin. Input RUPTURE to END.")
run = True
startChecking = True

def inputKeyword():
  global keyword
  keyword = input("$ ")

def initialize():
  global run, keyword, startChecking
  if keyword=="CREATE":
    print("The syntax is correct. Beginning syntax checker.")
    while startChecking:
      syntaxChecker()
  elif keyword=="RUPTURE":
    print("Thank you for using the syntax checker.")
    run = False
  
def syntaxChecker():
  global run, keyword, startChecking
  inputKeyword()
  checkWord = keyword.split('#')[0]
  syntax = keyword.split()[0]
  if checkWord=="CREATE":
    print("The syntax is correct.")
  elif checkWord=="RUPTURE":
    print("Thank you for using the syntax checker.")
    run = False
    startChecking = False
  elif checkWord=="" and keyword[0][0]=="#":
    print("The syntax is correct.")
  elif syntax=="GIVEYOU!" or syntax=="GIVEYOU!!":
    checkString(keyword, syntax)
  elif syntax=="PLUS" or syntax=="MINUS" or syntax=="TIMES" or syntax=="DIVBY" or syntax=="MODU":
    checkInteger(keyword, syntax)
  else:
    print("The syntax is incorrect.")

def checkString(word, syntax):
  # Combine strings in array with splitting specific word only once
  analyzeWord = ''.join(word.split(syntax + ' ',1)[1])
  if analyzeWord.startswith('"') and analyzeWord.endswith('"') and all(ord(char) > 31 for char in analyzeWord) and all(ord(char) < 127 for char in analyzeWord):
    print("The syntax is correct.")
  else:
    print("The syntax is incorrect.")

def checkInteger(number, syntax):
  numbers = number.split(syntax + ' ', 1)[1].split()
  if len(numbers) == 2:
    try:
      num1 = int(numbers[0])
      num2 = int(numbers[1])
      if isinstance(num1, int) and isinstance(num2, int):
        print("The syntax is correct.")
    except ValueError:
      print("The syntax is incorrect.")
  else:
      print("The syntax is incorrect.")

while run:
  inputKeyword()
  initialize()