import random

words = ["apple", "banana", "orange", "grape", "melon", "peach", "lemon", "cherry"]
# 目标：生成数据倾斜文件
# "apple" 出现的概率设为 90%，模拟热点 Key
# 必须加入换行符防止 OOM

print("Generating skewed data...")
with open("data_skewed.txt", "w") as f:
    for i in range(100000000):  # 循环次数决定文件大小
        if random.random() < 0.9: 
            f.write("apple ")  # 制造倾斜
        else:
            f.write(f"{random.choice(words[1:])} ") # 其他单词
        
        # 关键修正：每 10 个单词换一行
        if i % 10 == 0:
            f.write("\n")

print("Skewed data generation complete.")