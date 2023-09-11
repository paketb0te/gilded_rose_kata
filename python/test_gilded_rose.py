# -*- coding: utf-8 -*-


from gilded_rose import GildedRose, Item


def test_foo():
    items = [Item(name="foo", sell_in=0, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
