import PySimpleGUI as sg
import os

def crear_menu():
    path = os.path.abspath(os.path.dirname(__file__))
    imgAlumnos = os.path.join(path, 'alumnos.png')
    imgPagos = os.path.join(path, 'pagos.png')
    imgSalir = os.path.join(path, 'salir.png')
    
    layout = [[sg.Text(' Sistema integral de GymApp',size=(22,1), font=("Helvetica", 20))],
              [sg.Text(' '*1), sg.Button(key='Alumnos', image_filename=imgAlumnos, image_subsample=4, border_width=1), sg.Text(' '*4),
              sg.Button(key='Pagos',image_filename=imgPagos, image_subsample=4, border_width=1)],
              [sg.Text('     Alumnos'), sg.Text(' '*29), sg.Text('Pagos')],
              [sg.Text('')],
              [sg.Text(' '*1), sg.Button(key='Salir', image_filename=imgSalir, border_width=1)]]
    return sg.Window('GymApp', layout, finalize=True, size=(410,280))

def crear_tabla_alumnos():
    sg.change_look_and_feel('DarkBlue8')
    head = ['#','Apellido','Nombre','DNI']
    layout = [[sg.Table(values=[], headings=head,
        col_widths = (5,15,15,10),
        auto_size_columns=False,
        display_row_numbers=False,
        select_mode=sg.TABLE_SELECT_MODE_BROWSE,
        num_rows=15,
        font=('Arial',12),
        justification='left',
        text_color='black',
        background_color='lightblue',
        alternating_row_color='white',
        selected_row_colors=('white','blue'),          
        header_text_color='#f1c40f',
        header_background_color='#16a085',
        header_font=('Arial',12,'bold'),     
        vertical_scroll_only=True,      
        enable_events = True,
        bind_return_key = False,
        pad = None,
        key='TablaAlumnos',
        right_click_menu = None,)],
        [sg.Button('Nuevo', key='nuevoAlumno', font=('Arial',12,'bold')), sg.Button('Modificar', key='modificarAlumno', font=('Arial',12,'bold')), sg.Button('Eliminar', key='eliminarAlumno', font=('Arial',12,'bold')),sg.Text(' '*51), sg.Button('Salir', key='SalirAlumnos', font=('Arial',12,'bold'))]],
    return sg.Window('Datos Alumnos', layout, finalize=True)

def crear_alumno():
    layout = [[sg.Text(key='titulo', size=(16,1), font=('Arial',12,'bold'))],
            [sg.Text('Apellido')],
            [sg.Input(key='apellido', size=(25,1))],
            [sg.Text('Nombre')],
            [sg.Input(key='nombre', size=(35,1))],
            [sg.Text('DNI')],
            [sg.Input(key='dni', size=(15,1))],
            [sg.Button('Aceptar', key='aceptarAlumno'),sg.Button('Cancelar', key='cancelarAlumno')]]
    return sg.Window('Alumno', layout, finalize=True)