Django base project (project)
===========

Базовый проект для создания новых.

## Workflow

* Проверить зависимости и обновить их
  + Просмотр зависимостей, которые можно обновить:
    ```shell
    $ poetry show --outdated
    ```
  + Обновить зависимости всех заблокированных версий:
    ```shell
    $ poetry update
    ```

* Разработку удобно вести в ветки `development`.

  Если используются динамические переменные, их удобно называть `cookiecutter_{переменная}`.
  Например: `cookiecutter_project_name` заменится на `{{ cookiecutter.project_name }}` заменой по проекту.

* После добавления нового кода в ветке `development`, вручную мержим изменения в основную ветку.

## Как начать проект?

1. Установить зависимости

  ```shell
    $ (venv) pip install cookiecutter jinja2_git
  ```

2. Создать проект по шаблону:

  ```shell
    $ (venv) cookiecutter ssh://git@bitbucket.srvhub.tools:7999/srv/django_skeleton.git
  ```

или, если нужно получить шаблон из конкретной ветки:

  ```shell
    $ (venv) cookiecutter ssh://git@bitbucket.srvhub.tools:7999/srv/django_skeleton.git --checkout cookiecutter
  ```

3. Создать свой `docker-compose-dev.yml` на основе `docker-compose-dev.yml.example` и запустить.
4. Создать свой `local.py` на основе `src/{project_name}/settings/local.py.example`.
5. Установить зависимости:

  ```shell
    $ (venv) cd src/
    $ (venv) /src$ poetry install --no-root
  ```

6. Выполнить миграции:

  ```shell
    $ (venv) /src$ python manage.py migrate
  ```

### Для PyCharm

#### 1. Создать конфигурацию Django:

+ Add new configuration - Django/Server:

   ```
     Host: 0.0.0.0
     Port: 8001 (например)
   ```

+ Django Settings:

   ```
     Django project root: {project_directory}/src
     Settings: {project_name}/settings
     Manage script: manage.py
   ```

+ Для подсветки синтаксиса:

   ```
     ПКМ -> src -> Mark Directory as -> Sources Root
   ```

#### 2. Создать конфигурацию Celery:

+ Add new configuration - Python:

   ```
     Script path: {project_directory}/venv/bin/celery
     Parameters: -A project worker -l debug --queues=celery,emails --events
     Working directory: {project_directory}/src
   ```
