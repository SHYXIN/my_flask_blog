import os

# insert the GTK3 Runtime folder at the beginning
GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')

import csv
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

class CsvData:
    """This class reads, contains and provides the data for
    a CSV file where the first field is the unique id
    """

    def __init__(self, filename):
        self.data = {}
        filepath = Path(__file__).parent / filename
        with open(filepath, "r") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                #   类似  row[list(row)[0]]， 取第一个的键名，然后再取值，作为键，整个作为值
                self.data[row[next(iter(row))]] = row

    def get_by_id(self, unique_id):
        if str(unique_id) in self.data:
            return self.data[str(unique_id)]

    def get_all_by_relation_id(self, relation_name, relation_id):
        return [row for row in self.data.values() if row[relation_name]== str(relation_id)]

    def unique_ids(self):
        """Returns a sorted list of the unique ids from structure"""
        ids = list(self.data.keys())
        ids.sort()
        return ids



# sd = CsvData('address.csv')
# print(sd.get_by_id(1))
# print(sd.unique_ids())

class Transactions:
    """This class encapsulates all the company transaction data and interactions
    with that data"""

    def __init__(self):
        self._customer = CsvData("customer.csv")
        self._product = CsvData("product.csv")
        self._order = CsvData("order.csv")
        self._item = CsvData("item.csv")
        self._address = CsvData("address.csv")

    def order(self, order_id):
        """This method gets all the information about an order
        based on the unique order id

        Args:
            order_id (int): the unique order id value to locate an order with
        """
        order = self._order.get_by_id(order_id)
        customer = self._customer.get_by_id(order.get("customer_id"))
        address = self._address.get_by_id(order.get("address_id"))
        items = self._item.get_all_by_relation_id("order_id", order.get("order_id"))
        for item in items:
            product = self._product.get_by_id(item.get("product_id"))
            item["product"] = product.get("product")
        return {
            "order": order,
            "customer": customer,
            "address": address,
            "items": items,
        }

    def order_ids(self, ):
        """Returns a list of order ids"""
        return self._order.unique_ids()

def create_invoice(info):
    """Create the PDF invoice for the order

    Args:
        info (dict): The info information to generate the invoice with
    """
    path = Path(__file__).parent
    invoice_filename = path / f"invoice_{info.get('order').get('order_id')}.pdf"

    # delete existing order invoice file if exists
    if os.path.exists(invoice_filename):
        os.remove(invoice_filename)

    # set up Jinja2 to generate the HTML and then the PDF file
    env = Environment(loader=FileSystemLoader(Path(path)))
    template = env.get_template("invoice_template.jinja")
    html_out = template.render(info)
    HTML(string=html_out).write_pdf(
        invoice_filename,
        stylesheets=[
            path / "page.css",
            path / "bootstrap.css",
        ]
    )


# get the data in memory
transactions = Transactions()

# generate an invoice file for all the orders
for order_id in transactions.order_ids():
    print(f"Creating invoice for order id: {order_id}")
    order_info = transactions.order(order_id)
    print(order_info)
    create_invoice(order_info)
    break


# cd当前的目录
