# Swiftly App

![Intro](https://github.com/user-attachments/assets/5d35f8a3-a4b9-4edb-b016-063ce30bb174)

## Diagrama de clases

![Diagrama de clases](https://github.com/user-attachments/assets/f807f06a-9172-4f20-8d20-4f592d91842e)

## Descripcion del proyecto

Este es un proyecto hecho en Reflex - instalada cuando ejecutas `reflex init`.
Al iniciar este comando tome una plantilla en blanco de todas las plantillas disponibles `--template blank`
Si desea utilizar una plantilla diferente, pase la bandera `--template` a `reflex init`.
Por ejemplo, si desea un punto de partida más básico, puede ejecutar:

```bash
reflex init --template blank
```

## `Instalacion del proyecto paso a paso`

- ### `Crear el entorno virtual`
```bash
# Comando para crear el entorno virtual
python3 -m venv .venv
```
- ### `Activar el entorno virtual con poetry`
```bash
# Comando para activar el entorno virual
poetry shell
```
- ### `Instalacion de dependencias`
Esto instalará las dependencias definidas en pyproject.toml lo que incluye la instalacion de reflex dentro del entorno
```bash
# Comando para instalar las dependencias
poetry install
```
- ### `Inicializar el proyecto reflex`
Se debe proceder a crear el proyecto con reflex a tarves de comandos definidos con poetry `Nota: esto hará una ahorro de trabajo manual`
debe escoger un proyecto en blanco en el menu de opciones que le ofrece poetry
```bash
# Comando para crear el esqueleto del proyecto
poetry run create-skln
```
- ### `Correr el proyecto en modo desarrollo`
```bash
# Comando para correr el proyecto en modo desarrollo
poetry run --frontend
```

- ### `Crear estructura monorepo`
```bash
# Comando para crear estructura basica y vacia en monorepo
poetry run create-skln
```

## Estructura inicial para automatizar reflex 

Esta plantilla tiene la siguiente estructura de directorios:

```bash
├── .env
├── .gitignore
├── Readme.md
├── core.py
├── poetry.lock
└── pyproject.toml
```

Consulte [Project Structure docs](https://reflex.dev/docs/getting-started/project-structure/) para obtener más información sobre la estructura general de los proyectos Reflex.
