from controllers.base_controller import BaseController


class OrderController(BaseController):

    def __init__(self, service):
        super().__init__(service)

    def get_by_status(self, status):
        return self.service.get_many_by_field("status", status)