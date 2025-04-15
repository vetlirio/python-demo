"""def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 0

    return inventory[2]

print(get_leather_scraps())
"""

# Great, now making so you can call any of them.

def get_anything_from_list(item):
    bread = 20
    inventory = [ 
        "healing potion",
        "leather scraps", 
        "iron helmet", 
        bread, 
        "shortsword"
    ]
    return inventory[item]

print(get_anything_from_list(0))

# Wanting to upload 