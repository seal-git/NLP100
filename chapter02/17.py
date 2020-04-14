# coding: UTF-8

'''
Created on 2020/04/12
 
@author: seal0
'''
import argparse, sys

if __name__ == '__main__':
    pass

parser = argparse.ArgumentParser()

parser.add_argument("filename")

args = parser.parse_args()

with open(args.filename) as f:
    names_data = list(map(lambda x:x.split("\t"), f.read().strip().split("\n"))) #readでファイル終端まで読み込み、stripで空白文字を削除する

text = [t[0] for t in names_data]
new_text = list(set(text))
new_text.sort()    
print("\n".join(new_text))
print(len(new_text))