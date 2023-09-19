JRM autofill

Script for autofill information in JRM and Watcher

Предусловия:
Включен офисный ВПН


Перед использованием скрипта убедитесь, что:
- создано виртуальное окружение
- установлены зависимости из requirements.txt (pip install -r requirements.txt)
- проверьте устанавлены ли браузеры playwright командой: playwright install

Инструкция
- В файл settings вносим данные о логине пароле и прочем контексте
- запустить скрипт можно командой pytest
- чтобы визуально проследить за работой скрипта, в файле pytest.ini
добавить к параметру addopts аргумент --slowmo 500 (где 500 - милисекунды)