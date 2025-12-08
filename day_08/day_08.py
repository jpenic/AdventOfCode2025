import math

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

num_boxes = len(lines)

class JunctionBox():
    def __init__(self, id, x, y, z):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

id_value = 0
junction_boxes = {}
for lines in lines:
    coordinates = lines.split(',')
    new_junction_box = JunctionBox(id_value, coordinates[0], coordinates[1], coordinates[2])
    junction_boxes[new_junction_box.id] = new_junction_box
    id_value += 1

def calculate_euclidian_distance(jb1, jb2):
    return math.sqrt((jb1.x - jb2.x)**2 + (jb1.y - jb2.y)**2 + (jb1.z - jb2.z)**2)

shortest_distances = []

for i in range(0, num_boxes - 1):
    for j in range(i + 1, num_boxes):
        distance = calculate_euclidian_distance(junction_boxes[i], junction_boxes[j])
        shortest_distances.append([distance, i, j])

shortest_distances.sort(key=lambda x: x[0])
# shortest_distances = shortest_distances[:10]
shortest_distances = shortest_distances[:1000]

def get_circuits(distances):
    circuits = []
    for distance, i, j in distances:
        not_in_any_circuit = True
        for circuit in circuits:
            if i in circuit and j not in circuit:
                connected_circuits = False
                for c in circuits: # checking if the other box is already a part of an existing circuit, this means the two circuits need to be connected
                    if j in c:
                        circuit.extend(c)
                        circuits.remove(c)
                        not_in_any_circuit = False
                        connected_circuits = True
                        break
                if not connected_circuits: # else, just add this box to the already found circuit
                    circuit.append(j)
                    not_in_any_circuit = False
                break
            elif j in circuit and i not in circuit:
                connected_circuits = False
                for c in circuits:
                    if i in c:
                        circuit.extend(c)
                        circuits.remove(c)
                        not_in_any_circuit = False
                        connected_circuits = True
                        break
                if not connected_circuits:
                    circuit.append(i)
                    not_in_any_circuit = False
                break
            elif i in circuit and j in circuit: # if the boxes are already in one circuit, do nothing
                not_in_any_circuit = False
                break
        if not_in_any_circuit: # if the current connection wasn't found in any existing circuit, add it as a new one
            circuits.append([i, j])

    circuits.sort(key=lambda x: len(x), reverse=True)
    # print(circuits)
    return circuits

circuits = get_circuits(shortest_distances)

result = 1
for i in range(3):
    result *= len(circuits[i])
print("Result:", result)