# Некоторые фишки github и markdown

Ссылка на картинку из репозитория github:

![test_image](./img/test.png)

```md
- Иллюстрация к проекту со своей репы
![alt](./img/test.png)

- Иллюстрация к проекту с другой репы
![alt](https://github.com/{username}/{repository}/raw/{branch}/{path}/image.png)

{username} — username цели;
{repository} — название репы где хранится картинка;
{branch} — ветка репы;
{path} — путь к картинке(если она не в корне репы).
```

## GIT CMD

`git update-git-for-windows` проверить обновления git для Windows

`git remote -v` проверить текущий путь к удалённому репо

`git remote rm origin` удалить путь подключения __origin__ к удалённому репо

`git remote add origin_beta [link]` добавить новый путь подключения __origin_beta__ к удалённому репо

`git remote set-url origin [new_link]` задать новый путь подключения __origin__ к удалённому репо (даже если указан старый путь)

`git remote rename [old_name] [new_name]` переименование удалённого подключения с имени __old-name__ на __new-name__

`git rm --cached [file]` игнорировать файл, для которого ранее был сделан коммит(без удаления самого файла)

`git log --all FETCH_HEAD` просмотреть журнал коммитов для всех изменений

`git fetch` извлечение и загрузка содержимого из удалённого репо для просмотра изменений(не применяя эти изменения в локальном репо)

`git pull --all` извлечение и загрузка содержимого из удалённого репо с применением изменений

`git commit --amend -m [new_text]` изменение описания последнего коммита

`git revert [hash_commit]` - отмена коммита с последующим сохранением в журнале

## VERSION

[Семантическое версионирование](https://semver.org/lang/ru/)
