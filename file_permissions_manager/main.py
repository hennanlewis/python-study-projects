from permission_manager import PermissionManager

# Caminho do diretório a ser processado
path_to_process = r"C:\Windows\Sistem32"

# Cria uma instância do PermissionManager
permission_manager = PermissionManager(path_to_process)

# Executa o processamento
permission_manager.process_directory(use_bulk=False)
