#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import os, os.path as p
import json
from core.tools import cvd, wtf


class Interpreter:

    def __init__(self, loc=os.getcwd(), name="index.html"):

        self.loc = loc
        self.name = name
        self.path = p.join(loc, name)

        self.rawHtml = ""

        self.options = {
            "dest": "",
            "filename": ""
        }

        self.DOM = ""
        self.JSON = ""

    def config(self, configpath="config.json"):
        print("loading config")
        with open(p.join(self.loc, configpath), "r") as f:
            self.options = json.loads(f.read())

    def ingest(self):
        self.rawHtml = bs(open(self.path), "html.parser")

    def structure(self, parentid="start"):
        print("generating JSON")
        self.DOM = cvd(self.rawHtml.find(id=parentid))
        self.JSON = json.dumps(self.DOM)

    def write(self):
        print("writing to {0}".format(self.options["dest"]))
        wtf(self.options["dest"], self.JSON, filename="test")
