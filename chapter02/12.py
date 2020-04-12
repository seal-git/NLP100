# coding: UTF-8

'''
Created on 2020/04/12

@author: seal0
'''
if __name__ == '__main__':
    pass

with open("popular-names.txt") as f:
    names_data = list(map(lambda x:x.split("\t"), f.read().strip().split("\n"))) #readでファイル終端まで読み込み、stripで空白文字を削除する

with open("col1.txt", mode="w") as f1:
    f1.write("\n".join([s[0] for s in names_data]))

with open("col2.txt", mode="w") as f2:
    f2.write("\n".join([s[1] for s in names_data]))
