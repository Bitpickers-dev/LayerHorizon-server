def hex_to_gwei(hex: str):
    return '{:f}'.format(int(hex, 16) / 1000000000)


def hex_to_eth(hex: str):
    return '{:.18f}'.format(int(hex, 16) / 1000000000000000000)
