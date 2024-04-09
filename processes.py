import os
from tabulate import tabulate

def get_process_resource_usage():
    processes_info = []
    try:
        for pid in os.listdir("/proc"):
            if pid.isdigit():
                process_info = {"pid": pid}
                with open(f"/proc/{pid}/status") as status_file:
                    for line in status_file:
                        if line.startswith("Name:"):
                            process_info["name"] = line.split()[1]
                        elif line.startswith("VmRSS:"):
                            process_info["memory_usage"] = int(line.split()[1])
                    processes_info.append(process_info)
        return processes_info
    except Exception as e:
        return f"Ошибка при анализе процессов: {e}"

def get_top_processes_by_memory(n=5):
    processes_info = get_process_resource_usage()
    if isinstance(processes_info, str):
        return processes_info
    top_processes = sorted(processes_info, key=lambda x: x.get("memory_usage", 0), reverse=True)[:n]
    display_top_processes_by_memory(top_processes)

def display_top_processes_by_memory(top_processes):
    if isinstance(top_processes, list):
        print(tabulate(top_processes, headers="keys", tablefmt="fancy_grid"))
    else:
        print(top_processes)

if __name__ == "__main__":
    top_processes = get_top_processes_by_memory()
