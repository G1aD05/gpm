import urllib.request as request
import pip
import tarfile
import os
from typing import *


def install(package: str, build_packages: list = Optional[List]):
    os.chdir(f"{os.path.dirname(os.path.abspath(__file__))}/../../build")
    request.urlretrieve(f"https://raw.githubusercontent.com/G1ad05/gpm/refs/heads/master/packages/{package}.tar.gz/", f"{package}.tar.gz")
    with tarfile.open(f"{package}.tar.gz", "r:gz") as tar:
        tar.extractall()

