# Python

## Виртуальное окружение "venv" в "VS Code"

`python -m venv .venv` - создать папку для работы с виртуальным окружением, добавить в конце `--upgrade-deps` если нужен обновлённый __pip__ в __venv__

`.\.venv\Scripts\activate`(_win_) `.venv/bin/activate`(_unix_) - создать виртуальное окружение

`deactivate` - удалить виртуальное окружение

_Если появится ошибка с правами доступа, то выполняем в PowerShell из под админа:_

`Set-ExecutionPolicy RemoteSigned` и вводим "__A__"

`"python.terminal.activateEnvInCurrentTerminal": true` - добавить в settings.json проекта, для автоактивации "__venv__"

## PIP

`pip list` - список всех библиотек Python

`pip freeze` - список установленных библиотек Python

### Создание requirements.txt и его использование

`pip install pipreqs` - установка нужного инструмента для создания этого файла

`pipreqs --savepath requirements.txt` - перед вводом команды сборки файла перейти в папку проекта

`pip install -r requirements.txt` - установка библиотек из этого файла

`pip freeze > requirements.txt` - запись в текстовый файл всех установленных пакетов для Python

`pip install --upgrade -r requirements.txt` - обновление всех пакетов которые указаны в текстовом файле
