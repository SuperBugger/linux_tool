import subprocess
from base_service import BaseService, SpecialService


class ServiceService(BaseService):
    def __init__(self):
        super().__init__("Services")

    def get_status(self):
        try:
            result = subprocess.run(['systemctl', 'list-units', '--no-legend', '--type=service', '--state=running'],
                                    capture_output=True,
                                    text=True, check=True)
            output = result.stdout
            if not output.strip():
                return [["Нет запущенных сервисов."]]
            lines = output.strip().split('\n')[1:]
            service_info = [line.split(None, 4)[:4] for line in lines]
            return service_info
        except subprocess.CalledProcessError as e:
            return [["Ошибка при выполнении команды systemctl:", str(e)]]


class SpecialServiceService(SpecialService):
    def __init__(self, name):
        super().__init__(name)

    def get_special_status(self):
        try:
            result = subprocess.run(['systemctl', 'status', self.name], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Ошибка при выполнении команды systemctl: {e}"
