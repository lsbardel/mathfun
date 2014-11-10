import sys

if sys.version_info[0] == 3:
    from string import ascii_letters
    zip = zip
else:
    from string import letters as ascii_letters
    from itertools import izip as zip
