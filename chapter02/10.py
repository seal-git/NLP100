# coding: UTF-8
'''
Created on 2020/04/12

@author: seal0
'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("filename")

args = parser.parse_args()


with open(args.filename) as f:
    names_data = list(map(lambda x:x.split("\t"), f.read().strip().split("\n"))) #readでファイル終端まで読み込み、stripで空白文字を削除する

print(len(names_data))

    
