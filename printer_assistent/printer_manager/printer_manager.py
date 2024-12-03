import win32print
from icecream import ic

class PrinterManager:

    @staticmethod
    def get_printers_list():
        """Retorna a lista de impressoras atuais do computador com seus respectivos detalhes."""

        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        printer_info = []

        for printer in printers:
            printer_name = printer[2]

            try:
                handle = win32print.OpenPrinter(printer_name)
                printer_details = win32print.GetPrinter(handle, 2)
                printer_info.append(printer_details)
            except Exception as e:
                printer_info.append({'error': f"Erro ao obter detalhes da impressora '{printer_name}': {e}"})

        return printer_info

    @staticmethod
    def get_ports(printer_name):
        """Recebe o nome da impressora e retorna o nome das portas associadas a ela."""

        try:
            handle = win32print.OpenPrinter(printer_name)
            printer_info = win32print.GetPrinter(handle, 2)
            return printer_info.get('pPort', [])
        except Exception as e:
            raise RuntimeError(f"Erro ao obter portas da impressora '{printer_name}': {e}")

    @staticmethod
    def check_port_exists(printer_name, port_name):
        """Verifica se uma porta específica existe para a impressora fornecida."""

        try:
            ports = PrinterManager.get_ports(printer_name)
            return port_name in ports
        except Exception as e:
            raise RuntimeError(f"Erro ao consultar portas da impressora '{printer_name}': {e}")

    @staticmethod
    def set_port_value(printer_name, port_name, value, monitor=None):
        """Altera o valor de uma porta da impressora."""

        try:
            return f"Alterando porta: Impressora: {printer_name}, Porta: {port_name}, Valor: {value}, Monitor: {monitor}"
        except Exception as e:
            raise RuntimeError(f"Erro ao alterar porta da impressora {printer_name}: {e}")

    @staticmethod
    def create_port(printer_name, port_name, value, monitor=None):
        """Cria uma nova porta para a impressora."""

        try:
            return f"Criando porta: Impressora: {printer_name}, Porta: {port_name}, Valor: {value}, Monitor: {monitor}"
        except Exception as e:
            raise RuntimeError(f"Erro ao criar porta para a impressora {printer_name}: {e}")

    @staticmethod
    def delete_port(printer_name, port_name):
        """Exclui uma porta de uma impressora se ela existir."""

        try:
            return f"Excluindo porta: Impressora: {printer_name}, Porta: {port_name}"
        except Exception as e:
            raise RuntimeError(f"Erro ao excluir porta da impressora {printer_name}: {e}")
