from socket import *

# mylist 主要做的事情就是用作容器
class mylist:
    def __init__(self):
        self._elem = []

    def push(self,val):
        self._elem.append(val)

    def pop(self):
        return self._elem.pop()

    # 主要用于作判断
    def empty(self):
        return self._elem == []

# Ver做的事情主要是括号的业务判断
class Ver:
    def __init__(self):
        # self.parens在初始化对象时,我们要我们要验证的字符写进云
        self.parens = "{}[]()"  #　需要验证的字符
        # 将我们要判断的左括号写入到self.left_parens
        self.left_parens = "{[("
        #　验证配对是否正确
        self.opposite = {'}':'{',']':'[',')':'('}
        #最后创建出一个容器来
        self.vessel = mylist()


    # 负责提供遍历到的括号
    # parent 其实是一个生成器函数
    def parent(self,text):
      """
      遍历字符串,提供括号字符和其位置
      """
      #　ｉ记录索引位置
      #i 是文件的初始下标,text_len则是其长度
      i,text_len = 0,len(text)
      while True:
        # 循环遍历字符串
        # 到结尾结束，遇到括号提供给ｖｅｒ
        while i < text_len and text[i] not in self.parens:
        # 防止出现死循环
          i += 1
        # 当内层循环结束时,只有两种可能:1.遍历到结尾了   2.遇到括号了
        if i >= text_len:
          return
        # 在成功的匹配到括号时
        else:
          yield  text[i],i
          # text[i]  其实就是括号
          # i   指的是括号的位置
          i += 1


    #　字符是否匹配的验证工作
    # ver是一个启动函数
    def ver(self,text):
      for pr, i in self.parent(text):
        if pr in self.left_parens:
          self.vessel.push((pr,i))  #　左括号入栈
        #在右括号的情况下，执行elif
        elif self.vessel.empty() or self.vessel.pop()[0] != self.opposite[pr]:
          print("Unmatching is found at %d for %s"%(i,pr))
          break
      #　ｆｏｒ循环正常结束，一定没有经过break才会执行到else
      else:
        if self.vessel.empty():
          print("All parentheses are matched")
        else:
          #　剩下左括号了
          p = self.vessel.pop()
          print("Unmatching is found at %d for %s" % (p[1], p[0]))


# 主程序只负责做括号的验证
if __name__ == '__main__':
    file = input(">>")
    v = Ver()
    with open(file) as f:
        v.ver(f.read())










