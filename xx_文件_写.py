#1、只读方式,无法写入，回返回错误
# file=open('readme','r')
# file.write('hello')
# file.close()
#2、只写方式，会覆盖原有文件，如果文件不存在会创建
file=open('readme1','w')
file.write('hello')
file.close()
file=open('readme1','r')
print(file.read())
file.close()
#3、追加方式，指针到末尾，
file=open('readme1','a')
file.write('hello！！！')
file.close()
file=open('readme1','r')
print(file.read())
file.close()
#4、增加加号，读写方式，
# 一般用只读和只写方式打开，而不用读写方式