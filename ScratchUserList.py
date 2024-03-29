import os
os.system("pip install scratchattach")
os.system("pip install requests")
import scratchattach as scratch3
import requests

session = scratch3.login("DragonServer1", password)
conn = session.connect_cloud(project_id="706569784")

client = scratch3.CloudRequests(conn)

@client.request
def addUser(argument1, argument2):
  print("request received")
  print(f"{argument1} is adding {argument2}")
  file = open("ScratchUserList.txt", "r")
  text = file.read()
  if "key"+argument1.lower() in text.lower():
    status = "You already added someone."
  elif argument2.lower() in text.lower():
    status = "This person was already added."
  elif argument1.lower() == argument2.lower():
    status = "You cannot add yourself."
  else:
    response = requests.get(f"htttps://api.scratch.mit.edu/users/{argument2}")
    if response.status_code == 200:
      status = "User added!"
      file.close()
      file = open("ScratchUserList.txt", "a+")
      if len(text) > 0:
        file.write("\n")
      file.write("key"+argument1+":"+argument2)
      file.close()
      user = session.connect_user(argument2)
      user.post_comment(f"Hello @{argument2}! You have been added to SuperDragonStudios's Scratch User List (https://scratch.mit.edu/projects/706569784/) by @{argument1}.")
    else:
      status = "This user does not exist."
  print(status)
  return status

@client.request
def getListLength():
  print("request received")
  file = open("ScratchUserList.txt", "r")
  length = len(file.readlines())
  file.close()
  return length

@client.event
def on_ready():
  print("request handler is ready")

client.run()
