# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Check if the item is "Conjured"
            if item.name.startswith("Conjured"):
                degrade_rate = 2
            else:
                degrade_rate = 1

            # Handle quality degradation for normal and special items
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality -= degrade_rate
            else:
                if item.quality < 50:
                    item.quality += 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            item.quality += 1
                        if item.sell_in < 6:
                            item.quality += 1

            # Update sell_in value
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            # Handle quality change after the sell-by date has passed
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality -= degrade_rate
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1

