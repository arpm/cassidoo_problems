def makeAPal(base, new=None, c=0):
    if new is None:
        new = base = str.lower(base.replace(" ", ""))
    return c if new == new[::-1] else makeAPal(base, base + base[c::-1], c + 1)

print(makeAPal("Taco"))