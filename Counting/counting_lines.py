import os
def Write_file(link):
    file_list = []
    count_list = []
    file_dict = {}
    for file in os.listdir(link):
        if file.endswith('.txt'):
            file_list.append(file)
    for file_d in file_list:
        with open(file_d,encoding="utf-8") as f:
            text = f.readlines()
            count_list.append(len(text))
            file_dict[len(text)] = file_d
    count_list.sort()
    for count in count_list:
        if file_dict[count]=='3.txt':
            continue
        else:
            with open(file_dict[count], encoding="utf-8") as f, open('3.txt', 'a', encoding="utf-8") as file:
                text = f.readlines()
                file.write(f'\n{file_dict[count]}')
                file.write(f'\n{str(count)}\n')
                for s1 in text:
                    file.write(f'{s1}')
Write_file(os.getcwd())

