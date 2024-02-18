from phreeqpy.input import keywords, phreeqpy_help

#keywords.Advection.cells

adv = keywords.Advection()
adv.cells
adv.cells = 1
print adv.cells.__doc__
print adv.cells
phreeqpy_help()
phreeqpy_help(adv, verbose=True)
phreeqpy_help(adv.cells)

