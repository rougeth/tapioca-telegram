# coding: utf-8

import unittest

from tapioca_telegram_bot_api import TelegramBotApi


class TestTapiocaTelegramBotApi(unittest.TestCase):

    def setUp(self):
        self.wrapper = TelegramBotApi()


if __name__ == '__main__':
    unittest.main()
