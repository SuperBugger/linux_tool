#!/usr/bin/env python3
import sys
from ports import get_open_ports
from services import get_service_status
from processes import get_top_processes_by_memory

def list_ports():
    print("Список открытых портов:")
    get_open_ports()

def list_services():
    print("Список состояния сервисов:")
    get_service_status()

def list_processes():
    print("Список самых ресурсоемких процессов:")
    get_top_processes_by_memory()

def list_help():
    print("\nДоступные команды:")
    print("\tports - Показать открытые порты")
    print("\tservices - Показать состояние сервисов")
    print("\tprocesses - Анализ псевдофайловой системы /proc")
    print("\texit - Выход")

def main():
    while True:
        cmd = input("\n>>").strip()

        if cmd == "ports":
            list_ports()
        elif cmd == "services":
            list_services()
        elif cmd == "processes":
            list_processes()
        elif cmd == "help":
            list_help()
        elif cmd == "exit":
            print("Выход из программы...")
            sys.exit(0)
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()
