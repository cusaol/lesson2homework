"""
Creați o aplicație care va traduce textul.
Aplicația ar trebui să ceară utilizatorului limba țintă dintr-o listă de opțiuni. (Puteți decide ce opțiuni sunt
disponibile)
Aplicația ar trebui să permită utilizatorului să introducă orice text de lungime sau să furnizeze calea către un
fișier (fișier textual pentru traducere)
Scrieți codul ca o bibliotecă, astfel puteți avea funcții precum:
* get_all_languages
* translate(text, to_language)
* translate_file(path, to_language)
"""
import requests

def get_translated_text(text):
    url = "https://rapidapi.com/googlecloud/api/google-translate1"
    to_language = input('Choose target language: de/ro/en/ru/el/es/hi/it/ja/ka: ')
    payload = {
        "q": text,
        "target": to_language,
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "a72034e733msh5481bb684166fddp11a87djsn08625c047701",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    return data['data']['translations'][0]['translatedText']

if __name__ == '__main__':
    while True:
        inpt = input('Print END to stop. Text to translate (<=500 string): ')
        if inpt == 'END':
            break
        print(get_translated_text(inpt))