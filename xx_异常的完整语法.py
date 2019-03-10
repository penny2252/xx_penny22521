#需要执行的代码
try:
    num=int(input('请输入整数：'))
    result=8/num
    print(result)
#知道异常的信息
except ValueError:
    print('请输入整数')
#不知道异常的信息的其他异常
except Exception as result:
    print('未知错误%s'%result)
#如果没有异常执行的代码
else:
    print('尝试成功')
#无论是否异常都执行
finally:
    print('无论是否出现错误都会执行的')
print('-'*50)