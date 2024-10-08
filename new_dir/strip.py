noms = [
    " Alice  ",
    "   Bob  ",
    "   Charlie ",
    "  David  ",
    "   Eve   ",
    "Frank ",
    "  Grace   ",
    "Hannah   ",
    "   Ian",
    "  Julia  "
]

noms_optimized = [item.strip().upper() for item in noms]

print(noms_optimized)
