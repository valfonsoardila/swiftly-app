import os
import shutil
import subprocess
import socket
import zipfile


def create_skeleton():
    name_root = "main"
    # Ejecutar reflex init
    subprocess.run(["reflex", "init"], check=True)

    # Obtener el nombre del directorio actual (nombre del proyecto)
    original_name = os.path.basename(os.getcwd())

    # Reemplazar caracteres problemáticos en el nombre original
    expected_folder_name = original_name.replace("-", "_").replace(" ", "_")

    # Buscar la carpeta creada por reflex init
    created_folder_name = None
    for item in os.listdir():
        if os.path.isdir(item) and item.lower() == expected_folder_name.lower():
            created_folder_name = item
            break

    # Renombrar la carpeta encontrada
    if created_folder_name:
        os.rename(created_folder_name, name_root)

        # Actualizar el archivo rxconfig.py
        update_rxconfig_app_name(name_root)

    # Renombrar el archivo disparador de la aplicación
    for item in os.listdir():
        if os.path.isdir(item) and item.lower() == name_root:
            # Entra y buscar el archivo que concuerda con el valor de original_name + .py
            # Y lo reemplaza por el valor de expected_folder_name + .py
            for file in os.listdir(item):
                if file.lower() == f"{created_folder_name}.py":
                    os.rename(
                        os.path.join(item, file),
                        os.path.join(item, f"{name_root}.py"),
                    )
                    break
            break

    # Eliminar __pycache__
    delete_pycache()

    # Crear las carpetas adicionales
    server_path = os.path.join(name_root, "server")
    ui_path = os.path.join(name_root, "ui")

    # Crear carpetas server/api, server/controllers, server/models
    os.makedirs(os.path.join(server_path, "api"), exist_ok=True)
    os.makedirs(os.path.join(server_path, "controllers"), exist_ok=True)
    os.makedirs(os.path.join(server_path, "models"), exist_ok=True)

    # Crear carpetas ui/views, ui/states
    os.makedirs(os.path.join(ui_path, "views"), exist_ok=True)
    os.makedirs(os.path.join(ui_path, "states"), exist_ok=True)


def update_rxconfig_app_name(new_app_name):
    # Ruta del archivo rxconfig.py en la raíz del proyecto
    rxconfig_path = "rxconfig.py"

    # Verificar si el archivo existe
    if os.path.exists(rxconfig_path):
        with open(rxconfig_path, "r") as file:
            lines = file.readlines()

        # Reemplazar el valor de app_name
        with open(rxconfig_path, "w") as file:
            for line in lines:
                if "app_name=" in line:
                    line = f'    app_name="{new_app_name}",\n'
                file.write(line)


def get_free_port(default_port):
    """Intenta usar el puerto predeterminado, si está ocupado, busca otro libre."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("", default_port))
            return default_port
        except OSError:
            s.bind(("", 0))
            return s.getsockname()[1]


def run_frontend(default_port=8080):
    """Ejecuta el frontend en el puerto especificado o en uno dinámico."""
    frontend_port = get_free_port(default_port)
    subprocess.run(["reflex", "run", f"--frontend-port={frontend_port}"], check=True)
    delete_pycache()


def run_backend(default_port=8000):
    """Ejecuta el backend en el puerto especificado o en uno dinámico."""
    backend_port = get_free_port(default_port)
    subprocess.run(["reflex", "run", f"--backend-port={backend_port}"], check=True)
    delete_pycache()


def delete_build_folder():
    build_dir = "build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        print(f"Carpeta {build_dir} eliminada.")


def export_frontend():
    delete_build_folder()  # Eliminar la carpeta build antes de exportar
    subprocess.run(["reflex", "export", "--frontend-only"], check=True)

    zip_filename = "frontend.zip"
    build_dir = "build"

    if os.path.exists(zip_filename):
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
            zip_ref.extractall(build_dir)

        os.remove(zip_filename)
        print(f"Frontend exportado y descomprimido en la carpeta {build_dir}")
    else:
        print("El archivo frontend.zip no fue encontrado.")


def export_backend():
    delete_build_folder()  # Eliminar la carpeta build antes de exportar
    subprocess.run(["reflex", "export", "--backend-only"], check=True)

    zip_filename = "backend.zip"
    build_dir = "build"

    if os.path.exists(zip_filename):
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
            zip_ref.extractall(build_dir)

        os.remove(zip_filename)
        print(f"Backend exportado y descomprimido en la carpeta {build_dir}")
    else:
        print("El archivo backend.zip no fue encontrado.")


def delete_pycache():
    # Recorrer el árbol de directorios y eliminar __pycache__
    for root, dirs, files in os.walk("."):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                pycache_path = os.path.join(root, dir_name)
                shutil.rmtree(pycache_path)
