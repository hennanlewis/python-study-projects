from printer_manager import PrinterManager
import json

if __name__ == "__main__":
    manager = PrinterManager()

    # 1. Listar impressoras e monitores
    printers = manager.get_printer_list()
    for printer in printers:
        print(json.dumps(printer, indent=4))

    # 2. Obter as portas de uma impressora
    printer_name = 'Sua Impressora'
    ports = manager.get_ports(printer_name)
    print(f"Portas da impressora '{printer_name}':", ports)

    # 3. Verificar se uma porta existe
    port_name = 'Porta1'
    port_exists = manager.check_port_exists(printer_name, port_name)
    print(f"A porta '{port_name}' existe?", port_exists)

    # 4. Alterar valor de uma porta
    response = manager.set_port_value(printer_name, port_name, 'NovoValor', 'MonitorX')
    print(response)

    # 5. Criar uma nova porta
    response = manager.create_port(printer_name, 'NovaPorta', 'ValorPorta', 'MonitorY')
    print(response)

    # 6. Excluir uma porta
    response = manager.delete_port(printer_name, port_name)
    print(response)
