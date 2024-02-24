# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_conjured_item_quality_degrades_twice_as_fast(self):
        conjured_item_name = "Conjured Mana Cake"
        items = [Item(conjured_item_name, 3, 6)]  # Starting with 3 days to sell and quality 6
        gr = GildedRose(items)

        gr.update_quality()  # After 1 day

        # Quality should degrade by 2, SellIn by 1
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 2)

        gr.update_quality()  # After 2 days

        # Quality should degrade by another 2, SellIn by another 1
        self.assertEqual(items[0].quality, 2)
        self.assertEqual(items[0].sell_in, 1)

    def test_conjured_item_quality_degrades_four_times_as_fast_after_sell_by_date(self):
        conjured_item_name = "Conjured Mana Cake"
        items = [Item(conjured_item_name, 0, 6)]  # Sell by date has passed, quality 6
        gr = GildedRose(items)

        gr.update_quality()  # After sell by date

        # Quality should degrade by 4 as sell by date has passed
        self.assertEqual(items[0].quality, 2)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        for i, item in enumerate(gr.items):
            with self.subTest(i=i):
                self.assertEqual(item.name, expected_items[i].name)
                self.assertEqual(item.sell_in, expected_items[i].sell_in)
                self.assertEqual(item.quality, expected_items[i].quality)


if __name__ == '__main__':
    unittest.main()
