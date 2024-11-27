import sys
import gpm.machinery

"""
Nothing here yet
"""
args = []

for arg in sys.argv:
    args.append(arg)

gpm.machinery.parse.parse(args)
