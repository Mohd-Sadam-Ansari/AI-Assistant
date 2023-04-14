import datetime

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        greet="Good Morning"
    elif hour>12 and hour<16:
        greet="Good Afternoon"
    elif hour>15 and hour<22:
        greet="Good Evening"
    else:
        greet="Good Night"
    return greet
