check = False  # Переменная проверки, принимает значение True, если все данные корректны
rasst = []  # Массив расстояний до домов сотрудников
tarifs = []  # Массив тарифов таксистов за км
# Ввод n и обработка неккоректно введенных данных
while not check:
    # Проверка соответствия формату данных
    try:
        n = int(input("Введите n: "))
        check = True
    except ValueError:
        print("Некорректный формат данных\nПопробуйте снова")
        check = False

# Ввод расстояний и обработка неккоректного ввода
check = False
while not check:
    uncorrect_numbers = str()
    rasst=list(input(f"Введите n расстояний через пробел:\n").split())

    # Проверка количества элементов массива
    if n == len(rasst):
        check=True
    else:
        print(f"Количество расстояний не {n}")

    # Проверка соответствия формату данных
    if check:
        for i in range(len(rasst)):
            try:
                rasst[i] = int(rasst[i])
            except ValueError:
                uncorrect_numbers+=str(i+1)+' '
                check=False
        if not check:
            if len(uncorrect_numbers.split()) > 1:
                print(f"Неккоректные расстояния под номерами: {uncorrect_numbers}")
            else:
                print(f"Некорректное расстояние под номером {uncorrect_numbers.split()[0]}")

# Ввод тарифов и обработка неккоректного ввода
check=False
while not check:
    uncorrect_numbers = str()
    tarifs=list(input(f"Введите n тарифов через пробел:\n").split())

    # Проверка количества элементов массива
    if n == len(tarifs):
        check = True
    else:
        print(f"Количество тарифов не {n}")

    # Проверка соответствия формату данных
    if check:
        for i in range(len(tarifs)):
            try:
                tarifs[i] = int(tarifs[i])
            except ValueError:
                uncorrect_numbers += str(i+1)+' '
                check = False
        if not check:
            if len(uncorrect_numbers.split()) > 1:
                print(f"Неккоректные тарифы под номерами: {uncorrect_numbers}")
            else:
                print(f"Некорректный тариф под номером {uncorrect_numbers.split()[0]}")

rasst_sorted=[]  # Массив отсортированных расстояний
tarifs_sorted=[]  # Массив отсортированных тарифов

# Добавление элементов в отсортированные масивы в формате кортежа (Индекс элемента, Элемент)
for i in range(n):
    rasst_sorted.append((i,rasst[i]))
    tarifs_sorted.append((i,tarifs[i]))

# Сортировка массивов по элементу, с сохранением индексов элемента
rasst_sorted=sorted(rasst_sorted, key=lambda i: i[1])  # Сортировка по возрастанию
tarifs_sorted=sorted(tarifs_sorted, key=lambda i: i[1], reverse=True)  # Сортировка по убыванию

out=[0]*n  # Массив выходных данных

# Заполнение массива выходных данных
for i in range(n):
    out[rasst_sorted[i][0]] = tarifs_sorted[i][0] + 1  # Заполнение происходит по изначальным номерам элементов

# Вывод
for i in range(n):
    print(f"{i+1}-й сотрудник должен уехать на {out[i]}-й машине")