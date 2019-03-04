#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo

# Your test case class goes here

class TestStringMethods(unittest.TestCase):
    def test_isUpper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('heLlo'.isupper())

    def test_isLower(self):
        self.assertTrue('hello'.islower())
        self.assertFalse('HEllo'.islower())

    def test_isTitle(self):
        self.assertTrue('This Is String'.istitle())
        self.assertFalse('this Is String'.istitle())

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
    unittest.main()
