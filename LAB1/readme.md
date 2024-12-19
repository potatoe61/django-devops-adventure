Начинаем развертку джанго сервера:

call C:\api\.venv\Scripts\activate.bat - активируем венву
pause
waitress-serve --listen=127.0.0.1:8001 testapi.wsgi:application - используем вейтресс вместо стандартного runserver и указываем эндпойнт куда будет все перекидывать с NGINX
pause
cmd /k

Проверям доступность эндпоинта по HTTP.
![Проверка доступности.png](%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D0%B8.png)

Переходим к настройкам NGINX:
Для начала заказываем себе сертификаты, думаю для лабы сойдут и самоподписота. Сертбот на винде сейчас не желает даже давать дистрибутив для скачки.
Через powershell создаем сертификат и через openssl дробим его на серт, ключ и чейн. Их указываем в нашем конфиге NGINX:

ssl_protocols TLSv1.2 TLSv1.3;

ssl_ciphers HIGH:!aNULL:!MD5;

ssl_prefer_server_ciphers on;

ssl_session_cache shared:SSL:1m;

ssl_session_timeout  5m;


ssl_certificate "C:/nginx-1.27.3/nginx.crt";

ssl_certificate_key "C:/nginx-1.27.3/nginx.key";

ssl_trusted_certificate "C:/nginx-1.27.3/nginx.chain.crt";


Дальше добавляем алиас для статического контента (Одного надеюсь хватит - работает же:))

location /static/ {
alias C:\api\.venv\testapi\static;
}

Затем принудительную переадресацию с HTTP:

server {
        listen 8080;
        server_name localhost;
        return 301 https://$host$request_uri;
    }

Добавляем второй сервер блок для обработки второго "доменного имени" на одном сервере (в первом будет локалхост, на втором айпишник локальной сети):

server {
listen 443 ssl;
server_name 192.168.0.138;

        ssl_certificate "C:/nginx-1.27.3/nginx.crt";
        ssl_certificate_key "C:/nginx-1.27.3/nginx.key";

        location / {
            proxy_pass http://django;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias C:\api\.venv\testapi\static; 
        }
    }

Готово! Пробуем запуститься: start nginx
Файл с процесс айди появляется - ошибок нет. Проверяем наш сервер:

Берем наш любимый постман и пытаемся обратиться по порту 443 (выключаем проверку сертификата на подлинность по понятным причинам)
Результат успешный:
![постман на 443.png](%D0%BF%D0%BE%D1%81%D1%82%D0%BC%D0%B0%D0%BD%20%D0%BD%D0%B0%20443.png)

Пробуем постучаться через http. Для этого выключаем авторедирект в настройках и получаем 301 ответ с редиректом:
![постман на HTTP.png](%D0%BF%D0%BE%D1%81%D1%82%D0%BC%D0%B0%D0%BD%20%D0%BD%D0%B0%20HTTP.png)

Пробуем сходить на сервер через наш айпи локалки:
![Второй сервер блок.png](%D0%92%D1%82%D0%BE%D1%80%D0%BE%D0%B9%20%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%20%D0%B1%D0%BB%D0%BE%D0%BA.png)

Алиас на джанго не проверить, т.к. он защищает файлы от прямого доступа, но надеюсь по файлику принцип настройки понятен.

Полный файлик NGINX:
[nginx.conf](nginx.conf)
