# def even_check(lst):
#     for i in lst:
#         if i % 2==0:
#             print(i)
# even_check([1,4,6,88,144,123])






# calculator

# def sum(a, b):
#     return (a+b)


# def sub(a, b):
#     return (a-b)


# def mul(a, b):
#     return (a*b)


# def div(a, b):
#     return (a/b)


# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))

# print("Please choose the operation you want to perform ")
# print("1. Sum")
# print("2. Sub")
# print("3. Mul")
# print("4. Div")

# selection = int(input())

# if(selection == 1):
#     answer = sum(x, y)
# elif(selection == 2):
#     answer = sub(x, y)
# elif(selection == 3):
#     answer = mul(x, y)
# elif(selection == 4):
#     answer = div(x, y)

# print("The answer is", answer)






# email validation

# while True:
#     try:
#         email = input("Enter email: ")
#         password = input("Enter password: ")
#         domains = ['com', 'edu', 'co.in', 'org']

#         # abc@gmail.com abc123@hotmail.co.in
#         # ['abc@gmail', 'com'] ['abc123@hotmail', 'co.in']

#         if "@" not in email or email.split('.', 1)[1] not in domains:
#             raise IndexError
#         elif len(password) < 8:
#             raise ArithmeticError

#         print("Email: ", email)
#         print("Password: ", password)

#         break

#     except IndexError:
#         print("Email is not valid")

#     except ArithmeticError:
#         print("Password is not valid")


import re
import random


class Rulebot:
  negative_responses=("no","nope","nah","naw","not a chance","sorry")
  exit_commands=("quit","pause","exit","goodbye","bye","later")
  random_questions=(
      "why are you here?",
      "Are there more humans like you?",
      "What do you eat?",
      "Is there intelligent life?",
      "Does earth have a leader?",
      "What planets have you visited yet?",
      "What technology do you have on earth?"
  )

  def __init__(self):
    self.alienbabble={
        'describe_planet_intent': r'.*\s*your planet.*',
        'answer_why_intent': r'why\sare.*',
        'about_me': r'.*\s*Intellipat'
    }

  def greet(self):
    self.name=input("What is your name?\n")
    will_help=input(
        f"Hi {self.name}, I am a Rule-Bot. Will You tell me more about your planet?\n")
    if will_help in self.negative_responses:
      print("OK, Have a nice day!")
      return
    self.chat()

  def make_exit(self,reply):
    for command in self.exit_commands:
      if reply==command:
        print("Okay, have a nice day")
        return True

  def chat(self):
    reply=input(random.choise(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply=input(self.match_reply(reply))


  def match_reply(self,reply):
    for key,value in self.alienbabble.items():
      intent=key
      regex_pattern=value
      found_match=re.match(regex_pattern,reply)
      if found_match and intent=='describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent=='answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent=='about_me':
        return self.about_me()
    if not found_match:
      return self.no_match_intent()



  def describe_planet_intent(self):
    responses=("My planet is a utopia of diverse organisms and species.\n",
               "I am from opidious , the capital of the wayward galaxies.\n")
    return random.choice(responses)

  def answer_why_intent(self):
    responses=("I come in peace\n", "I am here to collect data on your planet and its inhabitants\n",
               "I heard the coffee is good\n")
    return random.choice(responses)

  def about_me(self):
    responses=("Intellipat is world's largest professional company.\n",
               "Intelipat is where your skills and career grows.\n")
    return random.choice(responses)

  def no_match_intent(self):
    responses=("Please tell me more\n", "Tell me more\n", "Why do you say that?\n", "I see can you elaborate?\n",
               "Interesting can you tell me more?\n", "I see, how do you think?\n",
               "why?\n","How do you think i feel when you say that?\n")
    return random.choice(responses)

AlienBot=Rulebot()
AlienBot.greet
