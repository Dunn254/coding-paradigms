class Podracer:
    def __init__(self, max_speed, condition, price):
        # Encapsulation: initializing attributes within the class
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        # Encapsulation: method to update the condition
        self.condition = 'repaired'

class AnakinsPod(Podracer):
    def boost(self):
        # Inheritance: AnakinsPod inherits from Podracer
        # Polymorphism: specific behavior for AnakinsPod
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        # Inheritance: SebulbasPod inherits from Podracer
        # Polymorphism: specific behavior for SebulbasPod
        other_podracer.condition = 'trashed'

# Example usage demonstrating OOP principles
nested_array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

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
