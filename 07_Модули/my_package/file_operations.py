def open_file(s):
    try:
        with open(s) as fin:
            txt = fin.readlines()
            return txt
    except:
        return -1