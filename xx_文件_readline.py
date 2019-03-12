file=open('readme')
while True:
    txt=file.readline()
    print(txt)
    if txt=='':
        break

file.close()