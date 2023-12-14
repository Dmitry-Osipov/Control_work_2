import json
from os import remove
from datetime import datetime
from pprint import pprint

class JSONWriter:
    """
    Класс предназначен для записи, обновления и удаления заметок в JSON.
    """
    def __init__(self, file_name: str):
        """
        Инициализатор класса автоматически присваивает каждой новой заметке уникальный id. Необходимо передать название
        файла, в который будут записываться заметки без указания расширения.

        :param file_name: Имя файла.
        """
        self.__file_name = file_name + ".json"
        self.__id_file_name = "id.txt"
        self.__id = self._load_id()

    def add(self, title: str, body: str) -> None:
        """
        Метод добавляет заметку с уникальным ID в JSON.

        :param title: Заголовок заметки.
        :param body: Тело заметки.
        """
        self.__id += 1
        new_data = {
            "id": self.__id,
            "title": title,
            "body": body,
            "time create": str(datetime.now()),
            "time update": str(datetime.now()),
        }

        try:
            list_data = JSONReader._reader(self.__file_name)
            list_data['all notes'].append(new_data)

        except FileNotFoundError:
            list_data = {'all notes': [new_data]}

        self._writer(list_data)
        self._save_id()
        print(f'Заметка №{self.__id} успешно добавлена')

    def update(self, note_id: int, new_title: str, new_body: str) -> None:
        """
        Метод обновляет заметку по его ID, устанавливая новое время обновления.

        :param note_id: ID заметки.
        :param new_title: Новый заголовок заметки.
        :param new_body: Новое тело заметки.
        """
        try:
            list_data = JSONReader._reader(self.__file_name)

            flag = False
            for data in list_data['all notes']:
                if data['id'] == note_id:
                    data['title'] = new_title
                    data['body'] = new_body
                    data['time update'] = str(datetime.now())
                    flag = True

            self._writer(list_data)
            print(f'Заметка №{note_id} успешно обновлена') if flag else print(f'Заметка №{note_id} не найдена')

        except FileNotFoundError:
            print('Файл не найден')

    def delete(self, note_id: int) -> None:
        """
        Метод удаляет заметку по ID.

        :param note_id: ID заметки.
        """
        try:
            list_data = JSONReader._reader(self.__file_name)

            flag = False
            for i, data in enumerate(list_data['all notes']):
                if data['id'] == note_id:
                    del list_data['all notes'][i]
                    flag = True

            self._writer(list_data)
            print(f'Заметка №{note_id} успешно удалена') if flag else print(f'Заметка №{note_id} не найдена')

        except FileNotFoundError:
            print('Файл не найден')

    def delete_all(self) -> None:
        """
        Метод удаляет все заметки.
        """
        try:
            remove(self.__file_name)
            print('Все заметки удалены')
        except OSError as e:
            print(f'Ошибка при удалении файла {self.__file_name}: {e}')

    def _save_id(self) -> None:
        """
        Служебный метод сохраняет счётчик ID заметок в отдельный файл.
        """
        with open(self.__id_file_name, 'w') as id_file:
            id_file.write(str(self.__id))

    def _load_id(self) -> int:
        """
        Служебный метод загружает из отдельного файла счётчик ID

        :return: ID заметки.
        :raises FileNotFoundError: Файл не найден по указанному пути.
        """
        try:
            with open(self.__id_file_name, 'r') as id_file:
                return int(id_file.read())
        except FileNotFoundError:
            return 0

    def _writer(self, data: dict) -> None:
        """
        Служебный метод предназначен для записи данных в JSON-файл.

        :param data: Словарь значений для записи данных.
        """
        with open(self.__file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)



class JSONReader:
    """
    Класс предназначен для чтения заметок из JSON-файла.
    """
    __file_name = None

    def __init__(self, file_name: str) -> None:
        """
        Инициализатор класса запрашивает имя файла.

        :param file_name: Имя файла без указания расширения.
        """
        self.__file_name = file_name + '.json'

    def read_all(self, desc: bool = False) -> None:
        """
        Метод производит чтение всех заметок. По умолчанию происходит чтение от старых файлов к новым.

        :param desc: Порядок сортировки. По умолчанию от старых заметок к новым, иначе от новых к старым.
        """
        try:
            list_data = JSONReader._reader(self.__file_name)
            pprint(list_data['all notes'], indent=2) if not desc else pprint(list_data['all notes'][::-1], indent=2)

        except FileNotFoundError:
            print('Файл не найден')

    def read_by_date(self, date: str, desc: bool = False) -> None:
        """
        Метод производит чтение заметок по дате добавления. По умолчанию происходит чтение от старых файлов к новым.

        :param date: Дата обновления в формате "YYYY-MM-DD"
        :param desc: Порядок сортировки. По умолчанию от старых заметок к новым, иначе от новых к старым.
        """
        try:
            list_data = JSONReader._reader(self.__file_name)

            result = list()
            for data in list_data['all notes']:
                if data['time create'][:10] == date:
                    result.append(data)

            if result:
                pprint(result, indent=2) if not desc else pprint(result[::-1], indent=2)
            else:
                print('Заметок по этой дате не обнаружено')

        except FileNotFoundError:
            print('Файл не найден')

    @staticmethod
    def _reader(file_name: str) -> dict[str, list]:
        """
        Служебный статичный метод читает данные из JSON-файла.

        :param file_name: Имя файла в формате *.json
        :return: Словарь. Ключ - 'all notes', значение - список из словарей, каждый словарь - это заметка.
        :raises FileNotFoundError: Файл не найден по переданному пути.
        """
        with open(file_name, 'r') as file:
            list_data = json.load(file)

        return list_data
