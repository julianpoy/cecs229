from plotting import plot

# S = {
# 	2 + 3j,
# 	3 + 3j,
# 	1 + 1j,
# 	2 + 1j,
# 	3 + 1j,
# 	4 + 1j
# }


# plot(S)

from image import file2image as f2i
data = f2i('./img01.png')

pts = [(x + y*1j) - len(data) * 1j for x in range(len(data)) for y in range(len(data[0])) if data[x][y][0] < 120]

plot(pts, 200)


