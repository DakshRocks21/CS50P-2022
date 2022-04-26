from urllib import response


def convert(x:str):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

def main():
    x = input()
    print(convert(x))

main()


