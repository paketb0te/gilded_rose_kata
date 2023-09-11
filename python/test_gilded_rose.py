# -*- coding: utf-8 -*-


from gilded_rose import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS, Item, update_quality


def test_should_decrease_sell_in_and_quality():
    items = [Item(name="foo", sell_in=20, quality=30)]
    update_quality(items)
    assert items[0].sell_in == 19
    assert items[0].quality == 29


def test_quality_should_degrade_twice_as_fast_after_sell_in_has_passed():
    items = [Item(name="foo", sell_in=1, quality=21)]
    # approach sell_in date
    update_quality(items)
    assert items[0].sell_in == 0
    assert items[0].quality == 20
    # pass sell_in date
    update_quality(items)
    assert items[0].sell_in == -1
    assert items[0].quality == 18


def test_quality_should_never_be_negative():
    items = [Item(name="foo", sell_in=10, quality=1)]
    # approach zero quality
    update_quality(items)
    assert items[0].sell_in == 9
    assert items[0].quality == 0
    # ensure quality stays non-negative
    update_quality(items)
    assert items[0].sell_in == 8
    assert items[0].quality == 0


def test_aged_brie_quality_should_increase():
    items = [Item(name=AGED_BRIE, sell_in=10, quality=20)]
    update_quality(items)
    assert items[0].quality == 21


def test_aged_brie_quality_should_increase_twice_as_fast_after_sell_in_date_has_passed():
    items = [Item(name=AGED_BRIE, sell_in=1, quality=20)]
    # approach sell_in date
    update_quality(items)
    assert items[0].sell_in == 0
    assert items[0].quality == 21
    # pass sell_in date
    update_quality(items)
    assert items[0].sell_in == -1
    assert items[0].quality == 23


def test_aged_brie_quality_should_never_be_more_than_fifty():
    items = [Item(name=AGED_BRIE, sell_in=10, quality=49)]
    # approach 50 quality
    update_quality(items)
    assert items[0].sell_in == 9
    assert items[0].quality == 50
    # ensure quality stays at 50
    update_quality(items)
    assert items[0].sell_in == 8
    assert items[0].quality == 50


def test_sulfuras_should_not_change():
    items = [Item(name=SULFURAS, sell_in=10, quality=99)]
    update_quality(items)
    assert items[0].sell_in == 10
    assert items[0].quality == 99


def test_backstage_passes_quality_should_increase():
    items = [Item(name=BACKSTAGE_PASSES, sell_in=15, quality=20)]
    update_quality(items)
    assert items[0].quality == 21


def test_backstage_passes_quality_should_increase_twice_as_fast_ten_days_before_concert():
    items = [Item(name=BACKSTAGE_PASSES, sell_in=11, quality=20)]
    # approach sell_in = 10
    update_quality(items)
    assert items[0].sell_in == 10
    assert items[0].quality == 21
    # pass sell_in = 10
    update_quality(items)
    assert items[0].sell_in == 9
    assert items[0].quality == 23


def test_backstage_passes_quality_should_increase_thrice_as_fast_five_days_before_concert():
    items = [Item(name=BACKSTAGE_PASSES, sell_in=6, quality=20)]
    # approach sell_in = 5
    update_quality(items)
    assert items[0].sell_in == 5
    assert items[0].quality == 22
    # pass sell_in = 5
    update_quality(items)
    assert items[0].sell_in == 4
    assert items[0].quality == 25


def test_backstage_passes_quality_should_drop_to_zero_after_concert():
    items = [Item(name=BACKSTAGE_PASSES, sell_in=1, quality=20)]
    # approach sell_in = 0
    update_quality(items)
    assert items[0].sell_in == 0
    assert items[0].quality == 23
    # pass sell_in = 0
    update_quality(items)
    assert items[0].sell_in == -1
    assert items[0].quality == 0


def test_backstage_passes_quality_should_never_be_more_than_fifty():
    items = [Item(name=BACKSTAGE_PASSES, sell_in=10, quality=49)]
    # approach 50 quality
    update_quality(items)
    assert items[0].sell_in == 9
    assert items[0].quality == 50
    # ensure quality stays at 50
    update_quality(items)
    assert items[0].sell_in == 8
    assert items[0].quality == 50
