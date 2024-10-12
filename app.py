"""
Модуль - это веб-приложение на Flask, которое предоставляет следующие функции:
1. Отображает домашнюю страницу.
2. Получает случайный факт о котах из внешнего API.
3. Переводит заданный текст с английского на русский.
4. Получает случайное изображение кота из внешнего API.

Зависимости:
- Flask: Микрофреймворк для создания веб-приложений на Python.
- deep_translator: Библиотека для перевода текста.
- requests: Библиотека для отправки HTTP-запросов.

Маршруты:
- GET /: Отображает домашнюю страницу.
- GET /get_fact: Возвращает случайный факт о котах в формате JSON.
- GET /translate: Переводит заданный текст с английского на русский.
- GET /get_cat_image: Возвращает URL случайного изображения кота в формате JSON.

Использование:
Запустите приложение с помощью команды:
    python3 app.py
Затем доступ к веб-приложению будет открыт по адресу http://127.0.0.1:5000/ в вашем браузере.

Автор: [PressFToCode]
"""

from flask import Flask, render_template, jsonify, request
from deep_translator import MyMemoryTranslator
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fact')
def get_fact():
    response = requests.get('https://catfact.ninja/fact')
    if response.ok:
        fact_data = response.json()
        fact = fact_data['fact']
        return jsonify({'fact': fact})
    return jsonify({'error': 'Не удалось получить факт.'}), 500

@app.route('/translate')
def translate():
    text = request.args.get('text')
    if not text:
        return jsonify({'error': 'Необходимо передать текст для перевода.'}), 400

    translator = MyMemoryTranslator(source='en-GB', target='ru-RU')
    translated_text = translator.translate(text)
    return jsonify({'translatedText': translated_text})

@app.route('/get_cat_image')
def get_cat_image():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.ok:
        image_data = response.json()
        image_url = image_data[0]['url']
        return jsonify({'image_url': image_url})
    return jsonify({'error': 'Не удалось получить изображение.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
