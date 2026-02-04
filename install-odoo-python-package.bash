#!/bin/bash

# --- CONFIGURACIÓN ---
ODOO_VERSION="19.0"
# Donde se descargará el repo completo
REPO_DIR="/usr/local/src/odoo_repo"
# La carpeta que contiene el núcleo (donde está el __init__.py)
LIB_SOURCE="$REPO_DIR/odoo"

if [[ $EUID -ne 0 ]]; then
   echo "❌ Ejecuta con sudo"
   exit 1
fi

# 1. Descargar el repositorio si no existe
if [ -d "$REPO_DIR" ]; then
    echo "👍 El repositorio ya existe en $REPO_DIR"
else
    echo "📥 Descargando repositorio de Odoo $ODOO_VERSION..."
    git clone --depth 1 --branch $ODOO_VERSION https://github.com/odoo/odoo.git $REPO_DIR
fi

# 2. Obtener la ruta de site-packages de Python de forma dinámica
PYTHON_SITE_PACKAGES=$(python3 -c "import site; print(site.getsitepackages()[0])")

echo "🔗 Vinculando la subcarpeta 'odoo' en $PYTHON_SITE_PACKAGES"

# 3. Crear un archivo .pth para que Python reconozca la carpeta 'odoo'
# Esto permite que 'import odoo' funcione apuntando directamente al código fuente
echo "$REPO_DIR" > "$PYTHON_SITE_PACKAGES/odoo_dev.pth"

# 4. Asegurar que las dependencias mínimas para tipado estén presentes
echo "📦 Instalando dependencias de tipado..."
pip3 install --break-system-packages \
    babel \
    pytz \
    werkzeug \
    lxml \
    psycopg2-binary

echo "=================================================="
echo "✅ ¡Configuración completada!"
echo "📍 Repositorio: $REPO_DIR"
echo "📂 Paquete Python: $LIB_SOURCE"
echo "🐍 Ahora 'import odoo' funcionará en cualquier script global."
echo "=================================================="