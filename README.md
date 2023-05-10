Простой **бот**, написанный на `python-telegram-bot v20`

**Бот** анализирует сообщения и отправляет ответ в зависимости от содержания. 

В папке `config` в поле `API` можете указать `HTTP API`, который вам выдал [@BotFather](t.me/BotFather)

## Бот поддерживает следующий функционал

 - Если пользователь отправляет команду  `help`, **бот** отправляет краткое
   описание своих возможностей.    
   
 - Команда `cat` вызывает отправку случайной картинки с котиком. 
 - Отправив фотокарточку, пользователь получит оценку этого фото от **бота**.

Также вы можете дополнить функционал **бота**, для этого перейдите в папку `assets`, и в файле `text_scheme.py` в словаре `scheme` добавьте новый *ключ*, со *списком слов* `list`, наличие хотя бы одного из которых в тексте будет вызывать отправку указанного вами *ответа* `response`.

> Избегайте повторения одинаковых слов в разных *списках*, т.к. **бот** ответит по тому *ключу*, который будет идти в словаре `sheme` раньше, т.е. **случайно**.
