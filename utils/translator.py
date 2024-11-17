from googletrans import Translator

class TranslatorZhTwToEn:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text):
        translation = self.translator.translate(text, src='zh-tw', dest='en')
        return translation.text

if __name__ == "__main__":
    # Example usage:
    translator = TranslatorZhTwToEn()
    translated_text = translator.translate("你好")
    print(translated_text)