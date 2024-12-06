from typing import List, Dict
from icecream import ic
import win32print
import subprocess

class PrinterManager:
    """Gerencia impressoras e portas associadas no sistema."""

    def __init__(self):
        """Inicializa o gerenciador de impressoras e define atributos relacionados."""

        self._printers_data = self._fetch_printer_list()
        self.printers_names = [printer["name"] for printer in self._printers_data]
        self.printer_list = self._printers_data

    def _fetch_printer_list(self) -> List[Dict]:
        """Obtém a lista de impressoras disponíveis com seus detalhes."""

        printers = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
        )
        printer_info = []

        for printer in printers:
            printer_name = printer[2]

            try:
                handle = self._open_printer(printer_name)
                printer_details = win32print.GetPrinter(handle, 2)
                printer_info.append({ "name": printer_name, "printer_details": printer_details })
            except Exception as e:
                raise RuntimeError(f"Erro ao acessar a impressora '{printer_name}': {e}")
        
        return printer_info

    def get_printers_ports(self) -> List[Dict]:
        """Obtém a lista de portas associadas às impressoras disponíveis."""

        if not self.printers_names:
            return []
        try:
            first_printer_name = self.printers_names[2]
            handle = self._open_printer(first_printer_name)
            printer = win32print.GetPrinter(handle, 2)
            return win32print.EnumPorts(printer.get("pPortsName"), 2)
        except win32print.error as e:
            raise RuntimeError(f"Erro ao obter portas: {e}")

    def check_port_exists(self, port_name: str) -> bool:
        """Verifica se uma porta específica existe."""

        return any(port.get("Name") == port_name for port in self.get_printers_ports())

    def create_ip_port(self, port_name: str, port_value: str) -> str:
        """Cria uma nova porta TCP/IP para a impressora."""

        if self.check_port_exists(port_name):
            response = f"Porta '{port_name}' já existe."
            return response

        command = [
            "powershell",
            "-Command",
            f"Add-PrinterPort -Name '{port_name}' -PrinterHostAddress '{port_value}'",
        ]

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return f"Nova porta TCP/IP '{port_name}' com IP '{port_value}' criada com sucesso!"
        except subprocess.CalledProcessError as e:
            ic(e.stderr)
            raise RuntimeError(f"Erro ao criar porta '{port_name}': {e.stderr}")

    def delete_port(self, port_name: str) -> str:
        """Exclui uma porta de impressora."""

        command = ["powershell", "-Command", f"Remove-PrinterPort -Name '{port_name}'"]
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return f"Porta '{port_name}' apagada com sucesso!"
        except subprocess.CalledProcessError as e:
            ic(e.stderr)
            raise RuntimeError(f"Erro ao apagar porta '{port_name}': {e.stderr}")

    @staticmethod
    def _open_printer(printer_name: str):
        """Helper para abrir uma impressora com suporte a context manager."""

        handle = win32print.OpenPrinter(printer_name)
        return handle
