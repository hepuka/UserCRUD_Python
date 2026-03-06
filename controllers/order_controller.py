from controllers.base_controller import BaseController
from bson import ObjectId

class OrderController(BaseController):

    def __init__(self, service):
        super().__init__(service)

    def get_by_status(self, status):
        return self.service.get_many_by_field("status", status)

    def get_by_tablenumber(self, value):
        return self.service.get_many_by_field("table_number", value)

    def get_open_order_by_table(self, value):

        orders = self.service.get_many_by_field("table_number", value)

        for order in orders:
            if order.status == "nyitott":
                return order

        return None

    def add_products_to_order(self, object_id, new_products, total_to_add):
        return self.service.add_products_to_order(object_id, new_products, total_to_add)