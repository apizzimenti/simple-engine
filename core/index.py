#!/usr/bin/env python3

from core import interpreter


def main():
    i = interpreter(name="index.html")
    i.config()
    i.ingest()
    i.structure()
    i.write()
