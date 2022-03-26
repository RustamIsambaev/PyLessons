class OrganicCell:
    def __init__(self, nucleus_qty=1):
        if nucleus_qty < 1:
            self.nucleus_qty = 1
        else:
            self.nucleus_qty = nucleus_qty

    def __add__(self, other):
        return OrganicCell(self.nucleus_qty + other.nucleus_qty)

    def __sub__(self, other):
        return OrganicCell(self.nucleus_qty - other.nucleus_qty) if self.nucleus_qty - other.nucleus_qty > 0 else None

    def __mul__(self, other):
        return OrganicCell(self.nucleus_qty * other.nucleus_qty)

    def __truediv__(self, other):
        return OrganicCell(self.nucleus_qty // other.nucleus_qty)

    def make_order(self, nucleus_qty_prow):
        if nucleus_qty_prow < 1:
            nucleus_qty_prow = 1
        rows_qty = self.nucleus_qty // nucleus_qty_prow
        end_row_nucleus_qty = self.nucleus_qty % nucleus_qty_prow
        cell_info = ('*' * nucleus_qty_prow + '\n') * rows_qty + '*' * end_row_nucleus_qty
        return cell_info


organic_cell1 = OrganicCell(9)
organic_cell2 = OrganicCell(8)
organic_cell3 = organic_cell1 + organic_cell2
print('organic_cell3\nstart\n' + organic_cell3.make_order(5) + '\nend')
organic_cell4 = organic_cell1 - organic_cell2
print('organic_cell4\nstart\n' + organic_cell4.make_order(0) + '\nend')
organic_cell5 = organic_cell2 - organic_cell1
print(organic_cell5)
organic_cell6 = organic_cell1 * organic_cell2
print('organic_cell6\nstart\n' + organic_cell6.make_order(25) + '\nend')
organic_cell7 = organic_cell6 / organic_cell3
print('organic_cell7\nstart\n' + organic_cell7.make_order(4) + '\nend')
