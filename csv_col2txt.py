import pandas as pd
import os
import argparse

# file_read
def file_read(filename):
    input = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file.readlines():
            input.append(line)
    file.close()

    return input

# file_save
def file_write(path, lst):
    with open(path, 'w', -1, 'utf-8') as output:
        for line in lst:
            output.write(line.lstrip()+"\n")
    output.close()


p = argparse.ArgumentParser()
p.add_argument('--path', '-p', help='Enter the file path.', type=str)
args = p.parse_args()

path = args.path

df = pd.read_csv(path)
df.head()


def dfcol2txt(df):
    col_lst = df.columns

    path = "./result/"
    if not os.path.isdir(path):
        os.mkdir(path)

    for col in col_lst:
        temp = list(df[col])
        file_write('./result/' + str(col) + '.txt', temp)


dfcol2txt(df)