from flask import Flask, request, jsonify
import argostranslate.package
import argostranslate.translate
from bs4 import BeautifulSoup

app = Flask(__name__)

def translate_text(text, from_code, to_code):
    return argostranslate.translate.translate(text, from_code, to_code)

def translate_html_content(html, from_code, to_code):
    soup = BeautifulSoup(html, 'html.parser')
    for text_element in soup.find_all(string=True):
        if text_element.strip():
            translated_text = translate_text(text_element, from_code, to_code)
            text_element.replace_with(translated_text)
    return str(soup)

@app.route('/translate', methods=['POST'])
def translate_html():
    data = request.json
    if 'html' not in data or 'language' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    html = data['html']
    to_code = data['language']

    from_code = 'en'

    try:
        translated_html = translate_html_content(html, from_code, to_code)
        return translated_html
    except Exception as e:
        return jsonify({"error:": str(e)})


if __name__ == '__main__':
    app.run(debug=True)