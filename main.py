from listener import listen
from processor import process_command

command = listen()
print(f"you said: {command}")

process_command(command)