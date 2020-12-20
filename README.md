# otus_dev_ci

<h1>CI (GitHub Actions)</h1>
Процесс CI <br>
1. Сделать пуш в main <br>
2. Стригирятся github actions (установятся зависимости и запустятся тесты).<br>

<h1>CI + CD (Travis, Coverrals, DockerHub) </h1>
Процесс CI/CD <br>
1. Запустить сервис для скачивания и установки контейра докер на локальном host (https://github.com/toropow/otus_webhook). <br> 
2. Запустить ngrok и обновить url в .travis.yml <br>
3. Сделать commit в ветку main. Запустится travis ci. <br>
4. После установки и прогона тестов(+ покрытие в coveralls) докер-образ запушится в docker registry. <br> 
5. После пуша нового образа прозойдет обращение по API, и на локальном хосте запустится образ docker.  <br>
 
[![Build Status](https://travis-ci.org/toropow/otus_dev_ci.svg?branch=main)](https://travis-ci.org/toropow/otus_dev_ci)
[![Coverage Status](https://coveralls.io/repos/github/toropow/otus_dev_ci/badge.svg?branch=main)](https://coveralls.io/github/toropow/otus_dev_ci?branch=main)