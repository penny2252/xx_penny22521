from distutils.core import setup
setup(name='xx_message',#包名
      version='1.0',#版本
      description='xiaoxiao发送和接收消息模块',#描述信息
      long_description='完整的发送和接受消息模块',#完整描述信息
      author='xiaoxiao',#作者
      author_email='13982121',#作者邮箱
      url='www',#主页
      py_modules=['xx_message.sendmessage',
                  'xx_message.receivemessage'])
