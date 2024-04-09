import subprocess
from tabulate import tabulate

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

def get_open_ports():
    try:
        result = subprocess.run(['ss', '-tuln'], capture_output=True, text=True, check=True)
        output = result.stdout
        display_open_ports(parse_ss_output(output))
    except subprocess.CalledProcessError as e:
        return f"Ошибка при выполнении команды ss: {e}"

def display_open_ports(ports_info):
    if isinstance(ports_info, list):
        print(tabulate(ports_info, headers="keys", tablefmt="fancy_grid"))
    else:
        print(ports_info)

if __name__ == "__main__":
    ports_info = get_open_ports()
