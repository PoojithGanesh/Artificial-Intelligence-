class MapColoringCSP:
    def __init__(self, regions, colors, adjacency):
        self.regions = regions
        self.colors = colors
        self.adjacency = adjacency
        self.assignment = {}
    
    def is_valid(self, region, color):
        for neighbor in self.adjacency.get(region, []):
            if self.assignment.get(neighbor) == color:
                return False
        return True
    
    def backtrack(self):
        if len(self.assignment) == len(self.regions):
            return self.assignment
        
        unassigned = [r for r in self.regions if r not in self.assignment]
        region = unassigned[0]
        
        for color in self.colors:
            if self.is_valid(region, color):
                self.assignment[region] = color
                result = self.backtrack()
                if result:
                    return result
                self.assignment.pop(region)
        
        return None
    
    def solve(self):
        return self.backtrack()

# Define regions, colors, and adjacency constraints
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']
adjacency = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Solve the map coloring problem
csp = MapColoringCSP(regions, colors, adjacency)
solution = csp.solve()
print("Map Coloring Solution:", solution)
