# Módulos de Odoo 19

Este repositorio contiene múltiples módulos personalizados para Odoo 19 desarrollados en un entorno de Codespace preparado. Se incluyen diferentes funcionalidades empresariales según los módulos implementados.

## Requisitos Previos

- Docker y Docker Compose instalados
- Bash shell disponible
- Acceso a internet para descargar las imágenes de Docker

> [!IMPORTANT]  
> Antes de iniciar Docker, debe crear el archivo `config/odoo.conf` en la carpeta `config`. Este archivo es necesario para que la configuración de Odoo funcione correctamente. Consulte la estructura del proyecto para la ubicación exacta.

## Estructura del Proyecto

```
├── addons/                        # Carpeta de módulos personalizados
│   ├── gestion-vehiculos/         # Módulo de gestión de vehículos
│   │   ├── models/                # Modelos de datos
│   │   ├── views/                 # Vistas XML
│   │   ├── controllers/           # Controladores
│   │   ├── security/              # Permisos y acceso
│   │   └── demo/                  # Datos de demostración
│   └── [otros módulos]/           # Espacio para más módulos
├── config/
│   └── odoo.conf                  # Configuración de Odoo
├── compose.yml                    # Configuración de Docker Compose
└── install-odoo-python-package.bash  # Script de instalación de dependencias
```

## Configuración Previa - ⚠️ OBLIGATORIO

Antes de proceder con la instalación, **debe crear el archivo `config/odoo.conf`**. Este archivo contiene las configuraciones esenciales para que Odoo funcione correctamente.

El archivo `config/odoo.conf` debe estar presente en la carpeta `config/` para que:
- Docker Compose pueda montar la configuración correctamente
- Odoo se inicie con los parámetros adecuados
- Funcione la conexión a la base de datos PostgreSQL

Asegúrese de que existe este archivo antes de ejecutar `docker-compose up`.

## Instrucciones de Instalación

### 1. Iniciar Docker con Docker Compose

Para iniciar los servicios de Docker (Odoo y PostgreSQL):

```bash
docker-compose up -d
```

Este comando:
- Crea e inicia los contenedores definidos en `compose.yml`
- Descarga las imágenes necesarias si no están disponibles
- Ejecuta los servicios en segundo plano (`-d`)

Para detener los servicios:

```bash
docker-compose down
```

Para ver los logs en tiempo real:

```bash
docker-compose logs -f
```

### 2. Instalar el Paquete de Python de Odoo

Para instalar las dependencias de Python necesarias para Odoo, ejecute el script de instalación:

```bash
bash install-odoo-python-package.bash
```

Este script se encarga de:
- Instalar todas las dependencias de Python requeridas por Odoo
- Configurar el entorno necesario para los módulos personalizados

### 3. Acceder a Odoo

Una vez que los servicios estén en ejecución, acceda a Odoo en su navegador:

```
http://localhost:8069
```

Credenciales por defecto:
- Usuario: `admin`
- Contraseña: `admin` (verificar en `config/odoo.conf` si es diferente)

## Flujo Completo de Configuración

1. **Iniciar Docker Compose:**
   ```bash
   docker-compose up -d
   ```

2. **Instalar dependencias de Python:**
   ```bash
   bash install-odoo-python-package.bash
   ```

3. **Acceder a Odoo:**
   - Abrir navegador en `http://localhost:8069`
   - Ingresar credenciales

4. **Instalar módulos personalizados:**
   - En Odoo, ir a Aplicaciones
   - Hacer clic en "Actualizar Lista de Aplicaciones"
   - Buscar los módulos de esta carpeta (ej: "gestion-vehiculos")
   - Hacer clic en Instalar en cada módulo deseado

## Módulos Disponibles

Los módulos personalizados se encuentran en la carpeta `addons/`. Actualmente se incluyen:

- **gestion-vehiculos**: Módulo de gestión de flota que incluye:
  - Gestión de vehículos
  - Gestión de empleados
  - Gestión de marcas
  - Registro de multas

Se pueden agregar más módulos siguiendo la estructura de directorios existente.

## Notas Importantes

- Los módulos pueden incluir datos de demostración que se cargan al instalar
- La configuración de Odoo se encuentra en `config/odoo.conf`
- Todos los módulos personalizados están en la carpeta `addons/`
- El entorno está preparado para desarrollo en Codespace
- Cada módulo debe cumplir con la estructura estándar de Odoo

## Troubleshooting

Si encuentra errores al iniciar Docker:
- Verifique que Docker y Docker Compose estén correctamente instalados
- Asegúrese de tener suficiente espacio en disco
- Revise los logs con `docker-compose logs`

Si hay problemas con la instalación de Python:
- Ejecute el script nuevamente: `bash install-odoo-python-package.bash`
- Verifique que tiene permisos de ejecución: `chmod +x install-odoo-python-package.bash`

## Desarrollo

Para hacer cambios en los módulos:
1. Modifique los archivos en la carpeta `addons/` (en el módulo correspondiente)
2. Reinicie el servidor Odoo dentro del contenedor
3. Actualice el módulo en la interfaz de Odoo (Aplicaciones → Actualizar Lista de Aplicaciones)

Para agregar un nuevo módulo:
1. Cree una nueva carpeta en `addons/` con el nombre del módulo
2. Siga la estructura estándar de Odoo (models, views, controllers, etc.)
3. Incluya el archivo `__manifest__.py` con la configuración del módulo
4. Reinicie el servidor para que Odoo detecte el nuevo módulo
