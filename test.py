import random

num_random_group = 10
lower_bound = 0
upper_bound = 999999999999999999999999999999999999999999

with open('random_numbers.txt', 'w') as file:
    for _ in range(num_random_group):
        flag = random.randint(0,1)
        if flag == 0:
            file.write("+\n")
        else:
            file.write("-\n")
        num_1 = random.randint(lower_bound, upper_bound)
        num_2 = random.randint(lower_bound, upper_bound)
        
        file.write(f"{num_1}\n{num_2}\n")

print("随机数已生成并写入文件。")
