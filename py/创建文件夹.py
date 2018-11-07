#__*__ encoding:utf-8 __*__
def mkdir(path):
    import os
    #移除首尾的空格
    path = path.strip()
    #去除末尾的\
    path = path.rstrip('\\')
    #判断目录是否存在
    isExists = os.path.exists(path)
    #如果目录不存在，则创建
    if not isExists:
        os.makedirs(path)
        #并提示已创建目录
        print(path, '创建成功')
    #否则提示该目录已存在
    else:
        print(path, '目录已存在')

if __name__ == '__main__':
    path = 'Hll/Test'
    mkdir(path)
