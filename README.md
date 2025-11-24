# Лабораторная работа №1  

Барышев Михаил ИУ10-96

## Данная лабораторная работа посвещена изучению систем обмена данными. Работа позволит ознакомиться с базовыми навыками необходимыми для произведения commit changes, публикации изменний в удаленный репозиторий, обновлениями данных для них, fork и тд.

![GitHub repo size](https://img.shields.io/github/repo-size/MishaBary/risk_lab1)
![GitHub last commit](https://img.shields.io/github/last-commit/MishaBary/risk_lab1)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MishaBary/risk_lab1)
![GitHub pull requests](https://img.shields.io/github/issues-pr/MishaBary/risk_lab1)
![GitHub contributors](https://img.shields.io/github/contributors/MishaBary/risk_lab1)


## Задание

- [x] 1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется
- [x] 2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации
- [x] 3. Отправить зарегистрированный адрес почтового ящика личным сообщением
- [x] 4. Отправить зарегистрированный логин личным сообщением
- [x] 5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания
- [x] 6. Сгенерировать **SSH** ключ и добавить его в список ключей для сервиса **GitHub**
- [x] 7. Сгенерировать **Personal Token** с правами **gist** и сохранить его в файл
- [x] 8. Сгенерировать GnuPG для подтверждения подписания коммитов и возможно использование Х.509 (включить в отчет описание, что такое `smimesign`)
- [x] 9. Подготовить глобальные переменные окружения для **GitHub**
- [x] 10. Ознакомиться с материалами `gh` сервиса и использовать их для авторизации, `commit`, `pull request` и тд.
- [x] 11. Выполнить инструкцию учебного материала
- [x] 12. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [x] 13. Составить `gist` отчет и отправить ссылку личным сообщением

## Выполнение задания

1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется
2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации
3. Отправить зарегистрированный адрес почтового ящика личным сообщением
4. Отправить зарегистрированный логин личным сообщением
5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания
6. Сгенирировать **SSH** ключ и добавть его в список ключей для сервиса **GitHub**
```bash
ssh-keygen -t ed25519 -C "mbtrud@mail.ru"
```

**Результат выполнения команды:**
- Создан SSH ключ в директории `~/.ssh/`
- Публичный ключ сохранен в `id_ed25519.pub`
- Ключ добавлен в GitHub Settings → SSH and GPG keys

7. Сгенирировать **Personal Token** с правами **gist** и сохранить его в файл

**Процесс создания Personal Access Token:**
1. Перейти в GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Нажать "Generate new token (classic)"
3. Выбрать права доступа: `gist, repo`
4. Сгенерировать токен и сохранить его в файл (токен показывается только один раз)

8. Сгенерировать GnuGP для подтверждения подписания коммитов и возможно использование Х.509 (включить в отчет описание, что такое `smimesign`)

**Генерация GPG ключа:**
```bash
gpg --full-generate-key
# Выбрать тип ключа: RSA and RSA
# Размер ключа: 4096
```

**Просмотр списка GPG ключей:**
```bash
gpg --list-secret-keys --keyid-format=long
# Скопировать ID ключа
gpg --armor --export <KEY_ID>
# Добавить публичный ключ в GitHub Settings → SSH and GPG keys
```

`smimesign` — инструмент для подписи Git-коммитов с помощью сертификатов
X.509 / S/MIME, в отличие от GPG. Используется в корпоративных политиках.
GitHub распознаёт такие подписи как Verified.

9. Подготовить глобальные переменные окружения для **GitHub**

```bash
git config --global user.name ""
git config --global user.email ""
git config --global commit.gpgsign true
git config --global user.signingkey <GPG_KEY_ID>
```

**Проверка настроек:**
```bash
git config --global --list
```

10. Ознакомиться с материалами `gh` сервиса и использовать их для авторизации, `commit`, `pull requeste` и тд.
```bash 
gh auth login
gh auth status 
```

**Результат авторизации:**
    - Выбрать GitHub.com
    - Выбрать способ авторизации (браузер или токен)
    - После успешной авторизации `gh auth status` покажет:
        - Аккаунт GitHub
        - Токен: Valid
        - Git operations: Authenticated

11. Выполнить инструкцию учебного материала

12. Оформить `README.md` по аналогии и использовать `shield`, etc.

13. Составить `gist` отчет и отправить ссылку личным сообщением.

## Задание Ч.2
1. Создайте локальный репозиторий на машине + 2. Проинициализируйте репозиторий
``` bash
mkdir risk_lab1
cd risk_lab1
git init
```
3. Авторизуйтесь и используйте `GitHub CLI` для создания удаленного 
``` bash
gh repo create risk_lab1 --public
```
4. Создайте пустой README.md + 7. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий
``` bash
touch README.md
git add README.md
git commit -S -m ""
git push -u origin master
```
5. Используйте указание URL своего созданного репозитория для присвоения ветки `master` статуса `origin` + 6. В локальном репозитории и сделайте `commit`
``` bash
git branch -M master
git remote add origin https://....
```
8. Создайте файл `hello.py` в локальном репозитории. Реализуйте **Hello appsec world** на языке python используя несколько интерпретаторов с "грязным" кодом + 9. Сделайте `commit` с флагом `-S`

**Пример "грязного" кода:**
```python
print ("Hello    appsec   world")

for i in [  "Hello" ,   "appsec", "world"   ]:
        print(i),

import sys
def run():
	name="appsec"
	sys.stdout.write("Hello "+ name +" world")
run()
```

10. Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил `Hello appsec world from @name` + 11. Сделайте `commit` с флагом `-S` и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений.

**Обновленный код:**
```python

name = input("Введите ваше имя: ")
print(f"Hello appsec world from @{name}")
```

**Команды для коммита и публикации:**
```bash
git add hello.py
git commit -S -m "Добавлен запрос имени пользователя"
git push -u origin master
git log --oneline --graph --all
```

12. В локальном репозитории создайте ветку `patch1` и внесите изменения исправлению кода и модернизации до следующего вида, что бы код был рабочим. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий.
``` bash
git checkout -b patch1
git add hello.py
git commit -S -m ""
git push -u origin patch1
```

13. Проверьте, что ветка `patch1` в удалённом репозитории. Создайте `pull-request` в виде `patch1 -> master`. В ветке `patch1` добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в `pull-request`. В удалённый репозитории выполните слияние `pull-request` для `patch1 -> master` и удалите ветку `patch1`

**Создание Pull Request:**
```bash
gh pr create --base master --head patch1 --title "..." --body "..."
```

14. Стяните последние актуальные изменения и просмотрите историю изменений для `master`

```bash
git pull origin master
git log --oneline --graph --all --decorate
```

**Результат:**
- Получены последние изменения из удаленного репозитория
- История коммитов показывает слияние ветки `patch1` в `master`
- Все коммиты подписаны (Verified)

15. Удалите локальную ветку `patch1`

16. Создайте новую локальную ветку `patch2`. Измените *code style* по своему усмотрению. Сделайте публикацию своего `commit` с флагом `-S` в удаленный репозиторий и создайте pull-request `patch2 -> master`
``` bash
git checkout -b patch2
git add hello.py
git commit -S -m ""
git push -u origin patch2

gh pr create --base master --head patch2
```
17. В ветке **master** удаленного репозитория явно измените комментарий. Увидите, что в `pull-request` появились расхождения. Локально сделайте **rebase** и исправьте расхождения (это называется **конфликт**). Сделайте `commit` и опубликуйте изменения в ветке `patch2`.

**Процесс rebase с разрешением конфликтов:**
```bash
git checkout patch2
git rebase master
# При возникновении конфликта:
# 1. Открыть файл hello.py и разрешить конфликт вручную
# 2. git add hello.py
# 3. git rebase --continue
# 4. git push --force-with-lease origin patch2
```

**Пример конфликта в файле:**
```
<<<<<<< HEAD
# Комментарий из master
=======
# Комментарий из patch2
>>>>>>> patch2
```

После разрешения конфликта и продолжения rebase, изменения будут применены поверх последнего коммита в master.

18. Убедитель, что пропали конфликтны. 
19. Сделайте `merge` для `pull-request` `patch2 -> master`.
20. Подготовьте отчет `gist`.
21. Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.

**История коммитов в удаленном репозитории (GitHub):**
```bash
https://github.com/MishaBary/risk_lab1/commits/master
```

**История коммитов в локальном репозитории:**
```bash
git log --oneline --graph --all --decorate
```

