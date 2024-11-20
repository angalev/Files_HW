# Функция к заданию 1
def output1(file_list):
    combined_list = []
    for file in file_list:
        with open(file, encoding='UTF-8') as f:
            combined_list.append(f.readlines())
    result = []
    for elem in sorted(combined_list, key=len):
        result.extend(elem)
    return [c.rstrip("\n") for c in result]

# Функция к заданию 2
def output2(file_list):
    combined_list = []
    for i in range(len(file_list)):
        combined_list.append([])
        with open(file_list[i], encoding='UTF-8') as f:
            lst = f.readlines()
            combined_list[i] = [file_list[i], str(len(lst))] + lst
    result = []
    for elem in combined_list:
        result.extend(elem)
    return [c.rstrip("\n") for c in result]

# test
# print(output1(["1.txt", "2.txt", "3.txt"]))
# print(output2(["1.txt", "2.txt", "3.txt"]))

# write to file
with open("Output1.txt", "w+", encoding='UTF-8') as f:
    for line in output1(["1.txt", "2.txt", "3.txt"]):
        f.write(line + '\n')


with open("Output2.txt", "w+", encoding='UTF-8') as f:
    for line in output2(["1.txt", "2.txt", "3.txt"]):
        f.write(line + '\n')