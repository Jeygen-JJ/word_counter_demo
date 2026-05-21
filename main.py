from collections import Counter

with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower().split()

counter = Counter(text)

with open('result.txt', 'w', encoding='utf-8') as f:
    for word, count in counter.items():
        f.write(f'{word}: {count}\n')

print("统计完成，结果写入 result.txt")
print("这是新的测试行")
<<<<<<< HEAD
# 输出总单词数
total_words = sum(counter.values())
print(f"总单词数: {total_words}")
=======
print("远程修改测试冲突")
>>>>>>> main
