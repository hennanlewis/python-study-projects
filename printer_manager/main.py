from printer_manager import PrinterManager
import json

if __name__ == "__main__":
    manager = PrinterManager()

    printers = manager.get_printer_list()
    for printer in printers:
        print(json.dumps(printer, indent=4))

    printer_name = 'Sua Impressora'
    ports = manager.get_ports(printer_name)
    print(f"Portas da impressora '{printer_name}':", ports)

    port_name = 'Porta1'
    port_exists = manager.check_port_exists(printer_name, port_name)
    print(f"A porta '{port_name}' existe?", port_exists)

    response = manager.set_port_value(printer_name, port_name, 'NovoValor', 'MonitorX')
    print(response)

    response = manager.create_port(printer_name, 'NovaPorta', 'ValorPorta', 'MonitorY')
    print(response)

    response = manager.delete_port(printer_name, port_name)
    print(response)
