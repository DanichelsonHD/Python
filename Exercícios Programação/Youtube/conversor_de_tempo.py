#00:00:00 => segundos

def convert_time_textBot (time: str):
    hours, minutes, seconds = time.split(':')
    new_time: int = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    print(new_time)
    
def convert_time (time: str):
    hours = int(time[0] + time[1])
    minutes = int(time[3] + time[4])
    seconds = int(time[6] + time[7])
    
    minutes = minutes + hours * 60
    seconds = seconds + minutes * 60
    print(seconds)

convert_time('00:01:30')