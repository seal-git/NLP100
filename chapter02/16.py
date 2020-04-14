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

parser.add_argument("N")

args = parser.parse_args()

with open(args.filename) as f:
    text = f.read().strip().split("\n") #readでファイル終端まで読み込み、stripで空白文字を削除する

print(len(text))
N = (int)(args.N)
if(len(text)%N != 0):
    print("lines must be multiple of N")

l = (int)(len(text)/N)
for i in range(N):
    with open("split_file_"+(str)(i).zfill(2)+".txt", mode="w") as f1:
        f1.write("\n".join([text[i] for i in range(i*l, i*l+l, 1)]))
    
    
    
    