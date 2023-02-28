"===CRUD==="
# creat - создать
# read -  читать
# update - обновлятьк
# delate  - удаление

from products import create ,read

while True:
    oper = input("Создать/Читать/Обновлять/Удаленте:")
    if oper == 'Создать':
        create()
    elif oper=='Читать':
        read()

