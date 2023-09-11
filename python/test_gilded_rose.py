# -*- coding: utf-8 -*-


from gilded_rose import GildedRose, Item


def test_should_decrease_sell_in_and_quality():
    items = [Item(name="foo", sell_in=20, quality=30)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 19
    assert items[0].quality == 29
