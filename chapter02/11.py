# coding: UTF-8

'''
Created on 2020/04/12

@author: seal0
'''
if __name__ == '__main__':
    pass

with open("popular-names.txt") as f:
    names_data = list(map(lambda x:x.replace("\t", " "), f.read().strip().split("\n"))) #readでファイル終端まで読み込み、stripで空白文字を削除する

print(names_data)
