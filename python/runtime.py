# Проверка времени выполнения кода в наносекундах
import time

ITER_COUNT = 6_000_000

start = 0
finish = 0

# ------- переменные для теста --------
string = "TEST string 123 !@#"
text1 = ""
text2 = ""
text3 = ""
# -------------------------------------

start = time.thread_time()
# ------------- 1 вариант -------------
for i in range(ITER_COUNT):
    text1 = "{} my concat {}".format(string, string)
# -------------------------------------
finish = time.thread_time()
print("1 вариант: " + str(finish - start))

start = time.thread_time()
# ------------- 2 вариант -------------
for i in range(ITER_COUNT):
    text2 = f"{string} my concat {string}"
# -------------------------------------
finish = time.thread_time()
print("2 вариант: " + str(finish - start))

start = time.thread_time()
# ------------- 3 вариант -------------
for i in range(ITER_COUNT):
    text3 = string + " my concat" + string
# -------------------------------------
finish = time.thread_time()
print("3 вариант: " + str(finish - start))

# Вывод: Второй вариант быстрый, но третий выигрывает при одной склейке...
