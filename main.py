from core.listener import listen
from core.processor import process_command

command = listen()
print(f"you said: {command}")

process_command(command)
