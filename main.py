import json
import xml.etree.ElementTree as ET
import xml.dom.minidom

class Library:
  def __init__(self, purpose, title, author, year):
      self.purpose = purpose
      self.title = title
      self.author = author
      self.year = year

  def to_dict(self):
      return {
          'purpose': self.purpose,
          'title': self.title,
          'author': self.author
      }

class Book(Library):
  def __init__(self, purpose, title, author, year, genre, length):
    super().__init__(purpose, title, author, year)
    self.genre = genre
    self.length = length
    
  def to_dict(self):
    book = super().to_dict()
    book.update({
      'purpose': self.purpose,
      'title': self.title,
      'author': self.author,
      'year': self.year,
      'genre': self.genre,
      'length': self.length
    })
    return book

class Magazine(Library):
  def __init__(self, purpose, title, author, year, type, release):
    super().__init__(purpose, title, author, year)
    self.type = type
    self.release = release

  def to_dict(self):
    magazine = super().to_dict()
    magazine.update({
      'purpose': self.purpose,
      'title': self.title,
      'author': self.author,
      'year': self.year,
      'type': self.type,
      'release': self.release
    })
    return magazine

book_1 = Book("Student", "Python for beginners", "Author 1", 2002, "Stydy", 105)
book_2 = Book("Student", "C++ for beginners", "Author 2", 1999, "Stydy", 110)
magazine_1 = Magazine("Girls", "Everything for fashion", "Author 3", 2023, "Fashion", 5)
magazine_2 = Magazine("Girls", "Beauty and fashion", "Author 3", 2023, "Fashion", 8)

# создаем словарь из объектов классов
dict_library = {
    "books": [book_1.to_dict(), book_2.to_dict()],
    "magazins": [magazine_1.to_dict(), magazine_2.to_dict()]
}

# сохраняем данные в файл JSON
with open('library_out.json', 'w') as f:
  json.dump(dict_library, f, indent=4)

# обработка ошибки открытия файла
try:
    # чтение из файла input.json
    with open('library_input.json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            print(line)
except FileNotFoundError:
    print("File not found")

# Создаем XML-структуру
# Циклs для обработки каждого объекта
root = ET.Element("library") #Создаем корневой элемент
for book in [book_1, book_2]: #Итерация по списку книг
  book_element = ET.SubElement(root, "book") #создаем новый подэлемент под корнем
  for key, value in book.to_dict().items(): #итерация по парам ключ-значение
    ET.SubElement(book_element, key).text = str(value) #Для каждой пары ключ-значение создаем новый подэлемент,  

for magazine in [magazine_1, magazine_2]:
  magazine_element = ET.SubElement(root, "magazine")
  for key, value in magazine.to_dict().items():
      ET.SubElement(magazine_element, key).text = str(value)
    
tree = ET.ElementTree(root)

with open('library.xml', 'wb') as f:
  tree.write(f)

with open('library.xml', 'r', encoding='utf-8') as f:
  # Читаем содержимое файла и сохраняем его в переменную xml_string
  xml_string = f.read()
  # Создаем объект DOM из строки XML (Возвращает объект Document, представляющий структуру этого документа.)
  dom = xml.dom.minidom.parseString(xml_string)
  # Преобразуем объект DOM в строку форматированного XML с заданными отступами
  # и сохраняем его в переменную pretty_xml_string
  pretty_xml_string = dom.toprettyxml(indent='  ')
  # Выводим строку форматированного XML на экран
  print(pretty_xml_string)