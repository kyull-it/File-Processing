
import os

path = "D:/Book/"
dirlist = os.listdir(path)

filelist = []
for directory in dirlist:

    try:
        temp_lst = os.listdir(path + directory)
        filelist.extend(temp_lst)

    except Exception as e:
        filelist.append(directory)

corpus_lst = []
for i, filename in enumerate(filelist):
    corpus_name = "corpus[" + str(i+1) + "]=" + str(filename)
    corpus_lst.append(corpus_name)


textfile = open("file_list.txt", 'w')

for element in corpus_lst:
    textfile.write(element+"\n")