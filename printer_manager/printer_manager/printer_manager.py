import win32print

class PrinterManager:

    @staticmethod
    def get_printer_list():
        """Retorna a lista de impressoras atuais do computador com seus respectivos monitores."""
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        printer_info = []
        for printer in printers:
            printer_name = printer[2]
            handle = win32print.OpenPrinter(printer_name)
            printer_details = win32print.GetPrinter(handle, 2)

            printer_details.pop('pDevMode', None)
            printer_details.pop('pSecurityDescriptor', None)

            printer_info.append(printer_details)

        return printer_info

    @staticmethod
    def get_ports(printer_name):
        """Recebe o nome da impressora e retorna o nome das portas da impressora recebida."""
        try:
            printer_info = win32print.GetPrinter(printer_name, 2)
            ports = printer_info['pPort']
            return ports
        except Exception as e:
            return f"Erro ao obter portas: {e}"

    @staticmethod
    def check_port_exists(printer_name, port_name):
        """Confere se uma porta de uma impressora X existe."""
        ports = PrinterManager.get_ports(printer_name)
        return port_name in ports if isinstance(ports, list) else False

    @staticmethod
    def set_port_value(printer_name, port_name, value, monitor=None):
        """Altera o valor da porta da impressora."""
        try:
            return f"Alterando porta: Impressora: {printer_name}, Porta: {port_name}, Valor: {value}, Monitor: {monitor}"
        except Exception as e:
            return f"Erro ao alterar porta: {e}"

    @staticmethod
    def create_port(printer_name, port_name, value, monitor=None):
        """Cria uma nova porta com o valor especificado para a impressora."""
        try:
            return f"Criando porta: Impressora: {printer_name}, Porta: {port_name}, Valor: {value}, Monitor: {monitor}"
        except Exception as e:
            return f"Erro ao criar porta: {e}"

    @staticmethod
    def delete_port(printer_name, port_name):
        """Exclui uma porta de uma impressora se existir."""
        try:
            return f"Excluindo porta: Impressora: {printer_name}, Porta: {port_name}"
        except Exception as e:
            return f"Erro ao excluir porta: {e}"
