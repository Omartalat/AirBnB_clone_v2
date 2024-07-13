#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import *
from os.path import isdir


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    try:
        day = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_N = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(file_N))
        return file_N
    except FileNotFoundError:
        return None
