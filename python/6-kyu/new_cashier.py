def get_order(order):
    lt = "Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke".split()
    res = ""
    for item in lt:
        if item.casefold() in order:
            for i in range(0, order.count(item.casefold())):
                res += item + " "
    return res[:-1]

MENU = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def get_order2(order):
    result = []
    for item in MENU:
        result.extend([item for _ in range(order.count(item.lower()))])
    return " ".join(result)

def get_order3(order):
    menu = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    clean_order = ''
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order[:-1]
