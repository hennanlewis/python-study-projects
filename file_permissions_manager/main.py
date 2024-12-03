from permission_manager import PermissionManager

if __name__ == "__main__":
    path_to_process = r"C:\Windows\Sistem32"

    permission_manager = PermissionManager(path_to_process)
    permission_manager.process_directory(use_bulk=False)
