{
    'name': "School Management",
    'summary': "Manage student records for a school.",
    'description': "A custom module for managing student information.",
    'author': "Your Name",
    'category': 'Education',
    'version': '1.0',
    
    # 2.- Dependencia esencial
    'depends': ['base'],

    # 3. & 4. Datos: Vistas, Seguridad y Menús
    'data': [
        'security/ir.model.access.csv', # Reglas de acceso (5)
        'views/student_view.xml',        # Vistas y menú (3 y 4)
    ],
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}