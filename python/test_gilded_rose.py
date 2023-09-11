# -*- coding: utf-8 -*-


from gilded_rose import (
    AGED_BRIE,
    BACKSTAGE_PASSES,
    SULFURAS,
    Item,
    update_quality_of_all_items,
    update_quality_of_single_item,
)


def test_should_decrease_sell_in_and_quality():
    item = Item(name="foo", sell_in=20, quality=30)
    update_quality_of_single_item(item)
    assert item.sell_in == 19
    assert item.quality == 29


def test_should_iterate_over_all_items_and_decrease_sell_in_and_quality():
    items = [
        Item(name="foo", sell_in=20, quality=30),
        Item(name="bar", sell_in=10, quality=15),
    ]
    update_quality_of_all_items(items)
    assert items[0].name == "foo"
    assert items[0].sell_in == 19
    assert items[0].quality == 29

    assert items[1].name == "bar"
    assert items[1].sell_in == 9
    assert items[1].quality == 14


def test_quality_should_degrade_twice_as_fast_after_sell_in_has_passed():
    item = Item(name="foo", sell_in=1, quality=21)
    # approach sell_in date
    update_quality_of_single_item(item)
    assert item.sell_in == 0
    assert item.quality == 20
    # pass sell_in date
    update_quality_of_single_item(item)
    assert item.sell_in == -1
    assert item.quality == 18


def test_quality_should_never_be_negative():
    item = Item(name="foo", sell_in=10, quality=1)
    # approach zero quality
    update_quality_of_single_item(item)
    assert item.sell_in == 9
    assert item.quality == 0
    # ensure quality stays non-negative
    update_quality_of_single_item(item)
    assert item.sell_in == 8
    assert item.quality == 0


def test_aged_brie_quality_should_increase():
    item = Item(name=AGED_BRIE, sell_in=10, quality=20)
    update_quality_of_single_item(item)
    assert item.quality == 21


def test_aged_brie_quality_should_increase_twice_as_fast_after_sell_in_date_has_passed():
    item = Item(name=AGED_BRIE, sell_in=1, quality=20)
    # approach sell_in date
    update_quality_of_single_item(item)
    assert item.sell_in == 0
    assert item.quality == 21
    # pass sell_in date
    update_quality_of_single_item(item)
    assert item.sell_in == -1
    assert item.quality == 23


def test_aged_brie_quality_should_never_be_more_than_fifty():
    item = Item(name=AGED_BRIE, sell_in=10, quality=49)
    # approach 50 quality
    update_quality_of_single_item(item)
    assert item.sell_in == 9
    assert item.quality == 50
    # ensure quality stays at 50
    update_quality_of_single_item(item)
    assert item.sell_in == 8
    assert item.quality == 50


def test_sulfuras_should_not_change():
    item = Item(name=SULFURAS, sell_in=10, quality=99)
    update_quality_of_single_item(item)
    assert item.sell_in == 10
    assert item.quality == 99


def test_backstage_passes_quality_should_increase():
    item = Item(name=BACKSTAGE_PASSES, sell_in=15, quality=20)
    update_quality_of_single_item(item)
    assert item.quality == 21


def test_backstage_passes_quality_should_increase_twice_as_fast_ten_days_before_concert():
    item = Item(name=BACKSTAGE_PASSES, sell_in=11, quality=20)
    # approach sell_in = 10
    update_quality_of_single_item(item)
    assert item.sell_in == 10
    assert item.quality == 21
    # pass sell_in = 10
    update_quality_of_single_item(item)
    assert item.sell_in == 9
    assert item.quality == 23


def test_backstage_passes_quality_should_increase_thrice_as_fast_five_days_before_concert():
    item = Item(name=BACKSTAGE_PASSES, sell_in=6, quality=20)
    # approach sell_in = 5
    update_quality_of_single_item(item)
    assert item.sell_in == 5
    assert item.quality == 22
    # pass sell_in = 5
    update_quality_of_single_item(item)
    assert item.sell_in == 4
    assert item.quality == 25


def test_backstage_passes_quality_should_drop_to_zero_after_concert():
    item = Item(name=BACKSTAGE_PASSES, sell_in=1, quality=20)
    # approach sell_in = 0
    update_quality_of_single_item(item)
    assert item.sell_in == 0
    assert item.quality == 23
    # pass sell_in = 0
    update_quality_of_single_item(item)
    assert item.sell_in == -1
    assert item.quality == 0


def test_backstage_passes_quality_should_never_be_more_than_fifty():
    item = Item(name=BACKSTAGE_PASSES, sell_in=10, quality=49)
    # approach 50 quality
    update_quality_of_single_item(item)
    assert item.sell_in == 9
    assert item.quality == 50
    # ensure quality stays at 50
    update_quality_of_single_item(item)
    assert item.sell_in == 8
    assert item.quality == 50
