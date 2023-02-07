# Проектная работа: диплом
[ссылка на репозиторий](https://github.com/bdannyv/graduate_work)

## Тема: бронирование билетов

Не всем нравится сидеть дома и смотреть фильмы в одиночку: иногда хочется их посмотреть с компанией единомышленников.
Для добавления такой возможности реализуйте кнопку покупки билета в кино для определенной группы фильмов. Система должна дать пользователю возможность составлять свои расписания, выбирать фильмы и место сбора. Также она должна показывать возможное количество зрителей и позволять пользователю выбирать дату и время просмотра и хоста — того, кто предлагает фильм и место. 
Для данной задачи реализовывать оплату не нужно: достаточно бронировать билеты и не давать забронировать их больше, чем есть мест у конкретного человека. 
В качестве задания «со звёздочкой» придумайте систему оценки пользователя-хоста и пользователя-гостя.


### Функциональные требования
- Покупка билетов на “группу фильмов”
- Составление расписания
- Выбор самого фильма
- Выбор места просмотра
- Выбор времени просмотра
- Возможное количество зрителей выбранного фильма в выбранном кинотеатре в выбранное время
- Выбор хоста
- Система оценки хоста и гостя



### Нефункциональные требования
- запросы не должны отдаваться более 300 миллисекунд

#### Описание архитектуры проекта находится в директории docs/architecture

## Запуск проекта
Для запуска проекта воспользуйтесь командой 

```bash
make start-local
```
