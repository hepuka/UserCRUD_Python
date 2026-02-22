class BaseController:

    def __init__(self, service):
        self.service = service

    def get_all(self):
        return self.service.get_all()

    def get_by_field(self, field, value):
        return self.service.get_by_field(field, value)

    def create(self, data):
        self.service.create(data)

    def delete(self, field, value):
        self.service.delete(field, value)
