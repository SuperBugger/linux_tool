#!/usr/bin/env python3
import sys
import argparse
from tabulate import tabulate
from ports import PortService
from services import ServiceService, SpecialServiceService
from processes import ProcessService


def list_ports():
    print("Список открытых портов:")
    display_table(port_service.get_status())


def list_services():
    print("Список состояния сервисов:")
    display_table(service_service.get_status())


def list_special_services(service_name):
    print(f"Информация о сервисе {service_name}:")
    special_service_service = SpecialServiceService(service_name)
    display_table(special_service_service.get_special_status())


def list_processes():
    print("Список самых ресурсоемких процессов:")
    display_table(process_service.get_status())


def display_table(data):
    if isinstance(data, list):
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    else:
        print(data)


def main_menu():
    parser = argparse.ArgumentParser(description='Консольная утилита для сбора аспектов безопасности ОС')

    subparsers = parser.add_subparsers(dest='command', title='commands')

    ports_parser = subparsers.add_parser('ports', help='Показать открытые порты')

    services_parser = subparsers.add_parser('services', help='Показать состояние сервисов')
    services_parser.add_argument('option', nargs='?', help='Опции для отображения состояния сервисов')

    processes_parser = subparsers.add_parser('processes', help='Анализ псевдофайловой системы /proc')

    args = parser.parse_args()

    if args.command == 'ports':
        list_ports()
    elif args.command == 'services':
        if args.option == "all":
            list_services()
        elif args.option:
            list_special_services(args.option)
        else:
            print("\nДоступные команды:")
            print("\tall - Показать информацию о всех сервисах")
            print("\tВведите название сервиса чтобы получить полную информацию о нём")
    elif args.command == 'processes':
        list_processes()


if __name__ == "__main__":
    port_service = PortService()
    service_service = ServiceService()
    process_service = ProcessService()
    main_menu()
