#functional programming to demostrate immutability and the use of higher-order functions

#from functools import reduce

#def flatten(array):
    #return reduce(lambda x, y: x + y, array)

def flatten_and_sort(array):
    # Flatten the array by calling the above defined flatten function which uses reduce module
    #flattened = flatten(array)

    # Alternative method to Flatten the array
    flattened = [item for sublist in array for item in sublist]
    print('Flattened array ', flattened)
    
    # Sort the flattened array and return the sorted array in ascending order using sorted python inbuilt function
    sorted_array = sorted(flattened)
    return sorted_array

# Example to demostrate implementation of the above function
nested_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flatten_and_sort(nested_array)
print('Sorted flattened array ', result) # expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#======================================================================================================================


#Object Orientated programming paradigm method
class Podracer:
    def __init__(self, max_speed, condition, price):
        # Initialize the Podracer with max_speed, condition, and price attributes
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        # Update the condition of the Podracer to 'repaired'
        self.condition = 'repaired'

class AnakinsPod(Podracer):
    def boost(self):
        # Double the max_speed of Anakin's Podracer
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        # Update the condition of another Podracer to 'trashed'
        other_podracer.condition = 'trashed'

# Example usage

# Creating a general Podracer instance
pod1 = Podracer(max_speed=500, condition='perfect', price=10000)
print(f"Pod1 -> Speed: {pod1.max_speed}, Condition: {pod1.condition}, Price: {pod1.price}")

# Creating an instance of Anakin's Podracer
anakin_pod = AnakinsPod(max_speed=600, condition='perfect', price=15000)
print(f"Anakin's Pod -> Speed: {anakin_pod.max_speed}, Condition: {anakin_pod.condition}, Price: {anakin_pod.price}")

# Boosting Anakin's Podracer speed
anakin_pod.boost()
print(f"Anakin's Pod after boost -> Speed: {anakin_pod.max_speed}")

# Creating an instance of Sebulba's Podracer
sebulba_pod = SebulbasPod(max_speed=550, condition='perfect', price=13000)
print(f"Sebulba's Pod -> Speed: {sebulba_pod.max_speed}, Condition: {sebulba_pod.condition}, Price: {sebulba_pod.price}")

# Sebulba's Podracer uses flame jet on the general Podracer instance (pod1)
sebulba_pod.flame_jet(pod1)
print(f"Pod1 after Sebulba's flame jet -> Condition: {pod1.condition}")

# Repairing the trashed Podracer
pod1.repair()
print(f"Pod1 after repair -> Condition: {pod1.condition}")

