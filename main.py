import os
from os.path import basename
import re

# поиск txt в директории 
def corr(dict, directory):
    for adress, _, files in os.walk(os.path.normpath(directory)):
        for file in files:
            if file.endswith('.txt'):
                dict.append(os.path.join(adress,file))
    print("Найдено файлов .txt: ", len(dict))

# поиск вхождения слова в найденных txt
def perebor_corr(dict, word):
    for files_txt in dict:
        text = open(files_txt, 'r', encoding='utf-8', errors='ignore').read().lower()  # считывает весь текст из всех текстовых документов
        filename = os.path.splitext(basename(files_txt)[:-4])   # отрезает у названий файлов .txt
        split_regex = re.compile(r'[.]')  # для деления словаря на предложения по точкам
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
        for i in sentences:
            if word in i:
                print(filename[0], ":", i)
                print("Количество символов до слова",word,"=",text.index(word))
                print("Количество символов после слова",word,"=", len(text) - text.index(word) - len(word))
    return exit_choise()

# ввод директории и искомого слова
def main():
    dict = []
    directory = input("Введите директорию: ")
    corr(dict, directory)
    word = input("Слово введи: ").lower()
    perebor_corr(dict, word)

# выбор завершить или продолжить поиск
def exit_choise():
    que = input("Продолжить? (y/n): ")
    if que == "y":
        return main()
    elif que == "n":
        exit       
  
main()
