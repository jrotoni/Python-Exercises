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
    print("Starting program")
    while startChecking:
      syntaxChecker()
  elif keyword=="RUPTURE":
    print("Ending program")
    run = False
  
def syntaxChecker():
  global run, keyword, startChecking
  inputKeyword()
  if len(keyword) > 0:
    checkWord = keyword.split('#')[0]
    inputWords = keyword.split()
    syntax = keyword.split()[0]
    if checkWord=="RUPTURE":
      print("Ending program")
      run = False
      startChecking = False
    elif (checkWord=="" and keyword[0][0]=="#") or checkWord=="CREATE":
      pass
    elif len(inputWords) > 1:
      if syntax=="GIVEYOU!" or syntax=="GIVEYOU!!":
        checkString(keyword, syntax)
      elif syntax=="PLUS" or syntax=="MINUS" or syntax=="TIMES" or syntax=="DIVBY" or syntax=="MODU":
        checkInteger(keyword, syntax)
      else:
        print("The syntax is incorrect.")
    else:
      print("The syntax is incorrect.")

def checkString(word, syntax):
  # Combine strings in array with splitting specific word only once
  analyzeWord = ''.join(word.split(syntax + ' ',1)[1])
  if analyzeWord.startswith('"') and analyzeWord.endswith('"') and all(ord(char) > 31 for char in analyzeWord) and all(ord(char) < 127 for char in analyzeWord):
    if syntax=="GIVEYOU!":
      print(analyzeWord[1:-1])
    elif syntax=="GIVEYOU!!":
      print(analyzeWord[1:-1] + "\n")
  else:
    print("The syntax is incorrect.")

def checkInteger(number, syntax):
  numbers = number.split(syntax + ' ', 1)[1].split()
  if len(numbers) == 2:
    try:
      num1 = int(numbers[0])
      num2 = int(numbers[1])
      if isinstance(num1, int) and isinstance(num2, int):
        if syntax=="PLUS":
          print(num1+num2)
        if syntax=="MINUS":
          print(num1-num2)
        if syntax=="TIMES":
          print(num1*num2)
        if syntax=="DIVBY":
          print(round(num1/num2))
        if syntax=="MODU":
          print(num1%num2)
    except Exception as error:
      print("Error: " + str(error))
  else:
    print("The syntax is incorrect.")

while run:
  inputKeyword()
  initialize()