# Некоторые фишки github и markdown

Ссылка на картинку из репозитория github:

```md
![Иллюстрация к проекту](https://github.com/jon/coolproject/raw/master/image/image.png)

![Image alt](https://github.com/{username}/{repository}/raw/{branch}/{path}/image.png)

{username} — ваш ник на ГитХабе;
{repository} — репозиторий где хранятся картинки;
{branch} — ветка репозитория;
{path} — путь к месту нахождения картинки.
```

## CMD

`git remote -v` проверить текущий путь к удалённому репозиторию

`git remote set-url origin [new link]` задать новый путь к удалённому репозиторию
