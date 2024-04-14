import subprocess
from base_service import BaseService


def parse_ss_output(output):
    lines = output.splitlines()
    ports_info = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 5:
            protocol = parts[0].upper()
            port_section = parts[4]
            port = port_section.split(':')[-1]
            ports_info.append({"Протокол": protocol, "Порт": port})
    return ports_info


class PortService(BaseService):
    def __init__(self):
        super().__init__("Ports")
    def get_status(self):
        try:
            result = subprocess.run(['ss', '-turn'], capture_output=True, text=True, check=True)
            output = result.stdout
            return parse_ss_output(output)
        except subprocess.CalledProcessError as e:
            return f"Ошибка при выполнении команды ss: {e}"
