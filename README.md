🎥 Sistema de Gestión de Préstamo de Herramientas

🔗 Video de Sustentación:
https://drive.google.com/file/d/1TarIKlmyC9ZG1RDuvIXQdRK6GXw-XGdF/view?usp=sharing

👥 Tipos de Usuario
🔐 Administrador

Tiene control total del sistema:

✅ Registrar, actualizar y eliminar usuarios

✅ Registrar, actualizar e inactivar herramientas

✅ Aprobar solicitudes de préstamo

✅ Gestionar devoluciones

✅ Ver todos los reportes

✅ Supervisar el registro de eventos (logs)

👤 Usuario (Residente)

Cuenta con acceso limitado:

🔎 Consultar herramientas disponibles

📊 Ver estado y disponibilidad

📝 Crear solicitudes de préstamo

📚 Consultar su historial de préstamos

🧰 Funcionalidades del Sistema
🔧 Gestión de Herramientas

➕ Crear herramientas

📋 Listar herramientas

🔎 Buscar herramienta por ID o nombre

✏️ Actualizar información

🚫 Inactivar herramienta

📦 Control automático de stock

📌 Estados posibles:

🟢 Activa

🟡 En reparación

🔴 Fuera de servicio

👥 Gestión de Usuarios

➕ Crear usuario

📋 Listar usuarios

🔎 Buscar usuario

✏️ Actualizar datos

❌ Eliminar usuario

🔄 Gestión de Préstamos

📝 Registrar préstamo

✔️ Validar disponibilidad

📉 Ajustar stock automáticamente

🔁 Registrar devolución

🔄 Cambiar estado del préstamo:

Activo

Vencido

Devuelto

🗒️ Agregar observaciones

📊 Reportes Disponibles

El sistema genera reportes automáticos como:

⚠️ Herramientas con stock bajo (< 3 unidades)

📌 Préstamos activos

⏰ Préstamos vencidos

📚 Historial de préstamos por usuario

🔝 Herramientas más solicitadas

👥 Usuarios que más solicitan herramientas

📝 Registro de Eventos (Logs)

Todos los errores y eventos importantes se almacenan en:

📄 logs.txt

Ejemplos de registros:

❌ Intentar prestar más herramientas de las disponibles

❌ Intentar prestar una herramienta fuera de servicio

⚠️ Errores de validación

🔐 Accesos no autorizados

Esto permite mayor control, seguridad y trazabilidad del sistema.

📂 Estructura del Proyecto
📁 proyecto-herramientas
│── main.py
│── herramientas.py
│── usuarios.py
│── prestamos.py
│── reportes.py
│── logs.txt
│── README.md


(La estructura puede variar según la implementación)

🔄 Flujo General del Sistema

1️⃣ Inicio del programa
2️⃣ Inicio de sesión según tipo de usuario
3️⃣ Menú principal
4️⃣ Acceso a módulos según permisos
5️⃣ Registro automático de eventos

🛡️ Validaciones Importantes

El sistema garantiza reglas de negocio como:

🚫 No se pueden prestar herramientas sin stock disponible.

🚫 No se puede prestar una herramienta en reparación o fuera de servicio.

🔐 Solo el administrador puede aprobar solicitudes.

✅ Conclusión

Este sistema permite:

📊 Mejor control de inventario

🔐 Seguridad en la gestión de préstamos

📈 Generación automática de reportes

📝 Registro detallado de eventos

⚙️ Organización modular y escalable

El stock se actualiza automáticamente en préstamos y devoluciones.

👨‍💻 Autor

Proyecto desarrollado como práctica académica para la gestión comunitaria de herramientas.
