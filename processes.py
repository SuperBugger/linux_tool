import os
from base_service import BaseService


class ProcessService(BaseService):
    def __init__(self):
        super().__init__("Processes")

    def get_status(self):
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
            return get_top_processes_by_memory(5, processes_info)
        except Exception as e:
            return f"Ошибка при анализе процессов: {e}"


def get_top_processes_by_memory(n, processes_info):
    if isinstance(processes_info, str):
        return processes_info
    top_processes = sorted(processes_info, key=lambda x: x.get("memory_usage", 0), reverse=True)[:n]
    return top_processes
