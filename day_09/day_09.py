with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

class RedTile():
    def __init__(self, id, x, y):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)

red_tiles = {}
id_counter = 0
for line in lines:
    coordinates = line.split(',')
    new_tile = RedTile(id_counter, coordinates[0], coordinates[1])
    red_tiles[id_counter] = new_tile
    id_counter += 1

def calculate_area(tile1, tile2):
    return (abs(tile1.x - tile2.x) + 1) * (abs(tile1.y - tile2.y) + 1)

areas = []

for i in range(0, len(red_tiles) - 1):
    for j in range(i + 1, len(red_tiles)):
        area = calculate_area(red_tiles[i], red_tiles[j])
        areas.append([area, i, j])

# print(areas)
areas.sort(key=lambda x: x[0], reverse=True)

largest_area = areas[0][0]
print("Largest area possible:", largest_area)
corner_coordinates1 = (red_tiles[areas[0][1]].x, red_tiles[areas[0][1]].y)
corner_coordinates2 = (red_tiles[areas[0][2]].x, red_tiles[areas[0][2]].y)
print("Corner coordinates 1:", corner_coordinates1)
print("Corner coordinates 2:", corner_coordinates2)
