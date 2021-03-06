#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author：Huihuihui 
# Time:2018/10/15

class DFA:
    file_object = ''  # 文件句柄

    line_number = 0  # 记录行号

    state = 0  # 状态

    ResWord = ['int', 'if', 'then', 'else', 'end', 'repeat', 'until', 'read', 'write']  # 保留字

    error_message = []  # 保存错误信息,存储元组,元组第一个参数是行号,第二个参数是错误字符

    annotate_message = []  # 注释信息,存储元组,元组第一个参数是行号,第二个参数是注释

    char_message = []  # 识别的字符串,存储元组,元组第一个参数是类型,第二个参数是该字符串

    def __init__(self, file_name):

        self.file_object = file_name

        self.state = 0

        self.line_number = 0

        self.error_message = []

        self.annotate_message = []

        self.char_message = []

    def Start_convert(self):

        for line in self.file_object:  # 一行行的处理

            line = line.strip('\n')  # 去除换行fu

            self.line_number += 1  # 没处理一行行号加一

            line_length = len(line)

            i = 0

            string = ''  # 存储一个字符串

            while i < line_length:

                ch = line[i]  # 读取该行的一个字符

                i += 1

                if self.state == 0:  # 初始状态

                    string = ch

                    if ch.isalpha():

                        self.state = 1

                    elif ch.isdigit():

                        self.state = 3

                    elif ch == '+':

                        self.state = 5

                    elif ch == '-':

                        self.state = 9

                    elif ch == '*':

                        self.state = 13

                    elif ch == '/':

                        self.state = 16

                    elif ch == '=':

                        self.state = 20

                        i -= 1

                    elif ch == '<':

                        self.state = 21

                        i -= 1

                    elif ch == '{':

                        self.state = 22

                        i -= 1

                    elif ch == '}':

                        self.state = 23

                        i -= 1

                    elif ch == ';':

                        i -= 1

                        self.state = 24

                    elif ch.isspace():

                        self.state = 25

                    else:

                        self.state = 26  # 不可识别状态

                        i -= 1

                elif self.state == 1:  # 判断字母数字

                    while ch.isalpha() or ch.isdigit():

                        string += ch

                        if i < line_length:

                            ch = line[i]

                            i += 1

                        else:

                            break

                    self.state = 2

                    i -= 2  # 回退2个字符

                elif self.state == 2:

                    if string in self.ResWord:

                        content = '(关键字,' + string + ')'

                    else:

                        content = '(标识符,' + string + ')'

                    # print content

                    self.char_message.append(content)

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 3:

                    while ch.isdigit():

                        string += ch

                        if i < line_length:

                            ch = line[i]

                            i += 1

                        else:

                            break

                    self.state = 4

                    i -= 2  # 回退2个字符

                elif self.state == 4:

                    content = '(数字,' + string + ')'

                    self.char_message.append(content)

                    # print string

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 5:

                    if ch == '+':

                        self.state = 6

                        i -= 1

                    elif ch == '=':

                        self.state = 7

                        i -= 1

                    else:

                        self.state = 8

                        i -= 2

                elif self.state == 6:  # 判断++

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 7:  # 判断+=

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 8:  # 判断+

                    content = '(特殊符号,' + ch + ')'

                    self.char_message.append(content)

                    # print ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 9:

                    if ch == '-':

                        self.state = 10

                        i -= 1

                    elif ch == '=':

                        self.state = 11

                        i -= 1

                    else:

                        self.state = 12

                        i -= 2

                elif self.state == 10:

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch#判断--

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 11:  # 判断-=

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 12:  # 判断-

                    content = '(特殊符号,' + ch + ')'

                    self.char_message.append(content)

                    # print ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 13:

                    if ch == '=':

                        self.state = 14

                        i -= 1

                    else:

                        self.state = 15

                        i -= 2

                elif self.state == 14:  # 判断*=

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 15:  # 判断*

                    content = '(特殊符号,' + ch + ')'

                    self.char_message.append(content)

                    # print ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 16:

                    if ch == '/':

                        self.state = 17

                        i -= 1

                    elif ch == '=':

                        self.state = 18

                        i -= 1

                    else:

                        self.state = 19

                        i -= 2

                elif self.state == 17:  # 判断//

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    content = '(注释,' + line[i:] + ')'

                    self.annotate_message.append(content)

                    # print content

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 18:  # 判断/=

                    content = '(特殊符号,' + string + ch + ')'

                    self.char_message.append(content)

                    # print string + ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 19:  # 判断/

                    content = '(特殊符号,' + ch + ')'

                    self.char_message.append(content)

                    # print ch

                    string = ''  # 回到初始情况

                    self.state = 0  # 回到状态0

                elif self.state == 20:

                    content = '(特殊符号,=)'

                    self.char_message.append(content)

                    # print '='

                    self.state = 0

                    string = ''

                elif self.state == 21:

                    content = '(特殊符号,<)'

                    self.char_message.append(content)

                    # print '<'

                    self.state = 0

                    string = ''

                elif self.state == 22:

                    content = '(特殊符号,{)'

                    self.char_message.append(content)

                    # print '{'

                    self.state = 0

                    string = ''

                elif self.state == 23:

                    content = '(特殊符号,})'

                    self.char_message.append(content)

                    # print '}'

                    self.state = 0

                    string = ''

                elif self.state == 24:

                    content = '(特殊符号,;)'

                    self.char_message.append(content)

                    # print ';'

                    self.state = 0

                    string = ''

                elif self.state == 25:

                    while ch.isspace():

                        if i < line_length:

                            ch = line[i]

                            i += 1

                        else:

                            break

                    self.state = 0

                    i -= 1

                elif self.state == 26:

                    content = '(行号:' + str(self.line_number) + ',' + ch + ')'

                    self.error_message.append(content)

                    # print 'error:' + ch

                    self.state = 0

                    string = ''

        # print self.state

    def Get_error(self):  # 获取错误信息

        return self.error_message

    def Get_annotate(self):  # 获取注释信息

        return self.annotate_message

    def Get_char(self):  # 获取识别信息

        return self.char_message




try:

    file_object = open("N:\\wang4.txt")

    dfa = DFA(file_object)

    dfa.Start_convert()

    content = dfa.Get_char()

    for item in content:

        print item

    content = dfa.Get_annotate()

    for item in content:

        print item

    content = dfa.Get_error()

    for item in content:

        print item

finally:  

    file_object.close()  


