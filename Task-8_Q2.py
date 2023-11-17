class Circle:
    # Private class 
    _pi = 3.141  
    def __init__(self, rad_list):
        self._rad_list = rad_list  
    def calculate_area(self):
        areas = [Circle._pi * r ** 2 for r in self._rad_list]
        return areas
    def display_areas(self):
        areas = self.calculate_area()
        for i, area in enumerate(areas, start=1):
            print(f"Circle {i} - Area: {area:.2f}")
# Example:
rad_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_exp = Circle(rad_list)
circle_exp.display_areas()
