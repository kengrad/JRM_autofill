JRM autofill

Script for autofill information in JRM


Перед использованием скрипта убедитесь, что установлены playwright-pytest и pytest
- В файл settings вносим данные о логине пароле и прочем контексте
- запустить скрипт можно командой pytest
- чтобы визуально проследить за работой скрипта, в файле pytest.ini
добавить к параметру addopts аргумент --slowmo 500 (500-количество милисекунд)