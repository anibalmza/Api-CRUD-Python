import PySimpleGUI as sg
from make_windows import *
from personas import *
persona = Personas()

def main():
    def desactivarBotonesMenu(estado):
        win_menu['Alumnos'].update(disabled=estado)
        win_menu['Salir'].update(disabled=estado)

    def desactivarBotonesAlumno(estado):
        win_tablaAlumnos['nuevoAlumno'].update(disabled=estado)
        win_tablaAlumnos['modificarAlumno'].update(disabled=estado)
        win_tablaAlumnos['eliminarAlumno'].update(disabled=estado)
        win_tablaAlumnos['SalirAlumnos'].update(disabled=estado)
    
    def desactivarCamposAlumno():
        win_alumno['apellido'].update(disabled=True)
        win_alumno['nombre'].update(disabled=True)
        win_alumno['dni'].update(disabled=True)

    def cargarDatosAlumno():
        datosTabla = win_tablaAlumnos['TablaAlumnos'].get()
        id = datosTabla[seleccion[0]][0]
        apellido = datosTabla[seleccion[0]][1]
        nombre = datosTabla[seleccion[0]][2]
        dni = datosTabla[seleccion[0]][3]
        win_alumno['apellido'].update(apellido)
        win_alumno['nombre'].update(nombre)
        win_alumno['dni'].update(dni)
        return id

    #############  Menu  #############
    win_menu = crear_menu()    
    while True:
        window, event, values = sg.read_all_windows()        
        # print(event, values)
        if event == 'Salir':
            break

        #############  Alumno  #############
        elif event == 'Alumnos':
            desactivarBotonesMenu(True)
            win_tablaAlumnos = crear_tabla_alumnos()            
            datos = persona.consulta_personas()
            win_tablaAlumnos['TablaAlumnos'].update(values=datos)
            win_tablaAlumnos.move(win_menu.current_location()[0] + 100, win_menu.current_location()[1] + 100)
            
        elif event == 'SalirAlumnos':
            desactivarBotonesMenu(False)
            win_tablaAlumnos.close()

        #############  Nuevo Alumno  #############
        elif event == 'nuevoAlumno':
            eventAnterior = event
            desactivarBotonesAlumno(True)
            win_alumno = crear_alumno()
            win_alumno['titulo'].update('Nuevo Alumno')
            win_alumno.move(win_tablaAlumnos.current_location()[0] + 100, win_tablaAlumnos.current_location()[1] + 100)

        #############  Modificar Alumno  #############
        elif event == 'modificarAlumno':
            eventAnterior = event
            seleccion = values['TablaAlumnos']
            if seleccion == []:
                sg.popup_auto_close('Debe seleccionar un Alumno', title = '<< Error >>', font=('Arial',12,'bold'))
            else:
                win_alumno = crear_alumno()
                win_alumno['titulo'].update('Modificar Alumno')
                id = cargarDatosAlumno()
                
        elif event == 'eliminarAlumno':
            eventAnterior = event
            seleccion = values['TablaAlumnos']
            if seleccion == []:
                sg.popup_auto_close('Debe seleccionar un Alumno', title = '<< Error >>', font=('Arial',12,'bold'))
            else:                
                win_alumno = crear_alumno()
                win_alumno['titulo'].update('Eliminar Alumno')
                id = cargarDatosAlumno()
                desactivarCamposAlumno()
        
        elif event == 'aceptarAlumno':
            if eventAnterior == 'nuevoAlumno':
                persona.inserta_persona(values['apellido'].upper(), values['nombre'].upper(), values['dni'].upper())
            elif eventAnterior == 'modificarAlumno':
                persona.modifica_persona(id, values['apellido'].upper(), values['nombre'].upper(), values['dni'].upper())
            elif eventAnterior == 'eliminarAlumno':
                persona.elimina_persona(id)

            datos = persona.consulta_personas()
            win_tablaAlumnos['TablaAlumnos'].update(values=datos)
            desactivarBotonesAlumno(False)
            win_alumno.close()

        elif event == 'cancelarAlumno':
            desactivarBotonesAlumno(False)
            win_alumno.close()

        elif event == 'Pagos':
            pass

    window.close()

if __name__ == '__main__':
    main()