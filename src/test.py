from urllib2 import urlopen
from wakfucraft.utils import WE_BASE_URL, WE_ITEM_PATH
from wakfucraft.item import ItemParser

class Test(object):

    resource_index = {306:"woodcutter", 308:"fisherman", 309:"farmer",
                      313:"herbalist", 281:"miner", 282:"trapper"}
    refinement_index = {327:"woodcutter", 393:"farmer", 463:"herbalist", 514:"miner"}

    @staticmethod
    def process_index(index_arr, iterator, item_type="resource"):
        response = urlopen(("%s%s/%s") % (WE_BASE_URL, WE_ITEM_PATH, iterator))
        ip = ItemParser(index_arr[iterator], item_type)
        ip.feed(response.read())
        print ip
        #print ip.prepare_data()

    def main(self):
        for i in Test.resource_index.keys():
            Test.process_index(Test.resource_index, iterator=i)
        for i in Test.refinement_index.keys():
            Test.process_index(Test.refinement_index, iterator=i, item_type="refinement")

if __name__ == "__main__":
    m = Test()
    m.main()