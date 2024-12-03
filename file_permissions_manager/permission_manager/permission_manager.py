import os
import subprocess
from typing import Optional, Callable

class PermissionManager:
    SUCCESS_LOG = "success_files.txt"
    FAILURE_LOG = "failure_files.txt"
    PERMISSIONS = "Todos:F"

    def __init__(self, directory: str, logger: Optional[Callable[[str], None]] = print):
        """Gerencia permissões de arquivos e diretórios."""

        self.directory = directory
        self.success_count = 0
        self.failure_count = 0
        self.logger = logger

    def _log_result(self, file_path: str, is_success: bool) -> None:
        """Registra o resultado (sucesso ou falha) no log correspondente."""

        log_file = self.SUCCESS_LOG if is_success else self.FAILURE_LOG
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(file_path + "\n")

    def _run_command(self, command: list[str], description: str) -> bool:
        """Executa um comando no sistema e captura o resultado."""

        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.logger(f"Sucesso: {description}")
            return True
        except subprocess.CalledProcessError:
            self.logger(f"Falha: {description}")
            return False

    def _change_permissions(self, file_path: str, recursive: bool = False) -> None:
        """Altera permissões de um arquivo ou diretório."""

        takeown_cmd = ["takeown", "/F", file_path, "/A"] + (["/R"] if recursive else [])
        icacls_cmd = ["icacls", file_path, "/grant", self.PERMISSIONS] + (["/T"] if recursive else [])

        success = (
            self._run_command(takeown_cmd, f"Take Ownership - {file_path}") and
            self._run_command(icacls_cmd, f"Set Permissions - {file_path}")
        )

        self._log_result(file_path, success)
        if success:
            self.success_count += 1
        else:
            self.failure_count += 1

    def process_directory(self, use_bulk: bool = False) -> None:
        """Processa um diretório para alterar permissões de arquivos e subdiretórios."""

        if use_bulk:
            self._change_permissions(self.directory, recursive=True)
        else:
            for root, _, files in os.walk(self.directory):
                self._change_permissions(root)
                for file in files:
                    self._change_permissions(os.path.join(root, file))

        self.logger(f"\n{self.success_count} itens processados com sucesso.")
        self.logger(f"{self.failure_count} falhas no processamento.")

