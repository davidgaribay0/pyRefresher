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


class Ram:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def load_information(self):
        pass


class Motherboard:
    def __init__(self, ram: Ram, total_ram_slots, ram_max_capacity):
        self.ram = ram
        self.total_ram_slots = total_ram_slots
        self.ram_max_capacity = ram_max_capacity

    def health_checks(self) -> bool:
        if self.ram_max_capacity > self.ram.capacity:
            return True
        else:
            raise Exception("Max ram capacity exceeded")

    def power_on(self):
        try:
            self.health_checks()
            print("Motherboard is turning on please wait...")
        except Exception as e:
            print(e)


class PowerSupplyUnit:
    def __init__(self, screen: Screen, device_name: str, motherboard: Motherboard):
        print(f'Powering on {device_name}, Please wait ...')
        screen.power_on()
        motherboard.power_on()


class DesktopComputer:
    def __init__(self, language: str):
        keyword = Keyboard(language)
        screen = Screen({'width': 3840, 'height': 2160})
        ram = Ram(4)
        motherboard = Motherboard(ram, 4, 128)
        power_supply_unit = PowerSupplyUnit(screen, 'Desktop Computer', motherboard)


class Laptop:
    def __init__(self, language: str):
        keyword = Keyboard(language)
        screen = Screen({'width': 1920, 'height': 1080})
        ram = Ram(8)
        motherboard = Motherboard(ram, 2, 64)
        power_supply_unit = PowerSupplyUnit(screen, 'Laptop', motherboard)
