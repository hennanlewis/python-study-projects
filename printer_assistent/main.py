from printer_manager import PrinterManager
from icecream import ic

if __name__ == "__main__":
    manager = PrinterManager()

    try:
        printers = manager.get_printers_list()
        for printer in printers:
            ic(printer.get("pPrinterName"))

        printer_name = "Nome válido"
        ports = manager.get_ports(printer_name)
        ic(printer_name, ports)

        port_name = "Porta1"
        port_exists = manager.check_port_exists(printer_name, port_name)
        ic(port_name, port_exists)

        response = manager.set_port_value(printer_name, port_name, "NovoValor", "MonitorX")
        ic(printer_name, response)

        response = manager.create_port(printer_name, "NovaPorta", "ValorPorta", "MonitorY")
        ic(printer_name, response)

        response = manager.delete_port(printer_name, port_name)
        ic(printer_name, response)
    
    except Exception as e:
        ic(e)
