Итак, приступим к установке зависимостей. Лаба выполняется на винде исключительно из твердых принципов.
1. Качаем миникьюб и используем приложенный ps файл для включения его в PATH.
2. Качаем десктоп версию докера, так как она сразу идет с WSL2.
3. После всех мучений и перезагрузки компьютера можем запускать миникьюб и говорить ему, что мы хотим докер использовать как наш драйвер. (minikube start --driver=docker)

![подьем.png](%D0%BF%D0%BE%D0%B4%D1%8C%D0%B5%D0%BC.png)

4. Далее создаем наш yaml файл и запускаем цмд в этой же папке. (Пример файла опишу в конце, так как переписывал его, чтобы потом поднимались все инстансы сразу) Далее пишем: 

            kubectl apply -f deployment.yaml

5. Получаем наш контейнер и проверяем в нем поды и сервисы:

![запуска одного контейнера.png](%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0%20%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80%D0%B0.png)

6. Далее командой получаем эндпоинт, где сможем проверить наш красивый сервис:

![результат 1 инстанса.png](%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%201%20%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%81%D0%B0.png)

7. Теперь модифицируем yaml файл, добавляя еще два таких же инстанса. Не забываем поменять порты у следующих!

[deployment.yaml](deployment.yaml)

8. Запускаем файлик таким же образом и смотрим как у нас заводятся 3 пода и 3 сервиса из одного файла:

![создаем 3 инстанса сразу.png](%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%B5%D0%BC%203%20%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%81%D0%B0%20%D1%81%D1%80%D0%B0%D0%B7%D1%83.png)

9. Наблюдаем как один из них умер, потому что попал на занятый порт. Не беда, в описании лабы было сказано 2-3.

![пол третьего ночи.png](%D0%BF%D0%BE%D0%BB%20%D1%82%D1%80%D0%B5%D1%82%D1%8C%D0%B5%D0%B3%D0%BE%20%D0%BD%D0%BE%D1%87%D0%B8.png)

10. Получаем от них эндпоинты и проверяем результат. (Поскольку это виндоус, то придется делать в разных окнах cmd :))))

![заходим на инстансы.png](%D0%B7%D0%B0%D1%85%D0%BE%D0%B4%D0%B8%D0%BC%20%D0%BD%D0%B0%20%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%81%D1%8B.png)

11. Готово!