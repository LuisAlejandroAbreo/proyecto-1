👥 Tipos de Usuario
🔐 Administrador

Registrar, actualizar y eliminar usuarios

Registrar, actualizar e inactivar herramientas

Aprobar solicitudes de préstamo

Ver todos los reportes

Gestionar devoluciones

👤 Usuario (Residente)

Consultar herramientas disponibles

Ver estado y disponibilidad

Crear solicitudes de préstamo

Consultar su historial de préstamos

🧰 Funcionalidades
Gestión de Herramientas

Crear herramientas

Listar herramientas

Buscar herramienta por ID o nombre

Actualizar información

Inactivar herramienta

Control de stock

Estados: activa, en reparación, fuera de servicio

Gestión de Usuarios

Crear usuario

Listar usuarios

Buscar usuario

Actualizar datos

Eliminar usuario

Gestión de Préstamos

Registrar préstamo

Validar disponibilidad

Ajustar stock automáticamente

Registrar devolución

Cambiar estado (activo, vencido, devuelto)

Agregar observaciones

Reportes Disponibles

Herramientas con stock bajo (< 3 unidades)

Préstamos activos

Préstamos vencidos

Historial de préstamos por usuario

Herramientas más solicitadas

Usuarios que más solicitan herramientas

Registro de Eventos (Logs)

Todos los errores y eventos relevantes se almacenan en:

logs.txt


Ejemplos:

Intentar prestar más herramientas de las disponibles

Intentar prestar una herramienta fuera de servicio

Errores de validación

Accesos no autorizados

📂 Estructura del Proyecto (Ejemplo)
📁 proyecto-herramientas
│── main.py
│── herramientas.py
│── usuarios.py
│── prestamos.py
│── reportes.py
│── logs.txt
│── README.md


(La estructura puede variar según tu implementación)

🔄 Flujo General del Sistema

Inicio del programa

Inicio de sesión según tipo de usuario

Menú principal

Acceso a módulos según permisos

Registro automático de eventos

🛡️ Validaciones Importantes

No se pueden prestar herramientas sin stock disponible.

No se puede prestar una herramienta en reparación o fuera de servicio.

Solo el administrador puede aprobar solicitudes.

El stock se actualiza automáticamente en préstamos y devoluciones.

👨‍💻 Autor

Proyecto desarrollado como práctica académica para la gestión comunitaria de herramientas.
