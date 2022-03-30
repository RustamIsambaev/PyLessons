class Warehouse:
    def __init__(self, place_qty):
        self.place_qty = place_qty
        self.structure = {}


class OfficeEquipment:
    def __init__(self, occ_places, model, serial_number, year):
        self.occ_places = occ_places
        self.model = model
        self.serial_number = serial_number
        self.year = year


class Printer(OfficeEquipment):
    def __init__(self, occ_places, model,  serial_number, year, printer_type):
        super().__init__(occ_places, model, serial_number, year)
        self.type = printer_type


class Scaner(OfficeEquipment):
    def __init__(self, occ_places, model,  serial_number, year, scaner_type):
        super().__init__(occ_places, model, serial_number, year)
        self.type = scaner_type


class Xerox(OfficeEquipment):
    def __init__(self, occ_places, model, serial_number, year, xerox_type):
        super().__init__(occ_places, model, serial_number, year)
        self.type = xerox_type
