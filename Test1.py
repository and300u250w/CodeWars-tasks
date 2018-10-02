def check_bit4(input):
    des = input & 0b1000
    return "on" if des > 0 else "off"


check_bit4(0b1)  # ==> "off"
check_bit4(0b11011)  # ==> "on"
check_bit4(0b1010)  # ==> "on"

