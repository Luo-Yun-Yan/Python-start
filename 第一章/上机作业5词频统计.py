def word_count(text):
    words=text.split()
    return{word:words.count(word) for word in dict.fromkeys(words)}
#dict.fromkeys(words)原顺序排序,set(words)随机排序,sorted首字母排序
print(word_count('apple banana apple'))