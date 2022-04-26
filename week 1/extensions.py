name = input(": ").lower().strip()

if name[-5:] == ".jpeg":
    print("image/jpeg")
elif name[-4:] == ".png":
    print("image/png")
elif name[-4:] == ".gif":
    print("image/gif")
elif name[-4:] == ".jpg":
    print("image/jpeg")
elif name[-4:] == ".txt":
    print("text/plain")
elif name[-4:] == ".pdf":
    print("application/pdf")
elif name[-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
