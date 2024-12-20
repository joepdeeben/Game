def input_assembler(worldmap, scale=0.1):
    objectcoordinates = []  # List to store triangles

    # Iterate over the worldmap with indices
    for z, row in enumerate(worldmap):
        for x, cell in enumerate(row):
            # Ensure cell is iterable (tuple or list); if not, make it a single-element tuple
            if not isinstance(cell, (tuple, list)):
                cell = (cell,)

            # Process each feature in the cell
            for feature in cell:
                if feature == 1:
                    # Define the quad for vertical wall segment
                    wall_quad = [
                        [x * scale, 1 * scale, z * scale, 1],           # Top-left
                        [(x + 1) * scale, 1 * scale, z * scale, 1],     # Top-right
                        [(x + 1) * scale, -1 * scale, z * scale, 1],    # Bottom-right
                        [x * scale, -1 * scale, z * scale, 1]           # Bottom-left
                    ]
                    # Split the wall quad into two triangles
                    objectcoordinates.append([wall_quad[0], wall_quad[1], wall_quad[2]])  # Triangle 1
                    objectcoordinates.append([wall_quad[0], wall_quad[2], wall_quad[3]])  # Triangle 2

                elif feature == 2:
                    # Define the quad for horizontal wall segment
                    wall_quad = [
                        [x * scale, 1 * scale, z * scale, 1],           # Top-left
                        [x * scale, 1 * scale, (z + 1) * scale, 1],     # Top-right
                        [x * scale, -1 * scale, (z + 1) * scale, 1],    # Bottom-right
                        [x * scale, -1 * scale, z * scale, 1]           # Bottom-left
                    ]
                    # Split the wall quad into two triangles
                    objectcoordinates.append([wall_quad[0], wall_quad[1], wall_quad[2]])  # Triangle 1
                    objectcoordinates.append([wall_quad[0], wall_quad[2], wall_quad[3]])  # Triangle 2

                elif feature == 3:
                    # Define the quad for floor (y = -1) and ceiling (y = 1)
                    floor_quad = [
                        [x * scale, -1 * scale, z * scale, 1],          # Bottom-left
                        [(x + 1) * scale, -1 * scale, z * scale, 1],    # Bottom-right
                        [(x + 1) * scale, -1 * scale, (z + 1) * scale, 1],  # Top-right
                        [x * scale, -1 * scale, (z + 1) * scale, 1]     # Top-left
                    ]
                    ceiling_quad = [
                        [x * scale, 1 * scale, z * scale, 1],           # Bottom-left
                        [(x + 1) * scale, 1 * scale, z * scale, 1],     # Bottom-right
                        [(x + 1) * scale, 1 * scale, (z + 1) * scale, 1],   # Top-right
                        [x * scale, 1 * scale, (z + 1) * scale, 1]      # Top-left
                    ]
                    # Split the floor quad into two triangles
                    objectcoordinates.append([floor_quad[0], floor_quad[1], floor_quad[2]])  # Triangle 1
                    objectcoordinates.append([floor_quad[0], floor_quad[2], floor_quad[3]])  # Triangle 2
                    # Split the ceiling quad into two triangles
                    objectcoordinates.append([ceiling_quad[0], ceiling_quad[1], ceiling_quad[2]])  # Triangle 1
                    objectcoordinates.append([ceiling_quad[0], ceiling_quad[2], ceiling_quad[3]])  # Triangle 2

    return objectcoordinates




# Example worldmap
worldmap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, (2, 3), 0, 0, 0, 0, 0, 0, (2, 3), 0],
    [0, (2, 3), 0, 0, 0, 0, 0, 0, (2, 3), 0],
    [0, (2, 3), 0, 0, 0, 0, 0, 0, (2, 3), 0],
    [0, (2, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (2, 3), 0],
    [0, (2, 3), 3, 3, 3, 3, 3, 3, (2, 3), 0],
    [0, (2, 3), 3, 3, 3, 3, 3, 3, (2, 3), 0],
    [0, (2, 3), 3, 3, 3, 3, 3, 3, (2, 3), 0],
    [0, (2, 3), 3, 3, 3, 3, 3, 3, (2, 3), 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# Generate interpreted world with scaling
worldmap_interpreted = input_assembler(worldmap, scale=0.1)
