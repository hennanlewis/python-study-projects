import subprocess
import os

class PermissionManager:
    def __init__(self, directory):
        self.directory = directory
        self.success_count = 0
        self.failure_count = 0
        self.success_log = "success_files.txt"
        self.failure_log = "failure_files.txt"

    def _log_result(self, file_path, is_success):
        """Salva o caminho do arquivo no log correspondente (sucesso ou falha)."""
        log_file = self.success_log if is_success else self.failure_log
        with open(log_file, "a", encoding="utf-8") as log:  # Adicionando a codificação UTF-8
            log.write(file_path + "\n")

    def _change_permissions(self, file_path):
        """Muda as permissões de um arquivo ou diretório individualmente."""
        try:
            subprocess.run(["takeown", "/F", file_path, "/A"], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(["icacls", file_path, "/grant", "Todos:F"], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Sucesso: {file_path}")
            self._log_result(file_path, True)
            self.success_count += 1
        except subprocess.CalledProcessError:
            print(f"Falha: {file_path}")
            self._log_result(file_path, False)
            self.failure_count += 1

    def _change_permissions_bulk(self, directory):
        """Altera as permissões para todos os arquivos e diretórios em lote."""
        try:
            subprocess.run(["takeown", "/F", directory, "/R", "/A"], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(["icacls", directory, "/grant", "Todos:F", "/T"], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Sucesso: Permissões alteradas para todos os arquivos em {directory}")
            self._log_result(directory, True)
            self.success_count += 1
        except subprocess.CalledProcessError:
            print(f"Falha: Não foi possível alterar as permissões para {directory}")
            self._log_result(directory, False)
            self.failure_count += 1

    def process_directory(self, use_bulk=False):
        """Percorre o diretório e altera as permissões de todos os arquivos e pastas."""
        if use_bulk:
            self._change_permissions_bulk(self.directory)
        else:
            for root, dirs, files in os.walk(self.directory):
                self._change_permissions(root)
                for file in files:
                    file_path = os.path.join(root, file)
                    self._change_permissions(file_path)

        print(f"\n{self.success_count} arquivos ou pastas processados com sucesso.")
        print(f"{self.failure_count} falhas no processamento de arquivos ou pastas.")
