def find_index(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def region(flake_loc_x, flake_loc_y):
    flake_regions = []
    for i in range(len(flake_loc_x)):
        if flake_loc_x[i] <= 256:
            if flake_loc_y[i] <= 341:
                flake_regions.append("UL")
            elif flake_loc_y[i] <= 682:
                flake_regions.append("UM")
            else:
                flake_regions.append("UR")
        elif flake_loc_x[i] <= 512:
            if flake_loc_y[i] <= 341:
                flake_regions.append("ML")
            elif flake_loc_y[i] <= 682:
                flake_regions.append("MM")
            else:
                flake_regions.append("MR")
        else:
            if flake_loc_y[i] <= 341:
                flake_regions[i].append("BL")
            elif flake_loc_y[i] <= 682:
                flake_regions.append("BM")
            else:
                flake_regions.append("BR")
    
    return flake_regions

# create class of flakes
class flakes:
    def __init__(self, image, mag, thickness, l_side, num_flakes, 
location):
        self.image = image
        self.mag = mag
        self.thickness = thickness
        self.l_side = l_side
        self.num_flakes = num_flakes
        self.location = location
    
