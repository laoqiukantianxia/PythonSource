import os
# print(dir(os))
print(os.name)     # nt => windows 系统，posix => lunux/Unix/Mac os x
# print(os.environ)  # 环境变量
print('GOPATH: ', os.environ.get('GOPATH'))

# 当前目录绝对路径
abs_path = os.path.abspath('.')
print(abs_path)
dir = os.path.join(abs_path, 'testdir')
if os.path.exists(dir):
    print(dir)
    os.rmdir(dir)
else:
    os.mkdir(dir)
print(os.path.split(dir))    # 最后一部分总是最后级别的目录或者文件名

#
# os.rename('test.txt', 'test.py')  # 重命名
# os.remove('test.py')  # 删除文件

# 列出文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
