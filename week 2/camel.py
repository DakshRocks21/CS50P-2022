text = input(": ")

new_text = ""
for i in range(len(text)):
    if text[i].isupper():
        new_text += "_"+text[i].lower()
    else:
        new_text += text[i]

print(new_text)