for 25 rows
end4sand9s = [99, 104, 109, 114, 119, 124, 129]
for col in end4sand9s:
    text = rotateColumn(text, col, 1)

end1sand6s = [96, 91, 86]
for col in end1sand6s:
    text = rotateColumn(text, col, 24)

ends3sand8s = [68, 73, 78, 83, 88, 93]
for col in ends3sand8s:
    text = rotateColumn(text, col, 24)


shiftsDown = []
for col in shiftsDown:
    text = rotateColumn(text, col, 24)

shiftsUp = [4, 100]
for col in shiftsUp:
    text = rotateColumn(text, col, 1)

# Block Shifts
finalBlock = range(66, 98)
for col in finalBlock:
    text = rotateColumn(text, col, 1)

penultimateBlock = range(45, 66)
for col in penultimateBlock:
    text = rotateColumn(text, col, 1)

# secondBlock = range(0,34)
# for col in secondBlock:
#     text = rotateColumn(text, col, 1)
