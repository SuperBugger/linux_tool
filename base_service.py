class BaseService:
    def __init__(self, name=None):
        self.name = name

    def get_status(self):
        raise NotImplementedError("Метод get_status должен быть переопределен в подклассе")


class SpecialService(BaseService):
    def __init__(self, name):
        super().__init__(name)

    def get_status(self):
        raise NotImplementedError("Метод get_status должен быть переопределен в подклассе")

    def get_detailed_status(self):
        raise NotImplementedError("Метод get_detailed_status должен быть переопределен в подклассе")
