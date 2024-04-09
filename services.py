import subprocess
from tabulate import tabulate
import ast

def get_service_status():
    try:
        result = subprocess.run(['systemctl', 'list-units', '--no-legend', '--type=service', '--state=running'], capture_output=True,
                                text=True, check=True)
        output = result.stdout
        if not output.strip():
            return [["Нет запущенных сервисов."]]
        lines = output.strip().split('\n')[1:]
        service_info = [line.split(None, 4)[:4] for line in lines]
        display_service_status(service_info)
    except subprocess.CalledProcessError as e:
        return [["Ошибка при выполнении команды systemctl:", str(e)]]

def display_service_status(service_status):
    service_status_str = str(service_status)
    service_status_list = ast.literal_eval(service_status_str)
    headers = ["UNIT", "LOAD", "ACTIVE", "SUB"]
    print(tabulate(service_status_list, headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    service_status = get_service_status()