from requests import get, post, delete, put

# все новости
print(get('http://localhost:5000/api/v2/news').json())
# одна новость
print(get('http://localhost:5000/api/v2/news/1').json())
# одна новость которой нет
print(get('http://localhost:5000/api/v2/news/999').json())
# одна новость где id не число
print(get('http://localhost:5000/api/v2/news/jsdfkhgkjsdhgkjsdg').json())
#
# # пустой запрос на добавление новости
# print(post('http://localhost:5000/api/news').json())
# # неполный запрос на добавление новости
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
# # правильный запрос на добавление новости
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1}).json())
#
# # удаляем несуществующую новость
# print(delete('http://localhost:5000/api/news/999').json())
# # удаляем сущесвтующую новость
# print(delete('http://localhost:5000/api/news/2').json())

# пустой запрос на изменение новости
# print(put('http://localhost:5000/api/news/1').json())
# # неполный запрос на изменение новости
# print(put('http://localhost:5000/api/news/1',
#            json={'title': 'Заголовок'}).json())
# # правильный запрос на изменение новости
# print(put('http://localhost:5000/api/news/1',
#            json={'title': 'ПЕЧАЛЬКА ВСЕЛЕНСКАЯ',
#                  'content': 'ПИТССЫ СОВСЕМ НЕТ!!!',
#                  'user_id': 3}).json())