from .install import install


def parse(args: list):
    if args[1] == "install":
        install(args[2])
