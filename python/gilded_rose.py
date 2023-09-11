# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def update_quality_of_all_items(items: list[Item]):
    for item in items:
        update_quality_of_single_item(item)


def update_quality_of_single_item(item: Item):
    update_sell_in_date(item)

    if item.name == AGED_BRIE:
        update_aged_brie(item)
    elif item.name == BACKSTAGE_PASSES:
        update_backstage_passes(item)
    elif item.name == SULFURAS:
        update_sulfuras(item)
    else:
        update_default_item(item)


def update_sulfuras(item: Item):
    pass


def update_default_item(item: Item):
    if item.quality > 0:
        item.quality = item.quality - 1
    if item.sell_in < 0:
        if item.quality > 0:
            item.quality = item.quality - 1


def update_backstage_passes(item: Item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.sell_in < 10:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 5:
            if item.quality < 50:
                item.quality = item.quality + 1
    if item.sell_in < 0:
        item.quality = item.quality - item.quality


def update_aged_brie(item: Item):
    if item.quality < 50:
        item.quality = item.quality + 1
    if item.sell_in < 0:
        if item.quality < 50:
            item.quality = item.quality + 1


def update_sell_in_date(item: Item):
    if item.name == SULFURAS:
        pass
    else:
        item.sell_in = item.sell_in - 1
