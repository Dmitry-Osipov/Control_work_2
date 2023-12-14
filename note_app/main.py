import argparse
from note import *

def main():
    """
    Функция запускает работу с парсером консоли для записи или чтения заметок в JSON.
    """
    parser = argparse.ArgumentParser(
        description="Чтение и запись заметок в JSON\n"
                    "Общий синтаксис записи: python3 main.py <действие> <имя файла> "
                    "--<аргументы функции(опционально)> <значение аргументов(опционально)>"
    )

    parser.add_argument('action',
                        choices=['add', 'update', 'delete', 'read_all', 'read_by_date', 'delete_all'],
                        help='Доступные действия: add, update, delete, delete_all, read_all, read_by_date')
    parser.add_argument('file_name', help='Имя JSON-файла без указания расширения')
    parser.add_argument('--id', type=int, help='ID заметки для обновления или удаления')
    parser.add_argument('--title', help='Название заметки для добавления или обновления')
    parser.add_argument('--body', help='Тело заметки для добавления или обновления')
    parser.add_argument('--date', help='Дата для чтения списка заметок по дате')
    parser.add_argument('--desc', action='store_true',
                        help='Сортировка в порядке убывания даты для чтения')

    args = parser.parse_args()

    if args.action in ['add', 'update']:
        writer = JSONWriter(args.file_name)
        if args.action == 'add':
            if args.title is None or args.body is None:
                print('Для добавление записи необходимо указать --title и --body')
            else:
                writer.add(args.title, args.body)
        elif args.action == 'update':
            if args.id is None or args.title is None or args.body is None:
                print('Для обновления необходимо указать --id, --title и --body')
            else:
                writer.update(args.id, args.title, args.body)

    elif args.action == 'delete':
        if args.id is None:
            print('Чтобы удалить заметку, необходимо указать --id')
        else:
            writer = JSONWriter(args.file_name)
            writer.delete(args.id)

    elif args.action == 'delete_all':
        writer = JSONWriter(args.file_name)
        writer.delete_all()

    elif args.action in ['read_all', 'read_by_date']:
        reader = JSONReader(args.file_name)
        if args.action == 'read_all':
            reader.read_all(args.desc)
        elif args.action == 'read_by_date':
            if args.date is None:
                print('Для чтения по дате необходимо указать --date в формате \"YYYY-MM-DD\"')
            else:
                reader.read_by_date(args.date, args.desc)

if __name__ == "__main__":
    main()
