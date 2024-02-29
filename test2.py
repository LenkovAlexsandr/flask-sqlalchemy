from flask import


print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())