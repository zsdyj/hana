"""
 编写一个函数，传入端口名称，返回这个端口运行情况中所描述
的address地址信息。
"""
import re

def get_address(port):
    '''
    :param port: 端口名称
    :return: 端口对应的address
    '''
    # f为文件流对象    它支持for循环的遍历
    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == '\n':
                break
            data += line
        # 没有找到目标段落
        if not data:
            return "没有该端口"
        #  提炼段落开头单词,作为判断依据,只要可以匹配到值,那就一定不会返回 None
        obj = re.match(r'\S+',data) # 使用正则匹配一段首个单词
        print('obj---------',obj)
        print('obj_text',obj.group())
        if port == obj.group():
            # pattern=r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
            pattern=r'(\d{1,3}\.){3}\d{1,3}/\d{2}|Unknown'
            # 返回match对象
            obj = re.search(pattern,data)
            print('xxxxxxxxxxxxxxxxxx',obj)
            # 如果说re.search 能够成功的返回match对象,就表明,此时,有数据已经匹配出来
            # 而如果re.search 并没有匹配出内容,则表示为None
            if obj:
                return obj.group()


if __name__ == '__main__':
    port = input("端口:")
    print(get_address(port))