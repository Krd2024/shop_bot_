import telebot


class TelegramBotWrapper:
    _instance = None

    def __new__(cls, token):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance = telebot.TeleBot(token)
        return cls._instance

    def __getattr__(self, name):
        return getattr(self._instance, name)
