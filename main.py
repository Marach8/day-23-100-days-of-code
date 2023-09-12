print('REPLIT LOGIN SYSTEM')
print()

def askUser():
  while True:
    username = input('what is your username?: ')
    print()
    password = input('What is your password?: ')
    print()
    
    if username == 'Marach' and password == 'MaRaCh':
      print('\033[32mWelcome to Replit!\033[0m')
      break
    else:
      print('\033[31mWhoops! I do not recognize that username or password.\033[0m')
      print()
      print('Try again!')
      print()

askUser()
  