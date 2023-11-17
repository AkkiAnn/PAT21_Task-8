class Circle:
    _pi = 3.141  
    def __init__(self, radius_list):
        self._radius_list = radius_list  
    @classmethod
    def calculate_area(cls, radius):
        return cls._pi * radius ** 2
    @classmethod
    def calculate_perimeter(cls, radius):
        return 2 * cls._pi * radius
    def display_properties(self):
        for i, radius in enumerate(self._radius_list, start=1):
            area = Circle.calculate_area(radius)
            perimeter = Circle.calculate_perimeter(radius)
            print(f"Circle {i} - Radius: {radius}, Area: {area:.2f}, Perimeter: {perimeter:.2f}")
# Example:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)
circle_instance.display_properties()
