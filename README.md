ODOO

1.-   Explica brevemente qué contiene cada una de las siguientes carpetas o archivos de un módulo Odoo:
•	__manifest__.py
Contiene metadatos esenciales sobre el módulo como, nombre, versión, categoría, autor y las dependencias.
•	__init__.py
Este archivo es requerido en cada directorio de Python para indicar que contiene paquetes que pueden ser importados.
•	/models/
Esta carpeta contiene los archivos Python que definen los modelos de datos (clases Python que mapean tablas en la base de datos) del módulo.
•	/views/
Esta carpeta contiene los archivos XML que definen la interfaz de usuario del módulo.
•	/security/
Esta carpeta contiene los archivos de configuración para la seguridad y los derechos de acceso del módulo. El archivo principal es a menudo ir.model.access.csv, que define los permisos de acceso (lectura, escritura, creación, eliminación) para los modelos del módulo, basados en grupos de usuarios.
•	/data/
Esta carpeta contiene archivos XML o CSV con datos de inicialización o configuración que se cargan automáticamente al instalar el módulo. Esto incluye datos estáticos, como registros por defecto, secuencias, tipos de datos predefinidos, o incluso a veces archivos de seguridad o vistas que se quiere cargar de forma separada.





2.-  ¿Qué significa el parámetro depends dentro del archivo __manifest__.py?
Da un ejemplo realista.
El parámetro depends dentro del archivo __manifest__.py es una lista de nombres técnicos de otros módulos Odoo que el módulo actual necesita para funcionar correctamente.
Esto establece una dependencia obligatoria, lo que significa que Odoo:
1.	Instalará automáticamente todos los módulos listados en depends antes de instalar el módulo actual.
2.	Garantiza que el código y los datos (modelos, vistas, campos, etc.) de los módulos dependientes estén disponibles para ser usados por el módulo actual.
Supongamos que estás creando un módulo llamado school_management y quieres que la información del estudiante se integre con la funcionalidad de gestión de contactos y usuarios que ya existe en Odoo.
{
    'name': "School Management",
    'version': '1.0',
    'category': 'Education',
    
    'depends': ['base', 'mail'],
    'data': [
        #archivos de vistas y seguridad 
    ],
    'installable': True,
    'application': True,
}



3.-  ¿Cuál es la diferencia entre un modelo transitorio (TransientModel) y un modelo normal (Model)?
La diferencia principal entre un modelo normal (Model) y un modelo transitorio (TransientModel) en Odoo radica en su propósito y en cómo Odoo gestiona sus datos en la base de datos.
Usa Model para todo lo que debe guardarse de forma permanente y TransientModel para formularios que solo existen para guiar al usuario a través de una acción (como la impresión de un documento o una importación de datos) y cuyos datos deben limpiarse después.



4.- ¿Qué hace el campo api.depends() en un método de un modelo?
Da un ejemplo corto de código.
Declarar qué campos deben ser monitoreados para que, cuando cambien sus valores, el método calculado se vuelva a ejecutar y actualice el valor del campo destino. Es una regla de re-cálculo de datos.
from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    age = fields.Integer(string='Age') # 
    # Nuestro campo calculado que NO se almacena en la BD (store=False por defecto)
    age_status = fields.Char(string='Age Status', compute='_compute_age_status') 

    # El método computado
    @api.depends('age') 
    def _compute_age_status(self):
        for record in self:
            if record.age >= 18:
                record.age_status = 'Adulto'
            else:
                record.age_status = 'Menor'




5.-  ¿Qué diferencia hay entre los campos Many2one, One2many y Many2many?
Estas son las relaciones de los campos  donde Many2one es muchos a 1 por ejemplo muchos estudiantes apuntan a un solo asesor
O en One2many uno a muchos por ejemplo un curso tiene muchos estudiantes 
Por ultimo Many2many muchos a muchos donde muchos estudiantes se relacionan con múltiples cursos aun que aquí se utilizaría una tabla pivote




6.- El módulo se debe llamar school_management y tener una estructura completa.
Debe incluir como mínimo:
school_management/
├── __init__.py
├── __openerp__.py
├── models/
│   ├── __init__.py
│   └── student.py
├── views/
│   └── student_view.xml
├── security/
│   ├── ir.model.access.csv
└── data/

2.- En student.py, define un modelo school.student con los siguientes campos:
•	name (Char)
•	age (Integer)
•	birth_date (Date)
•	email (Char)
•	active (Boolean, por defecto True)
3.- Crea una vista tipo form y tree en el archivo student_view.xml.
4.- Incluir el menú:
•	School Management → Students
5.- Genera las reglas de acceso básicas en ir.model.access.csv.
