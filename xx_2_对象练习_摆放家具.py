class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        # return str(self.area)
        return '%s 占地 %0.1f平米' % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.item_list = []
        self.free_area = area

    def __str__(self):
        return ('户型：%s,\n总面积：%.2f,剩余面积：%.2f,\n家具名称列表:%s'
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        if self.free_area<item.area:
            return
        self.item_list.append(item.name)
        self.free_area -= item.area
        # print('添加家具%s'% item)
        print(item)


bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)


bighouse = House('big_house', 100)
bighouse.add_item(bed)
bighouse.add_item(chest)
bighouse.add_item(table)
print(bighouse)
