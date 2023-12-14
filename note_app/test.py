from note_app.note import *

if __name__ == '__main__':
    writer = JSONWriter('test')
    writer.add('old title', 'old body')
    writer.add('new title', 'new body')

    reader = JSONReader('test')
    reader.read_all()
    writer.update(2, 'super title', 'super body')
    reader.read_all(desc=True)
    reader.read_by_date('2023-12-14')
    reader.read_by_date('2023-12-14', desc=True)
    writer.delete(1)
    reader.read_all()
    writer.delete_all()
    reader.read_all()
