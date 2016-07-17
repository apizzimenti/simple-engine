#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import os, os.path as p
import json
from core.tools import wtf
from core.interpreter import cvd


class Interpreter:

    def __init__(self, loc=os.getcwd()):

        self.loc = loc
        self.rawHtml = ""

        self.options = {}

        self.DOM = ""
        self.JSON = ""

    def config(self):
        print("loading config")

        try:
            with open(p.join(self.loc, "engine.json"), "r") as f:
                self.options = json.loads(f.read())
        except FileNotFoundError:
            print("no engine.json in this directory")

    def ingest(self):
        path = p.join(self.loc, self.options["src"])
        self.rawHtml = bs(open(path), "html.parser")

    def structure(self):
        print("generating JSON")
        self.DOM = cvd(self.rawHtml.find(id=self.options["toplevelid"]))
        self.JSON = json.dumps(self.DOM)

    def write(self):
        print("writing to {0}".format(self.options["dest"]))
        wtf(self.options["cwd"], self.JSON, filename=self.options["dest"])
