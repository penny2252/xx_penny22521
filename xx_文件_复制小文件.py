file1=open('readme')
file2=open('readme_1','w')
file2.write(file1.read())
file1.close()
file2.close()
file3=open('readme_1')
print(file3.read())
file3.close()
#大文件
file_read=open('readme')
file_write=open('readme_2','w')
while True:
    txt=file_read.readline()
    file_write.write(txt)
    if txt=='':
        break
file_read.close()
file_write.close()
file3=open('readme_2')
print(file3.read())
file3.close()