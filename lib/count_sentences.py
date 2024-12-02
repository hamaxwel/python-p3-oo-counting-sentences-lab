import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
        self._value = value if isinstance(value, str) else ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        standardized_value = re.sub(r'[.!?]+', '.', self._value)
        sentences = [s.strip() for s in standardized_value.split('.') if s.strip()]
        return len(sentences)
