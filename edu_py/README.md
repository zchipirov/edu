# Python-9

## Модуль Collections, main_4.3
Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок правильной.

Какая последовательность скобок правильная?
Правильной скобочной последовательностью назовём такую последовательность скобок, в которой для каждой открывающей скобки есть последующая соответствующая ей закрывающая скобка.

Цветом обозначены соответствующие друг другу скобки: (()())()

Соответственно, остальные скобочные последовательности назовём неправильными.

Пустую строку будем считать правильной последовательностью.

Для решения этой задачи потребуется использовать стек.
Посимвольно переберите строку. Если встретилась открывающаяся скобка, положите её в стек. Если встретилась закрывающаяся скобка, извлеките скобку из стека.

Если стек пустой, то есть извлечь скобку нельзя, последовательность неправильная.
Если строка закончилась и стек стал пустым, последовательность правильная.
Если в стеке остались скобки, последовательность неправильная.
Пример:

print(brackets("(()())"))
True
print(brackets(""))
True
print(brackets("(()()))"))
False

## Модуль Collections, main_4.9
Дан список кортежей ratings с рейтингами кафе. Кортеж состоит из названия и рейтинга кафе.
Необходимо отсортировать список кортежей по убыванию рейтинга. Если рейтинги совпадают, то отсортировать кафе дополнительно по названию в алфавитном порядке.
Получите словарь cafes с упорядоченными ключами из отсортированного списка, где ключи — названия кафе, а значения — их рейтинг.

## Модуль Collections, main_4.10
Напишите функцию task_manager, которая принимает список задач для нескольких серверов. Каждый элемент списка состоит из кортежа (<номер задачи>, <название сервера>, <высокий приоритет задачи>).

Функция должна создавать словарь и заполнять его задачами по следующему принципу: название сервера — ключ, по которому хранится очередь задач для конкретного сервера. Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.

Для словаря используйте defaultdict, для очереди — deque.

Функция возвращает полученный словарь с задачами.

Пример:

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))
- defaultdict(, {'voltage': deque([41667, 35364]),
- 'office': deque([36871, 40690, 33850])})