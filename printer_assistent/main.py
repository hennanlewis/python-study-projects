from printer_manager import PrinterManager
from icecream import ic

ic.configureOutput(includeContext=True)
def main():
    printer_manager = PrinterManager()

    printer_list = printer_manager.printers_names
    print("Impressoras disponíveis:")
    ic(printer_list)

    # Exibindo os detalhes das impressoras
    for printer in printer_manager.printer_list:
        print("Detalhes das impressoras: ", printer["name"])
        printer_details = printer["printer_details"]
        ic(printer_details)

    # Exibindo as portas disponíveis
    print("Portas disponíveis:")
    printers_ports = printer_manager.get_printers_ports()
    for port_info in printers_ports:
        print(f"Porta: '{port_info["Name"]}'")
        ic(port_info)

    # Verificando a existência de uma porta específica
    port_to_check = "MyNewPort" # portas não devem possuir espaços
    has_port = printer_manager.check_port_exists(port_to_check)
    print("Porta a checar:", port_to_check)
    ic(has_port)

    # Criando uma nova porta TCP/IP
    print("\nCriando porta...")
    new_port_name = "MyNewPort"
    new_port_ip = "192.168.1.100"
    response = printer_manager.create_ip_port(new_port_name, new_port_ip)
    response = printer_manager.create_ip_port(new_port_name, new_port_ip)
    ic(response)

    # Excluindo uma porta
    print("\nExcluindo porta...")
    response = printer_manager.delete_port(new_port_name)
    ic(response)

    response_options = {
        0: f"Porta '{new_port_name}' não existe.",
        1: f"Porta '{new_port_name}' já existe."
    }
    has_port = printer_manager.check_port_exists(new_port_name)
    response = response_options[1] if has_port else response_options[0]
    print(f"\nChecando existência da porta '{new_port_name}':")
    ic(response)

if __name__ == "__main__":
    main()
