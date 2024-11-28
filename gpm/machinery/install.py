import urllib.request as request
import pip
import tarfile
import os
from typing import *
import json


def install(package: str, build_packages: list = Optional[List]):
    os.chdir(f"{os.path.dirname(os.path.abspath(__file__))}/../../packages")
    request.urlretrieve(f"https://raw.githubusercontent.com/G1ad05/gpm/refs/heads/master/packages/{package}.tar.gz/", f"{package}.tar.gz")
    with tarfile.open(f"{package}.tar.gz", "r:gz") as tar:
        tar.extractall()
    os.chdir(package)
    with open("manifest.json", "r") as file:
        contents = json.loads(file.read())
        build_packs = contents["dependencies"]["gpm-packages"]
        if not contents["dependencies"]["python-packages"] == {}:
            for package in contents["dependencies"]["python-packages"]:
                pip.main(["install", package])
