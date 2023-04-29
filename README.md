## В проекте реализованы API и UI тесты для сайта https://reqres.in/


Общая настройка для запуска тестов :

В командной строке прописать :

1.  pip install poetry

2.  poetry lock

3.  poetry install 

Для запуска тестов из командной строки необходимо прописать : 

-  для запуска API тестов на проверку пользователей : pytest tests/api_tests/tests_reqres_users.py 

-  для запуска API тестов на проверку ресурса : pytest tests/api_tests/tests_reqres_resource.py 

-  для запуска комбинированных тестов, проверяющих соответствие тела ответа и статус кода при API и UI тестах : pytest tests/combined_tests/tests_combined.py 

-  для запуска UI тестов : pytest tests/ui_tests/test_ui.py 

---

В целях увеличения тестовых данных и оптимизации кода, в проекте реализована параметризация тестов и фикстуры с использованием Pytest.
Кроме этого, используется Page Object модель архитектуры проекта, которая позволяет оптимизовать код и его поддержу и в будущем масштабировать проект путем добавления новых страниц и/или версий API.

---

В целях удобства выборки тестов для прогона, некоторые тесты были маркированы : 

Например, для запуска негативных проверок для API, пропишите в командной строке : pytest tests/tests_api/tests_reqres_users.py -m negative

Для запуска медленных API тестов : pytest tests/tests_api/tests_reqres_users.py -m slow

Для запуска проверок json схемы : pytest tests/tests_api/tests_reqres_users.py -m schema

---

Для просмотра отчета о прохождении тестов в командной строке пропишите : allure.bat serve allure-results

![Альтернативный текст](https://github.com/andrechizh8/IBS/blob/main/readme_files/ibs_1.png)


![Альтернативный текст](https://github.com/andrechizh8/IBS/blob/main/readme_files/ibs_2.png)

После прохождения UI и комбинированных тестов есть возможность посмотреть логи :

![Альтернативный текст](https://github.com/andrechizh8/IBS/blob/main/readme_files/ibs_3.png)




