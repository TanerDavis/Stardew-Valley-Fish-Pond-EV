from enum import Enum
from item import Item
from random import randint
from fish import Fish
from roe import Roe


# Info object used to create fish pond roll tables.
# quantity      - how many of Item are produced if rolled
# item          - Item that is produced
# probability   - what is the probability this item gets rolled
class PondProduceInfo:
    def __init__(self, quantity, item, probability):
        self.quantity = quantity
        self.item = item
        self.probability = probability


# Some items in ponds generate a random quantity of said items.
# Use this generate to randomly generate a quantity for FishProduce
# Enums.
def generate_amount(a, b):
    while True:
        yield randint(a, b)


# Item tables for fish ponds.
class PondProduce(Enum):
    LAVA_EEL = [
        PondProduceInfo(10, Item.MAGMA_GEODE, .033),
        PondProduceInfo(5, Item.MAGMA_GEODE, .02),
        PondProduceInfo(5, Item.SPICY_EEL, .04),
        PondProduceInfo(3, Roe(Fish.LAVA_EEL), .033),
        PondProduceInfo(2, Roe(Fish.LAVA_EEL), .15),
        PondProduceInfo(5, Item.GOLD_ORE, .10),
        PondProduceInfo(1, Roe(Fish.LAVA_EEL), 1),
    ]
    STURGEON = [
        PondProduceInfo(2, Roe(Fish.STURGEON), .25),
        PondProduceInfo(1, Roe(Fish.STURGEON), 1)
    ]
    ICE_PIP = [
        PondProduceInfo(5, Item.FROZEN_GEODE, .05),
        PondProduceInfo(5, Item.FROZEN_TEAR, .075),
        PondProduceInfo(1, Item.FROZEN_GEODE, .12),
        PondProduceInfo(1, Item.DIAMOND, .01),
        PondProduceInfo(5, Item.IRON_ORE, .1),
        PondProduceInfo(1, Roe(Fish.ICE_PIP), .5),
        PondProduceInfo(1, Roe(Fish.ICE_PIP), .25),
    ]
    STONEFISH = [
        PondProduceInfo(5, Item.GEODE, .05),
        PondProduceInfo(30, Item.STONE, .075),
        PondProduceInfo(1, Item.GEODE, .12),
        PondProduceInfo(1, Item.DIAMOND, .01),
        PondProduceInfo(5, Item.COPPER_ORE, .1),
        PondProduceInfo(1, Roe(Fish.STONEFISH), .5),
        PondProduceInfo(1, Roe(Fish.STONEFISH), .25),
    ]
    SUPER_CUCUMBER = [
        PondProduceInfo(generate_amount(1, 3), Item.IRIDIUM_ORE, .05),
        PondProduceInfo(generate_amount(1, 3), Item.AMETHYST, .05),
        PondProduceInfo(1, Roe(Fish.SUPER_CUCUMBER), 1),
    ]
    PUFFERFISH = [
        PondProduceInfo(1, Roe(Fish.PUFFERFISH), 1),
    ]
