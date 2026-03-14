from datetime import datetime
now = datetime.now()

def curr_time():
    current_time = now.strftime("%H:%M")
    return current_time

