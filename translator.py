import requests

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Translator:
    def __init__(self, token):
        self.url = "https://api-free.deepl.com/v2/translate"
        self.token = token
    
    
    def _execute_api_call(self, text):
        try:
            #raise Exception("error")
            s = requests.Session()
            data = {"target_lang": "EN", "auth_key": self.token, \
                            "text": text}
            response = s.post(self.url, data)
            #result = response.json()['translations'][0]

        except Exception as e:
            print(e)
            return

        return response

    
    def translate(self, text):
        
        result = self._execute_api_call(text)
        if not result:
            return "Was unable to translate"
        elif result.status_code == 200:
            result = result.json()['translations'][0]
            if result['detected_source_language'] == 'EN':
                return
            else:
                return "Translation: " + result['text'] + \
                    " (Translated from " + \
                    result['detected_source_language'] + ")"
        elif result.status_code == 456:
            return 'Quota exceeded, can no longer offer translations this month. Wake me up next month for further translations. Good night!'

    