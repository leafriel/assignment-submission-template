import random

words = ["apple", "banana", "orange", "grape", "melon", "peach", "lemon", "cherry"]
# 生成约 200MB - 500MB 的数据
# 关键点：每 10 个单词换一行
with open("data_uniform.txt", "w") as f:
    for i in range(100000000): 
        f.write(f"{random.choice(words)} ")
        if i % 10 == 0:  # 每10个单词插入一个换行符
            f.write("\n")
print("Data generation complete.")