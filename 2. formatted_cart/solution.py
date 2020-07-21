
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __format__(self, format_spec):
        if format_spec == 'short':
            return ', '.join(item.name for item in self.items)
        elif format_spec in {'long', ''}:
            longest_qty = max([len(str(item.qty)) for item in self.items])
            longest_unit = max([len(item.unit) for item in self.items])
            longest_name = max([len(item.name) for item in self.items])
            longest_unit_price = max([len(item.unit_price_str) for item in self.items])
            return '\n'.join([
                item.long_fmt(longest_qty, longest_unit, longest_name, longest_unit_price) for item in self.items
            ])
        else:
            raise ValueError(f'Unknown format spec: {format_spec}')


class Item:
    def __init__(self, qty, unit, name, unit_price):
        self.qty, self.unit, self.name, self.unit_price = qty, unit, name, unit_price
        self.total_price = self.qty * self.unit_price
        self.unit_price_str = f'{float(self.unit_price):.2f}'

    def long_fmt(self, longest_qty, longest_unit, longest_name, longest_unit_price):
        qty = f'{self.qty:>{longest_qty}}'
        unit = f'{self.unit:{longest_unit}}'
        name = f'{self.name:{longest_name}}'
        unit_price = f'{self.unit_price_str:{longest_unit_price}}'
        return f'\t{qty} {unit} {name} @ ${unit_price} ... ${self.total_price:.2f}'

    def __str__(self):
        return f'{self.qty} {self.unit} {self.name} @ ${self.unit_price_str} ... ${self.total_price:.2f}'
