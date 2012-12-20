from mechanize import urlopen
from wakfucraft.utils import WE_BASE_URL, WE_ITEM_PATH, db_commit
from wakfucraft.item import ItemParser


class Main(object):

    resource_index = {306:"woodcutter", 308:"fisherman", 309:"farmer",
                      313:"herbalist", 281:"miner", 282:"trapper"}
    refinement_index = {327:"woodcutter", 393:"farmer", 463:"herbalist", 514:"miner"}

    @staticmethod
    def process_index(index, type, resource):
        response = urlopen(("%s%s/%s") % (WE_BASE_URL, WE_ITEM_PATH, index))
        ip = ItemParser()
        ip.feed(response.read())
        print ip.prepare_data(type, job=resource[index])
        db_commit(ip.prepare_data(type, job=resource[index]))

    def main(self):
        for i in Main.resource_index.keys():
            Main.process_index(i, "resource", Main.resource_index)
        for i in Main.refinement_index.keys():
            Main.process_index(i, "refinement", Main.refinement_index)

if __name__ == "__main__":
    m = Main()
    m.main()
