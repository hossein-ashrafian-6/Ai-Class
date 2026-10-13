scores = {
    "Ali": 18,
    "Sara": 20,
    "Reza": 9,
    "Mina": 14,
    "Omid": 11.5
}

passed_students = []

# الف) چاپ نمره و رتبه هر دانشجو
for name, score in scores.items():
    if score >= 17:
        rank = "عالی"
    elif score >= 14:
        rank = "خوب"
    elif score >= 10:
        rank = "قبول"
    else:
        rank = "مردود"

    print(f"{rank} → {name}: {score}")

    # ب) جمع کردن اسم دانشجویان قبول شده
    if score >= 10:
        passed_students.append(name)

print("قبول شده‌ها:", passed_students)

# ج) محاسبه میانگین کلاس
average = sum(scores.values()) / len(scores)
print("میانگین کلاس:", average)

# د) پیدا کردن نفر اول کلاس
top_student = max(scores, key=scores.get)
print("نفر اول:", top_student)
