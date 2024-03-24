from os import strerror

try:
    src = open("tzop.txt", 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
    st=''

dictn = {}

try:
    ch = src.read(1)
    while ch != '':
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            dictn[ch.lower()] = dictn.get(ch.lower(), 0) + 1
        ch=src.read(1)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)

print(dict, 'byte(s) succesfully written')
print("sorted:",dict(sorted(dictn.items(), key=lambda item: item[1], reverse=True)))
src.close()
