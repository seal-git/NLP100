# coding: UTF-8

'''
Created on 2020/04/12
 
@author: seal0
'''
import argparse

if __name__ == '__main__':
    pass

parser = argparse.ArgumentParser()

parser.add_argument("filename")

parser.add_argument("N")

args = parser.parse_args()

with open(args.filename) as f:
    text = f.read().strip().split("\n") #readでファイル終端まで読み込み、stripで空白文字を削除する

print([text[i] for i in range((int)(args.N))])
    
    
    
    
    