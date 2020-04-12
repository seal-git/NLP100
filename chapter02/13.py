# coding: UTF-8

'''
Created on 2020/04/12
 
@author: seal0
'''
if __name__ == '__main__':
    pass

with open("col1.txt") as f1:
    col1 = f1.read().strip().split("\n") #readでファイル終端まで読み込み、stripで空白文字を削除する

with open("col2.txt") as f2:
    col2 = f2.read().strip().split("\n") #readでファイル終端まで読み込み、stripで空白文字を削除する

col1_and_col2 = [s1+"\t"+s2 for s1, s2 in zip(col1, col2)]
with open("col1_and_col2.txt", mode="w") as f12:
    f12.write("\n".join(col1_and_col2))