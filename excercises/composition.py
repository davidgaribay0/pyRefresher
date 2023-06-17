class Keyboard:
    def __init__(self, language):
        self.language = language

    def type(self):
        print("Typing")


class Screen:
    def __init__(self, display_size: dict):
        self.display_size = display_size
        self.total_pixes = display_size.get('width') * display_size.get('height')

    def power_on(self):
        print("Screen is turning on...")
        print(f"Rendering a total of {self.total_pixes} pixels")


class PowerSupplyUnit:
    def __init__(self, screen: Screen, device_name: str):
        print(f'Powering on {device_name}')
        screen.power_on()


class DesktopComputer:
    def __init__(self, language: str):
        keyword = Keyboard(language)
        screen = Screen({'width': 3840, 'height': 2160})
        power_supply_unit = PowerSupplyUnit(screen, 'Desktop Computer')


class Laptop:
    def __init__(self, language: str):
        keyword = Keyboard(language)
        screen = Screen({'width': 1920, 'height': 1080})
        power_supply_unit = PowerSupplyUnit(screen, 'Laptop')
