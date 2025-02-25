### 1. Не соответствует значение параметра "name" в методе GET /api/1/item/:id созданному объявлению
```
Предусловия:
1. Создано объявление методом POST /api/1/item c телом {"name": "Телефон", "price": 85566, "sellerId": 345971} 
2. Получен ID объявления (4ed533ee-f642-4ad8-b887-d14a6ce1bd08)


Шаги:
1. Выполнить GET-запрос по адресу https://qa-internship.avito.com/api/1/item/:id с id = "4ed533ee-f642-4ad8-b887-d14a6ce1bd08"


Фактический результат:
1. Получены данные 
{
        "createdAt": "2025-02-16 18:05:06.636349 +0300 +0300",
        "id": "4ed533ee-f642-4ad8-b887-d14a6ce1bd08",
        "name": "dsdsd",
        "price": 85566,
        "sellerId": 345971,
        "statistics": {
            "contacts": 0,
            "likes": 0,
            "viewCount": 0
        }
    }
2. Значение "name" в ответе не соответствует значению "name" в теле запроса POST /api/1/item 

Ожидаемый результат:
Значения параметров ответа "name", "price", "sellerId" соответствуют значения параметров запроса POST /api/1/item 
```

### 2. Не соответствует формат даты в параметре "createdAt" в методе GET /api/1/item/:id
```
Шаги:
1. Выполнить GET-запрос по адресу https://qa-internship.avito.com/api/1/item/:id с id = "4ed533ee-f642-4ad8-b887-d14a6ce1bd08"


Фактический результат:
1. Получены данные 
{
        "createdAt": "2025-02-16 18:05:06.636349 +0300 +0300",
        "id": "4ed533ee-f642-4ad8-b887-d14a6ce1bd08",
        "name": "dsdsd",
        "price": 85566,
        "sellerId": 345971,
        "statistics": {
            "contacts": 0,
            "likes": 0,
            "viewCount": 0
        }
    }
2. В параметре "createdAt" присутствуют милисекунды
3. В параметре "createdAt" дублируется таймзона


Ожидаемый результат:
Формат даты соответствует формату "%Y-%m-%d %H:%M:%S %z" ("2025-02-16 18:05:06 +0300") 
```

### 3. Отсутствует валидация на обязательность параметров при создании объявления методом POST /api/1/item
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item без параметра "name"
{
    "price": 1,
    "sellerId": 3452
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано, так как параметры являются обязательными (https://github.com/avito-tech/tech-internship/blob/main/Tech%20Internships/QA/QA-trainee-assignment-winter-2025/swagger.yaml)
3. Получена ошибка "Не передан обязательный параметр"


Комментарии:
Аналогичное поведение при отсутствии любого из обязательных параметров: "name", "price", "sellerId"
```

### 4. Доступно создание объявления с пустым "name" методом POST /api/1/item
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с пустым "name"
{
    "price": 1,
    "sellerId": 3452,
    "name": ""
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано, так как "name" не может быть пустым
3. Получена ошибка "Не передан обязательный параметр"
```

### 5. Доступно создание объявления с "price": null методом POST /api/1/item
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с "price": null
{
    "price": null,
    "sellerId": 3452,
    "name": "Телефон"
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано, так как "price" не может быть null или быть меньше 1
3. Получена ошибка "Не передан обязательный параметр"
```

### 6. Доступно создание объявления с "sellerId": null методом POST /api/1/item
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с "sellerId": null
{
    "price": 12345,
    "sellerId": null,
    "name": "Телефон"
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано, так как "sellerId" не может быть null
3. Получена ошибка "Не передан обязательный параметр"
```

### 7. Не соответствует текст ошибки при создании объявления методом POST /api/1/item с неверным типом данных в параметрах
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с "name": 12345 (число)
{
    "price": 12345,
    "sellerId": 345971,
    "name": "Телефон"
}


Фактический результат:
1. Статус код - 400
2. Текст ошибки - "не передано тело объявлени"


Ожидаемый результат:
1. Текст ошибки - "Передан неверный тип данных у параметра 'name'"


Комментарии:
Аналогичное поведение при передаче любого из параметров с неверным типом данных: "name", "price", "sellerId"
```

### 8. Передается текст ошибки в параметре "status" при создании объявления методом POST /api/1/item с неверным типом данных
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с "name": 12345 (число)
{
    "price": 12345,
    "sellerId": 345971,
    "name": "Телефон"
}


Фактический результат:
1. Статус код - 400
2. Получен ответ 
{
    "result": {
        "message": "",
        "messages": {}
    },
    "status": "не передано тело объявлени"
}
3. Текст ошибки передан в параметре "status"


Ожидаемый результат:
1. Статус код - 400
2. В параметре "result.message" передан текст ошибки "Передан неверный тип данных у параметра 'name'"
3. В параметре "status" передан код ошибки


Комментарии:
Аналогичное поведение при передаче любого из параметров с неверным типом данных: "name", "price", "sellerId"
```

### 9. Отсутствует валидация переданных значений параметров при создании объявления методом POST /api/1/item 
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с невалидным значением "name" (не буквы):
Например,
{
    "name": "!@#$%^&*()",
    "price": 85566,
    "sellerId": 3452
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано
3. Получена ошибка "Передан неверный тип данных у параметра 'name'"


Комментарии:
Аналогичное поведение при передаче невалидного значения для любого из параметров: "name", "price", "sellerId"
Например,
('name', '!@#$%^&*()') - знаки,
('name', '1234567890') - числа в строке,
('name', ' ') - пробел,
('name', 'Ваня Ваня') - два слова,
('name', 'Ва-ня-Ва-ня') - более одного тире в имени,
('name', 'Ваня!Ваня') - имя + знак не тире,
('price', -12345) - отрциательное число,
('sellerId', -12345) - отрциательное число
```

### 10. Отсутствует валидация на граничные значения параметров при создании объявления методом POST /api/1/item
```
Шаги:
1. Выполнить POST-запрос по адресу https://qa-internship.avito.com/api/1/item с "sellerId": 111110:
Например,
{
    "name": "Телефон",
    "price": 85566,
    "sellerId": 111110
}


Фактический результат:
1. Статус код - 200
2. Объявление создано
3. Получен id объявления


Ожидаемый результат:
1. Статус код - 400
2. Объявление не создано
3. Получена ошибка "Превышены допустимые значения у параметра 'sellerId'"
4. Граничные значения 'sellerId' = 111111 - 999999


Комментарии:
Аналогичное поведение при передаче значений для любого из параметров: "name", "price", "sellerId"
Например,
('name', '') - меньше 1 символа,
('name', 'Расположениключевыхсловпогруппамипочастотевключаетв') - больше 50 символов,
('price', 0) - меньше 1 рубля,
('price', 6000000001) - больше 6000000000 рублей
```

### 11. Перепутаны значения параметров "id" и "name" в ответе запроса получения объявлений продавца методом GET /api/1/:sellerID/item
```
Шаги:
1. Получить список объявлений продавца, выполнив GET-запрос по адресу https://qa-internship.avito.com/api/1/:sellerID/item с "sellerID": 345971 (например, 345971)


Фактический результат:
Перепутаны значения параметров "id" и "name"
"id": "dsdsd", - передано название "name"
"name": "4ed533ee-f642-4ad8-b887-d14a6ce1bd08", - передан "id"


Ожидаемый результат:
Значения параметров соответствуют их данным
"id": "4ed533ee-f642-4ad8-b887-d14a6ce1bd08", - передан "id"
"name": "dsdsd", - передано название "name"
```


### 12. Не соответствует значение "name" в ответе запроса получения объявлений продавца методом GET /api/1/:sellerID/item у добавленного объявления
```
Шаги:
1. Получить список объявлений продавца, выполнив GET-запрос по адресу https://qa-internship.avito.com/api/1/:sellerID/item с "sellerID": 345971 (например, 345971)
2. Добавить объявление продавцу, выполнив POST-запрос по адресу https://qa-internship.avito.com/api/1/item 
{
    "name": "Телефон",
    "price": 85566,
    "sellerId": 345971 
}
3. Повторно получить список объявлений продавца, выполнив GET-запрос по адресу https://qa-internship.avito.com/api/1/:sellerID/item с "sellerID": 345971
4. Сравнить ответы метода GET /:sellerID/item до и после добавления объявления


Фактический результат:
1. Объявление добавлено
2. Значение параметра "name" ("dsdsd") не соответствует "name" ("Телефон") из добавленного объявления


Ожидаемый результат:
Данные объекта товара соответствуют данным из тела запроса из предусловий  ("name": "Телефон")
```

### 13. Не соответствует текст ответа и код в теле ответа запроса получения объявлений продавца методом GET /api/1/:sellerID/item
```
Шаги:
1. Выполнить GET-запрос по адресу https://qa-internship.avito.com/api/1/:sellerID/item с "sellerID": !@#$%^&*()_+{}|?><,.


Фактический результат:
1. Статус код - 404
2. Получен ответ
{
    "message": "route /api/1/!@ not found",
    "code": 400
}
3. В теле ответа "code": 400


Ожидаемый результат:
1. Статус код - 400
2. Получен ответ (как для других невалидных значений, например, 9999999999999999999999999)
{
    "result": {
        "message": "передан некорректный идентификатор продавца",
        "messages": {}
    },
    "status": "400"
}
