# 5.Получите и преобразуйте текущую системную дату, возвращаемую методом date.today() модуля стандартной библиотеки datetime,
# из формата «год-месяц-день» в формат «день.месяц.год». Выведите оба формата даты на экран.

import datetime

date_1 = datetime.date.today()
date_2 = datetime.date.today(). strftime("%d.%m.%Y")

print(f' {date_1}, {date_2} ')