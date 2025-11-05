libreria_gran_poeta/
│
├── inventario/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               modelos actualizados y migrados correctamente
│   ├── views.py                incluye CRUD de productos + movimientos + historial
│   ├── urls.py                 con rutas: list, crear, editar, eliminar, movimiento, movimientos
│   └── templates/
│       └── inventario/
│           ├── base.html       con Bootstrap y barra superior funcional
│           ├── producto_list.html
│           ├── producto_form.html
│           ├── movimiento_form.html
│           ├── movimiento_list.html
│           └── producto_confirm_delete.html (probablemente básico)
│
├── libreria_gran_poeta/
│   ├── settings.py            corregido con idioma, zona horaria, rutas y static
│   ├── urls.py                con redirect hacia /productos/
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3                  base de datos local funcionando
├── manage.py
├── requirements.txt            (versión Django 5.2.7)
└── .venv/                      entorno virtual activo


#


# 📚 Librería *El Gran Poeta*
**Proyecto académico — Ingeniería de Software**

Sistema de gestión de inventario y bodegas desarrollado en **Django**, para la librería *El Gran Poeta*.  
Permite administrar productos, controlar movimientos de stock, gestionar bodegas y mantener un historial de entradas, salidas y traslados.

---

## 🧠 Objetivo del proyecto
Desarrollar un **prototipo funcional de software** para la administración de inventario de una librería, implementando buenas prácticas de ingeniería de software, metodologías ágiles (Scrum) y diseño modular en Django.

---

## ⚙️ Tecnologías utilizadas
- **Lenguaje:** Python 3.14  
- **Framework web:** Django 5.2.7  
- **Base de datos:** SQLite3  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Entorno:** Visual Studio Code  
- **Control de versiones:** Git / GitHub

---

## 🧩 Estructura del proyecto

