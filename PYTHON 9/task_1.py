temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
    from collections import OrderedDict
    ordered_temps = OrderedDict((sorted(temps, key=lambda x: x[1], reverse=True)))
    print(ordered_temps)

check(temps)
