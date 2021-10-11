Django base project (project)
===========

Базовый проект для создания новых.

# Workflow

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
