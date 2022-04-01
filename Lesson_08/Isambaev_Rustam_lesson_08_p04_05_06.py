class Warehouse:
    def __init__(self, place_qty: int):
        self.place_qty = place_qty  # вместимость склада


class OfficeEquipment:
    def __init__(self, occ_places: int):
        self.occ_places = occ_places  # занимаемое место на складе


class Printer(OfficeEquipment):
    def __init__(self, occ_places, printer_type):
        super().__init__(occ_places)
        self.printer_type = printer_type


class Scaner(OfficeEquipment):
    def __init__(self, occ_places, scaner_type):
        super().__init__(occ_places)
        self.scaner_type = scaner_type


class Xerox(OfficeEquipment):
    def __init__(self, occ_places, xerox_type):
        super().__init__(occ_places)
        self.xerox_type = xerox_type


class OperationRegistry:
    def __init__(self):
        self.regstructure = {}
        self.operation_id = 0

    @staticmethod
    def validation(recipient_side, transmitting_side, office_equipment, qty):  # 6
        rez = isinstance(qty, int) and isinstance(office_equipment, OfficeEquipment) and isinstance(
            recipient_side, Warehouse) and isinstance(
            transmitting_side, Warehouse) and recipient_side.place_qty >= qty * office_equipment.occ_places
        return rez

    def transaction(self, recipient_side, transmitting_side, office_equipment, qty):  # 5
        if self.validation(recipient_side, transmitting_side, office_equipment, qty):
            self.regstructure[self.operation_id] = [office_equipment, recipient_side, transmitting_side, qty]
            recipient_side.place_qty -= office_equipment.occ_places * qty
            transmitting_side.place_qty += office_equipment.occ_places * qty
            self.operation_id += 1
            print('транзакция записана успешно!')
        else:
            print('введены некорректные данные - транзакция не записана!')


if __name__ == '__main__':
    supplier = Warehouse(50)
    my_dep = Warehouse(20)
    my_warehouse = Warehouse(15)
    my_printer = Printer(1, 'лазерный')
    my_operregistry = OperationRegistry()
    my_operregistry.transaction(my_warehouse, supplier, my_printer, 15)
    my_operregistry.transaction(my_dep, my_warehouse, my_printer, 15)
    my_operregistry.transaction(my_warehouse, supplier, my_printer, 15)
    my_operregistry.transaction(my_dep, my_warehouse, my_printer, 5)
    my_operregistry.transaction(my_warehouse, my_dep, my_printer, 20)
