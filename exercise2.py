
f = open("talk.txt", "r")
for each_line in f:
    if each_line[0:] != '\n':  # 分行
        (role, line_spoken) = each_line.split(':', 1)  # 分割人物与话语
        if role not in person:
            person[role] = [line_spoken]
        else:
            person[role].append(line_spoken)

f.close()

for name in person:
    with open(name + '.txt', 'w') as fw:
        # writelines接收的是一个列表,意在将列表中的元素分别写入文件
        fw.writelines(person[name])
