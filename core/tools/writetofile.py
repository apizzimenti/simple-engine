#!/usr/bin/env python3

import os.path as p
from datetime import datetime


def writetofile(path, data, filename="simpleDom", var="simpleDom"):

    prepend = "/* generated by simple-engine {0} */\n".format(datetime.now().time())
    largedata = "{0}var {1} = {2};".format(prepend, var, data)

    with open(p.join(path, filename), "w") as f:
        f.write(largedata)