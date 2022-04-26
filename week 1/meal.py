def main():
    time = input("Enter a time: ")
    t = convert(time)
    if 7<= t <= 8:
        print("breakfast time")
    elif 12<= t <= 13:
        print("lunch time")
    elif 18<= t <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    time = time.split(":")
    return float(time[0]) + float(time[1]) / 60


main()
