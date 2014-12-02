from .epsonprinter import EpsonPrinter
from optparse import OptionParser
import sys

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-v", "--idvendor", action="store", type="int", dest="id_vendor", help="The printer vendor id")
    parser.add_option("-p", "--idProduct", action="store", type="int", dest="id_product", help="The printer product id")
    options, args = parser.parse_args()
    if not options.id_vendor or not options.id_product:
        parser.print_help()
    else:
        printer = EpsonPrinter(options.id_vendor, options.id_product)
        printer.center()
        printer.print_text("NICKCONTROL")
        printer.linefeed()
        printer.set_text_size(1, 1)
        printer.print_text("Bestellung")
        printer.linefeed()
        printer.set_text_size(0, 0)  
        printer.left_justified()
        printer.print_text("------------------------------")
        printer.linefeed(3)
        printer.left_justified()
        printer.print_text("1x Coca Cola")
        printer.linefeed()
        printer.print_text("1x Dani Sahne")
        printer.linefeed()
        printer.set_text_size(2, 2)
        printer.center()
        printer.print_text("Vielen Dank")
        printer.linefeed(10)
        printer.cut()
        sys.exit(1)
