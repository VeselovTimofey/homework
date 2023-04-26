# homework

### Первое задание(last_message.sql)
Задание: необходимо написать SQL запрос, который бы выводил текст последнего сообщения каждого пользователя.

Решение: в подзапросе находим дату последнего сообщения каждого пользователя.
В запросе выводим текст всех сообщений, у которых дата публикации совпадает с датами из подзапроса.

Проблема: если существуют сообщения с одинаковыми датами публикации, то запрос может выводить лишние сообщения.

### Второе задание(validation_brackets.py)
Задание: необходимо написать функцию, которая будет проверять валидность строки состоящей из скобок.

Решение: проверяем каждый элемент строки. Если это левая скобка мы прибавляем счётчик.
Если это правая скобка и у неё есть левая пара, то мы отнимаем счётчик. 
Если это правая скобка без пары или не скобка вовсе, мы выходим из цикла с ненулевым счётчиком.
В конечном счёте проверяем наш счётчик, если он нулевой то строка валидна.