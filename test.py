#!/usr/bin/env python
# -*- conding: UTF-8 -*-
# 2014-03-22 xiaom #



#�����һ��git�����ļ�


# -- testcase -- #
import unittest
class   TestTest(unittest.TestCase):
    def setUp(self):
        pass


if  __name__ == "__main__":
    suite   = unittest.makeSuite(TestTest, "test")
    runner  = unittest.TextTestRunner()
    runner.run(suite)
