from datetime import date
def measure_date(year : int, month : int, day : int):
    if (month in range(1,13)):
        target_date = date(year,month,day)
    else:
        return "Помилкова дата"
    
    today = date.today()

    if target_date == today:
        return "Це сьогодні!"
    elif target_date > today:
        return f"Ця дата буде через {(target_date-today).days} днів."
    else:
        return f"Ця дата була {} днів тому."
        


y = int(input("Введіть рік: "))
m = int(input("Введіть місяць: "))
d = int(input("Введіть день: "))

print(measure_date(y,y,d))