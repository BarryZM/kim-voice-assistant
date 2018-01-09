# -*- coding: utf-8-*-
import unittest
import os
os.sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from src.tts import TTSEngine
from utils import logger
from threading import Thread
from time import sleep


class TestTTSEngine(unittest.TestCase):
    """

    """

    def setUp(self):
        self.tts_engine = TTSEngine.get_instance()

    def test_fetch_speech_wave(self):
        """
        测试获取语音
        :return:
        """
        result = self.tts_engine.fetch_speech_wave('你好世界')
        print(result)


if __name__ == '__main__':
    logger.init(info=True)
    unittest.main()

