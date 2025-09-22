"""
PROBLEM: Water Container Management System

You're building a water management system for a smart city. The city has various types of 
water containers (tanks, reservoirs, pools) arranged in a line, each with different heights 
and capacities. 

You need to:
1. Find the maximum water volume that can be trapped between any two containers
2. Support different container types with inheritance
3. Use efficient algorithms to process large arrays of containers

REQUIREMENTS:
- Use inheritance to model different container types
- Implement two pointers technique for optimal water volume calculation
- Use appropriate data structures for container management
- Calculate maximum trappable water volume between containers

CONSTRAINTS:
- 2 ≤ number of containers ≤ 10^5
- 1 ≤ container height ≤ 10^4
- Container types: Tank, Reservoir, Pool (each with different properties)

"""

class Container:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

class Tank(Container):
    def __init__(self, height, capacity, material):
        super().__init__(height)
        self.capacity = capacity
        self.material = material

class Reservoir(Container):
    def __init__(self, height, capacity, is_covered = False):
        super().__init__(height)
        self.capacity = capacity
        self.is_covered = is_covered

class Pool(Container):
    def __init__(self, height, capacity, shape):
        super().__init__(height)
        self.capacity = capacity
        self.shape = shape

class WaterManagement:
    def __init__(self, containers):
        # Save the containers passed into the object
        self.containers = containers

    def max_trappable_water(self):
        left, right = 0, len(self.containers) - 1
        max_water = 0

        while left < right:
            height_left = self.containers[left].get_height()
            height_right = self.containers[right].get_height()
            width = right - left
            
            # Volume = min height × width
            current_volume = min(height_left, height_right) * width
            max_water = max(max_water, current_volume)
            
            # Move the pointer pointing to the shorter container
            if height_left < height_right:
                left += 1
            else:
                right -= 1
        
        return max_water


if __name__ == "__main__":
    containers = [
        Tank(5, 100, "steel"), 
        Reservoir(8, 200, True), 
        Pool(6, 150, "Rectangular")
    ]

    wm = WaterManagement(containers)
    print("Maximum trappable water volume:", wm.max_trappable_water())