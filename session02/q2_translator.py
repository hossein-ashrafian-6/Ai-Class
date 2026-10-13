words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "hello": "سلام",
    "world": "جهان",
    "computer": "کامپیوتر",
    "book": "کتاب",
    "good": "خوب"
}

sentence = "I love python and AI"

translated_words = []
translated_count = 0
not_translated_count = 0

for word in sentence.lower().split():
    if word in words:
        translated_words.append(words[word])
        translated_count += 1
    else:
        translated_words.append(f"[{word}]")
        not_translated_count += 1

print(" ".join(translated_words))

# بخش اضافه: تعداد کلمات ترجمه شده و ترجمه نشده
print("تعداد کلمات ترجمه شده:", translated_count)
print("تعداد کلمات ترجمه نشده:", not_translated_count)
