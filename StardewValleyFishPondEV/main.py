from random import random
from item import Item
from types import GeneratorType
from roe import Roe
from fish import Fish
from pond_produce import PondProduce

# List keeping track of aging roe
aging_roe = []


# Will the pond try generating something from its item table?
def pond_will_try_generating_something_today():
    return 0.95 >= random()


# Iterate through all roe in the global aging_roe list
#  and age them by one day. If the roe is done aging,
#  add its sell value to a running total called value
#  and return the total value of aged roe sold that day.
# Finally, make a new list of roe that wasn't sold as
#  we should not remove roe as we iterate through the list.
def age_all_roe_by_one_day():
    global aging_roe
    value = 0
    for roe in aging_roe:
        returned_value = roe.age_one_day()
        if returned_value is not None:
            value += returned_value
    aging_roe = [roe for roe in aging_roe if not roe.is_finished()]
    return value


def run_fish_ev():
    final_ev_dict = {}
    number_of_days = 1000000
    global aging_roe
    for fish_name, fish_value in Fish.__members__.items():
        total_gold_from_selling = 0.0
        aging_roe = []
        for day in range(1, number_of_days):
            total_gold_from_selling += age_all_roe_by_one_day()
            if pond_will_try_generating_something_today():
                # for each item in the fish pond table in order
                for produce_info in PondProduce[fish_name].value:
                    # if the item probability is met, the item is produced, and no further rolls needed on the table
                    if produce_info.probability >= random():
                        # if it is roe, let it age in preserves jar
                        if isinstance(produce_info.item, Roe):
                            # sometimes more than 1 roe is produced in the pond per day
                            for insert in range(0, produce_info.quantity):
                                aging_roe.insert(0, Roe(produce_info.item.fish_object))
                        # if it is an item, just sell it
                        elif isinstance(produce_info.item, Item):
                            # if the quantity is random each time the object is rolled on the table,
                            # generate the item's random quantity
                            if isinstance(produce_info.quantity, GeneratorType):
                                total_gold_from_selling += next(produce_info.quantity) * produce_info.item.value
                            else:
                                total_gold_from_selling += produce_info.quantity * produce_info.item.value
                        else:
                            print("Item {} doesn't match anything", produce_info.item)
                        break
        expected_daily_value = total_gold_from_selling / number_of_days
        final_ev_dict[fish_name] = expected_daily_value
        print('{:15} {} g/day'.format(fish_name, expected_daily_value))
    print('=======================================')
    print('Expected Values in Descending Order')
    [print(key, value) for (key, value) in sorted(final_ev_dict.items(), key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    run_fish_ev()
