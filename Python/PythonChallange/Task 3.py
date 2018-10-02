# http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page

guts = open("/ocr.txt").read()
d = {}
for ch in guts:
    d[ch] = d.get(ch, 0) + 1
