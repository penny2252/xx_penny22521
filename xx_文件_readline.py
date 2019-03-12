file=open('readme')
while True:
    txt=file.readline()
    if txt=='':
        break
    print(txt)
file.close()