def cargar_archivos(filename):
    archivo = open(filename, 'r', encoding='utf-8')
    registro = {}
    archivo.readline() #saltear primera linea

    for linea in archivo:
        datos = linea.strip('\n').split(',')
        registro[datos[0]] = datos[1:]

    archivo.close()
    return registro


def guardar_cambios(registro_viejo, filename):
    archivo = open(filename, 'w', encoding='utf-8')
    archivo.write("id,fecha,año,latitud,longitud\n")
    for id_viejo, datos in registro_viejo.items():
        fecha = datos[0]
        año = datos[1]
        latitud = datos[2]
        longitud = datos[3]
        archivo.write(f"{id_viejo},{fecha},{año},{latitud},{longitud}\n")
    archivo.close()


def main():
    registro_viejo = cargar_archivos('data.csv')
    registro_nuevo = cargar_archivos('nuevo.csv')
    for id_nuevo in registro_nuevo:
        datos_nuevo = registro_nuevo[id_nuevo]
        if id_nuevo in registro_viejo:
            if registro_viejo[id_nuevo][2] != datos_nuevo[2] or registro_viejo[id_nuevo][3] != datos_nuevo[3]:
                registro_viejo[id_nuevo] = datos_nuevo
        else:
            registro_viejo[id_nuevo] = datos_nuevo
    guardar_cambios(registro_viejo,'data.csv')

if __name__ == '__main__':
    main()