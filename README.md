# Знакомство с Jenkins 

## В порядке очереди: 

```bash
1) Создаем проект новый или через git clone 
2) Если через git clone, то создаем виртуальное окружение: 

- python3 -m venv .venv
- source .venv/bin/activate

3) команда для проверки с каким репозиторием связан проект

- git remote -v

4) ставим все зависимости: 

- pip install -r requirements.txt

должен быть создан файл requirements.txt с содержанием примерным: 

selene==2.0.0rc9
pytest
allure-pytest

5) не забываем создать сразу файлик pytest.ini

[pytest]
addopts =
    --clean-alluredir
    --alluredir=allure-results
    
6) с уже установленным Allure команда для генерации отчета 

allure serve allure-results/ 

7) создаем проект на Jenkins
 - заполняем в разделе Source Code Management - git и ссылку на репозиторий 
 
 - раздел Branches to build - меняем */master на */main
 
 - добавляем в шаги execute shell 
 
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest .
    
 - Post-build Actions - выбираем Allure reports и path allure-results

```