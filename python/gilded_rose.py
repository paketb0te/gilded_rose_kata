# -*- coding: utf-8 -*-
from typing import Protocol

ItemName = str

AGED_BRIE: ItemName = "Aged Brie"
BACKSTAGE_PASSES: ItemName = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS: ItemName = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name: ItemName, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdateFunc(Protocol):
    def __call__(self, item: Item) -> None:
        ...


def update_default_item(item: Item):
    item.sell_in -= 1

    decrement = 2 if item.sell_in < 0 else 1
    new_quality = item.quality - decrement
    item.quality = max(new_quality, 0)


def update_aged_brie(item: Item):
    item.sell_in -= 1

    increase = 2 if item.sell_in < 0 else 1
    new_quality = item.quality + increase
    item.quality = min(new_quality, 50)


def update_backstage_passes(item: Item):
    item.sell_in -= 1

    if 5 <= item.sell_in < 10:
        increase = 2
    elif 0 <= item.sell_in < 5:
        increase = 3
    elif item.sell_in < 0:
        increase = -item.quality
    else:
        increase = 1
    new_quality = item.quality + increase
    item.quality = min(new_quality, 50)


def update_sulfuras(item: Item):
    pass


UPDATER_MAPPING: dict[ItemName, ItemUpdateFunc] = {
    AGED_BRIE: update_aged_brie,
    BACKSTAGE_PASSES: update_backstage_passes,
    SULFURAS: update_sulfuras,
}


def update_all_items(items: list[Item]):
    for item in items:
        update_single_item(item)


def update_single_item(item: Item):
    update_quality = UPDATER_MAPPING.get(item.name, update_default_item)
    update_quality(item=item)
