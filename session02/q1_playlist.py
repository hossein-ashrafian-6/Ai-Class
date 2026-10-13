playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

# الف) تعداد آهنگ‌ها
print("تعداد آهنگ‌ها:", len(playlist))

# ب) اولین و آخرین آهنگ
print("اولین آهنگ:", playlist[0])
print("آخرین آهنگ:", playlist[-1])

# ج) اضافه کردن آهنگ Dynamite
playlist.append("Dynamite")

# د) حذف آهنگ Believer
playlist.remove("Believer")

# هـ) مرتب کردن لیست به ترتیب حروف الفبا
playlist.sort()
print("لیست مرتب شده:", playlist)

# و) چاپ شماره‌دار آهنگ‌ها با حلقه for
for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")
