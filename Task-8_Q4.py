class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
    def get_status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"
class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    def display_details(self):
        return f"{self.get_status()}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}"
class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, viewing_angle, backlight):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.viewing_angle = viewing_angle
        self.backlight = backlight
    def display_details(self):
        return f"{self.get_status()}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, " \
               f"Lifespan: {self.lifespan}, Viewing Angle: {self.viewing_angle}, Backlight: {self.backlight}"
# Example:
led_tv = LedTV("Samsung", "Ultra Slim", "Low", "10 years", "120Hz")
plasma_tv = PlasmaTV("Sony", "Slim", "Medium", "8 years", "180 degrees", "LED")
print(led_tv.display_details())
print(plasma_tv.display_details())
