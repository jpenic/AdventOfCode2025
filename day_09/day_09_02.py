import matplotlib.pyplot as plt

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

xs = [red_tiles[id].x for id in red_tiles]
ys = [red_tiles[id].y for id in red_tiles]
plt.plot(xs, ys)
# data shows there are two obvious outliers
# one of them will be a corner in the rectangle

outliers = []
previous_x = red_tiles[0].x
for tile_id in red_tiles:
    if abs(red_tiles[tile_id].x - previous_x) > 20000:
        outliers.append(red_tiles[tile_id])
        outliers.append(red_tiles[tile_id + 1])
        break
    else:
        previous_x = red_tiles[tile_id].x

print("Outliers:")
for o in outliers:
    print("ID:", o.id, "X:", o.x, "Y:", o.y)

outlier1 = outliers[0]
outlier2 = outliers[1]

def check_rectangle(corner1, corner2, red_tiles):
    for tile_id in red_tiles:
        if (corner1.x < red_tiles[tile_id].x < corner2.x
                or corner1.x > red_tiles[tile_id].x > corner2.x ) \
            and (corner1.y < red_tiles[tile_id].y < corner2.y
                 or corner1.y > red_tiles[tile_id].y > corner2.y):
            return False
    return True

def calculate_area(tile1, tile2):
    return (abs(tile1.x - tile2.x) + 1) * (abs(tile1.y - tile2.y) + 1)

# for each rectangle, where one of the corners is one of the outliers, check if
# all other red tiles are outside the rectangle, and memorize the largest area found
max_area = 0
max_area_tile_id = 0
outlier_in_result = -1
for tile_id in red_tiles:
    if check_rectangle(red_tiles[tile_id], outlier1, red_tiles):
        curr_area = calculate_area(red_tiles[tile_id], outlier1)
        if curr_area > max_area:
            max_area = curr_area
            max_area_tile_id = tile_id
            outlier_in_result = 1
    if check_rectangle(red_tiles[tile_id], outlier2, red_tiles):
        curr_area = calculate_area(red_tiles[tile_id], outlier1)
        if curr_area > max_area:
            max_area = curr_area
            max_area_tile_id = tile_id
            outlier_in_result = 2

found_corner = red_tiles[max_area_tile_id]

if outlier_in_result == 1:
    rectangle_x = [outlier1.x, outlier1.x, found_corner.x, found_corner.x]
    rectangle_y = [outlier1.y, found_corner.y, found_corner.y, outlier1.y]
else:
    rectangle_x = [outlier2.x, outlier2.x, found_corner.x, found_corner.x]
    rectangle_y = [outlier2.y, found_corner.y, found_corner.y, outlier2.y]

plt.plot(rectangle_x, rectangle_y, color='red')
plt.show()

print("Largest area found is:", max_area)