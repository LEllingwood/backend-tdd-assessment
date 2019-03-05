#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "LEllingwood"

import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def isUpper(text):
    return text.upper()


def isLower(text):
    return text.lower()


def isTitle(text):
    return text.title()


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()
    
    # result = args.text

    if not args:
        parser.print_usage()
        sys.exit(1)
        
    if args.upper:
        print isUpper(args.text)
        # result = result.upper  PM method

    if args.lower:
        print isLower(args.text)
    
    if args.title:
        print isTitle(args.text)


if __name__ == '__main__':
    main(sys.argv[1:])
