import json
import argparse
import os
import sys
from pandas import json_normalize

#json파일 불러오기
def json_read(file_path):

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as json_file:

        json_data = json.load(json_file)

    json_file.close()

    return json_data

# file_save
def file_write(path, lst):
    with open(path, 'w', -1, 'utf-8') as output:
        for line in lst:
            output.write(str(line)+"\n")
    output.close()


p = argparse.ArgumentParser()
p.add_argument('--path', '-p', help='Enter the path of the folder contains json files.', type=str)
args = p.parse_args()

file_lst = os.listdir(args.path)
print()
# print(str(args.path))
print("입력하신 경로에 존재하는 파일목록입니다.")
print(file_lst)
print()

#예외처리
for file in file_lst:
    tmp = file.split(".")
    if tmp[-1] != "json":
        print("해당 경로에는 json file만 존재하여야합니다.")
        sys.exit()

output_path = "./result/"
if not os.path.isdir(output_path):
    os.mkdir(output_path)


for i in range(0, len(file_lst)):

    path = args.path + file_lst[i]
    json_data = json_read(path)
    print(file_lst[i])

    if type(json_data) != list:
        keys_lst = list(json_data.keys())
        if len(keys_lst) == 1:
            key = keys_lst[0]
            keys_lst = json_data[key][0].keys()
            json_data = json_data[key]
            print("list of keys : ", end=' ')
            print(keys_lst)
            print()

    else:
        keys_lst = json_data[0].keys()
        print("list of keys : ", end=' ')
        print(keys_lst)
        print()

    select_keys = input("추출하실 key명들을 입력해주세요(en,ko,mt,,,) : ")
    select_keys = select_keys.split(",")
    # print(select_keys)
    print()

    json_df = json_normalize(json_data)

    for key in select_keys:
        print(key)
        temp = json_df[key]

        if not key.encode().isalpha():         #예외처리
            extension = input("저장하실 파일 확장자를 입력해주세요 : ")
            file_write(output_path + file_lst[i] + '.' + extension, temp)
        else:
            file_write(output_path + file_lst[i] + '.' + key, temp)

        print("finish--")
        print()
    print()






