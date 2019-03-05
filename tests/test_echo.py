#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


class TestStringMethods(unittest.TestCase):
    def test_isUpper(self):
        self.assertTrue(echo.isUpper('hello'), 'HELLO')
        self.assertFalse(echo.isUpper('hello'), 'heLLo')

    def test_isLower(self):
        self.assertTrue(echo.isLower('Hello'), 'hello')
        self.assertFalse(echo.isLower('hello'), 'HEllo')

    def test_isTitle(self):
        self.assertTrue(echo.isTitle('This Is String'), 'This Is String')
        self.assertFalse(echo.isTitle('This Is String'), 'this Is string')

    pass


def test_help(self):
    """ Running the program without arguments should show usage. """

    # Run the command `python ./echo.py -h` in a separate process, then
    # collect it's output.
    process = subprocess.Popen(
        ["python", "./echo.py", "-h"],
        stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    usage = open("./USAGE", "r").read()

    self.assertEquals(stdout, usage)

if __name__ == '__main__':
    # test_methods = TestStringMethods()
    # test_methods(args)
    
    unittest.main()

