import requests

def crear(act=False):
    id = None
    if not act:
        id = int(input('Ingrese el ID: '))
    nombre = input('Ingrese Nombre de la Mascota: ')
    telefono = input('Ingrese telefono: ')
    animal = int(input('Ingrese id de la Categoria (1=Perro, 2=Gato, 3=Conejo): '))
    return {'idMascota': id, 'nombre': nombre, 'telefonoDuenio': telefono, 'idAnimal': animal}

consulta = """Ingrese la accion que desea realizar\n 
            1: Todos los registros
            2: Crear Registro
            3: Buscar Registro
            4: Actualizar registro
            5: Eliminar Registro
            0: Salir\n"""

while True:
    opcion = int(input(consulta))
    if opcion == 0:
        break
    elif opcion == 1:
        response = requests.get('http://127.0.0.1:8000/api/lista')
        for i in response.json():
            print(i + '\n')
    elif opcion == 2:
        datos = crear()
        response = requests.post('http://127.0.0.1:8000/api/lista/', data=datos)
        if response.status_code != 201:
            print('Error en los datos, intenta con otro ID')
        else:
            print('Mascota creada!')
    elif opcion == 3:
        id = int(input('Ingrese el ID de la mascota que desea buscar: '))
        response = requests.get(f'http://127.0.0.1:8000/api/lista/{id}')
        if response.status_code == 404:
            print(f'No se encontró una mascota con el ID {id}')
        else:
            print(response.json())
    elif opcion == 4:
        id = int(input('Ingrese el ID de la mascota que desea actualizar: '))
        datos = crear(act=True)
        datos['idMascota'] = id
        response = requests.put(f'http://127.0.0.1:8000/api/lista/{id}', data=datos)
        if response.status_code != 200:
            print('Error al modificar los datos')
        else:
            print('Datos actualizados!')
    elif opcion == 5:
        id = int(input('Ingrese el ID de la mascota que desea eliminar: '))
        response = requests.delete(f'http://127.0.0.1:8000/api/lista/{id}')
        if response.status_code != 200:
            print('Mascota no encontrada')
        else:
            print('Mascota eliminada')
    else:
        print('Opcion Inválida')

        
