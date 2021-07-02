''' BIBLIOTECAS '''

from pathlib import Path # Para administrar archivos y directorios
from moviepy.editor import VideoFileClip # Para extraer metadatos archivos de video
import math # Módulo matemático
import os # Opciones de sistema operativo
import shutil # Para mover archivos y directorios
import subprocess # Para ejecutar comandos de consola
import random # Manejo de aleatoriedad
# import cv2 # OpenCV 2.0, procesamiento de imágenes



''' FUNCIONES '''

# def extraer_fotogramas(ffmpeg_ruta,video_ruta,salida_ruta):
#     '''
#     Extrae todos los fotogramas de un video.
#     '''
#     subprocess.run([ffmpeg_ruta,
#                     "-loglevel", "quiet",
#                     "-i",
#                     video_ruta,
#                     os.path.join(salida_ruta,"fotograma" + "_imagen%04d_" + "1.jpg"),
#                     "-hide_banner"])


# def crear_dataset(imagenes_ruta, salida_ruta):
#     imagenes = Path(imagenes_ruta) # Imágenes en el directorio
#     print("Ruta de las imagenes: {}".format(imagenes)) # Ruta de las imagenes
#     c = 1
#     for imagen_ruta in imagenes.iterdir():
#         print(imagen_ruta)
#         imagen = cv2.imread(str(imagen_ruta),cv2.IMREAD_COLOR)
#         filas, columnas, _ = imagen.shape
#         imagen = cv2.resize(imagen,(int(columnas/6),int(filas/6)))
#         filas, _, _ = imagen.shape
#         imagen = imagen[:int(filas/4),:]
#         salida = os.path.join(salida_ruta,str(c)+"_1.jpg")
#         cv2.imwrite(salida,imagen)
#         c += 1


canales_dict = {
    "Soul Calibur Chile": ["https://www.youtube.com/channel/UCRmPkSnLwBG7mBg8L2tGLSw"],
    "SigFrancis": ["https://www.youtube.com/user/refran5"],
    "Camus": ["https://www.youtube.com/channel/UCCfUfXhGb4CWfcufUfo0nVQ", "https://www.youtube.com/channel/UC-SWYSSJDofVuMl-ch8T92A"],
    "Junixart": ["https://www.youtube.com/user/junixart"],
    "zen-x": ["https://www.twitch.tv/zenx_arg"],
    "Eche": ["https://www.youtube.com/channel/UCYOfh1vaybY-AgE5WCOgNfQ"],
    "Gontranno": ["https://www.youtube.com/channel/UCo3EZ-0WFtmAErr8f5KFY7w"],
    "DemonioGarudaCL": ["https://www.youtube.com/channel/UC-f5ATC1hxZJwxcSLVSxtsQ"],
    "raynarrok": ["https://www.youtube.com/user/lraynarrokl"],
    "Eddy_Beowulf": ["https://www.youtube.com/channel/UCVwZEdvYzonU_vFIfcKlXpQ"],
    "Maxxus": ["https://www.youtube.com/channel/UC5KGtnO8zi9B0SR5_xub60w"],
    "E1000": ["https://www.youtube.com/channel/UC-28NThOmlZ_06Te3QLJKtQ"],
    "Lang_FFXIII": ["https://www.youtube.com/channel/UCwqY50qCzN5bXuVtWyaaFbA"],
    "LN_Mastodon": ["https://www.youtube.com/channel/UCm7pucCgAFgKUFOhkfrMjMQ"],
    "SaimonChaild": ["https://www.twitch.tv/saimonchaild_"],
    "Sonic-X": ["https://www.youtube.com/c/SonicX"],
    "Sebas_ep90": ["https://www.youtube.com/channel/UC7S9cOu9ob384mkuscDhsFw"],
    "Albhed_x": ["https://www.youtube.com/channel/UCFrFKjy5e2XVomZx-ohyC2Q"],
    "wylde": ["https://www.youtube.com/user/guitardevilf5/featured"],
    "Kyoragecl": ["https://www.youtube.com/user/unrealassasin"]
}


listas_reproduccion_dict = {
    "Adrianncr": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7zOm81n6T_fUa5aNyuHJ0v",
    "RYUDO": "https://www.youtube.com/playlist?list=PL90QAKwVH1t74Qzm4wlx604Ffw1hbHY6x",
    "SigFrancis": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6fRaOJPS84khrnPhlKodB7",
    "Kyoragecl": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4wszcCcv3sVPWv5kGHOW5y",
    "LN_Mastodon": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5WtjO5OrpAs9VeRC3LPCyj",
    "DuCaine": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5ne2e6POOCmL43DogtrDzo",
    "Eddy_Beowulf": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6libDfzT5ZgnCKty20jPki",
    "SaimonChaild": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6BIHUbhWoiImcYZbeQYFzW",
    "Sebas_ep90": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5cCPrXbS3vyIIHSP5ssLzE",
    "Gontranno": "https://www.youtube.com/playlist?list=PL90QAKwVH1t78dk4jj6x51dJa_oEFQJJu",
    "E1000": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5OrZV2eQgXC2S2OslYIoNK",
    "wylde": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6EGhT85l7I_dyhcr8kScjl",
    "Estaries": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5vdm87xTohCp1mYcr0RXBb",
    "Marv_995": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7tqJ9tdKQ377j_PGNwTKb9",
    "zen-x": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5iVwDcfNHJ30ORntTWE_Mt",
    "Albhed_x": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6tHpF3Q1Q1JQAGO-re1e-X",
    "Taki": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7W3yhPMKyU9uje26G1ZnBu",
    "Talim": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7R1-ibZfefU2wUDRAIa3G2",
    "Setsuka": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6GsZ9sHFdkhLJ4MdSEOrwF",
    "Hilde": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5CnUs7a5OfQAQsL_VQdAF4",
    "2B": "https://www.youtube.com/playlist?list=PL90QAKwVH1t60fEU20FYYg20Tp1Y5FBGQ",
    "Azwel": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6q-TlxlQSVO-F1WLcSLT03",
    "Geralt": "https://www.youtube.com/playlist?list=PL90QAKwVH1t78v9zPaxD-M2WS5W8Shdf9",
    "Groh": "https://www.youtube.com/playlist?list=PL90QAKwVH1t75-dwernEnAEWlSX73fzex",
    "Haohmaru": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4IvEvmhRHEfz-xEzMaoLiR",
    "Zasalamel": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6a2rA51DIX72J95BqTnsbh",
    "Tira": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4dqovymm_ftxh69-vXOG0e",
    "Amy": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7QvwDN2c4jbLq0hhqVlOFq",
    "Cassandra": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5anV4BL93UxrqYBAGNOgI2",
    "Hwang": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5Y9hflTAH8dVYLeOr10jHR",
    "Raphael": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4vGjaOfK800WFGyx6EbCG1",
    "Xianghua": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6LjfBNjGih8rH6pGcW1rg-",
    "Astaroth": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4YdujqkS3PCw8HoaqC7p40",
    "Ivy": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6jL0gEFDhFF8ypHtpU3ZQJ",
    "Kilik": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4lDq3Ko9-yw4ipOzALlRf5",
    "Maxi": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5HBO3pV8il2FFtRNcHLGEg",
    "Seong Mi-na": "https://www.youtube.com/playlist?list=PL90QAKwVH1t6faZQFTW_-d883_az5An5g",
    "Sophitia": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7_Yf0QJUfGVpErfaQ7u_bV",
    "Yoshimitsu": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7mTyKaL4pb_hzKvI6WHLgw",
    "Cervantes": "https://www.youtube.com/playlist?list=PL90QAKwVH1t7q1b8iijnrYmaYuI27Gfyo",
    "Mitsurugi": "https://www.youtube.com/playlist?list=PL90QAKwVH1t64CN2gW3GZYr6OiKOGRsWQ",
    "Nightmare": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5lPgdyLfAac9Msc77gqGjZ",
    "Siegfried": "https://www.youtube.com/playlist?list=PL90QAKwVH1t49YI80I9PtNerAjAklbWXf",
    "Voldo": "https://www.youtube.com/playlist?list=PL90QAKwVH1t4JEKK40NPSAIXIO8Bh5Mu-",
    "Duelos": "https://www.youtube.com/playlist?list=PL90QAKwVH1t5g2Pirxvs9YFm7blxYyvhl",
    "Ranked": "https://www.youtube.com/playlist?list=PL90QAKwVH1t79_xIVc3WnFp8QCk8a7d3N"
}


def lista_sumar_elementos(lista):
    '''
    Suma los elementos de una lista de números
    '''
    suma = 0
    for e in lista:
        suma += e
    return suma


def segundos_to_hhmmss(tiempo_segundos):
    '''
    Convierte un número en formato segundos (236.37 por ejemplo) a un string con el formato HH:MM:SS
    '''
    tiempo_total_horas = tiempo_segundos/3600
    tiempo_horas = int(tiempo_total_horas)
    tiempo_total_minutos = abs(tiempo_total_horas-tiempo_horas)*60
    tiempo_minutos = int(tiempo_total_minutos)
    tiempo_total_segundos = int(abs(tiempo_total_minutos-tiempo_minutos)*60)
    horas = str("%02d" % tiempo_horas)
    minutos = str("%02d" % tiempo_minutos)
    segundos = str("%02d" % tiempo_total_segundos)
    tiempo = horas + ":" + minutos + ":" + segundos
    return tiempo


def generar_marcas_de_tiempo(archivo_abierto, lista_resultado_duraciones, pos_lista):
    '''
    Genera las marcas de tiempo de un video de YouTube.
    '''
    marca_tiempo = "00:00:00"
    marca_nombre = "Pelea "    
    archivo_abierto.write("Marcas de tiempo:\n")
    cadena = marca_tiempo + " " + marca_nombre + "1" + "\n"
    archivo_abierto.write(cadena)
    lista_duraciones = lista_resultado_duraciones[pos_lista[0]]
    tiempo_acumulado = 0
    for indice_tiempo in enumerate(lista_duraciones):
        tiempo_acumulado += indice_tiempo[1]
        if indice_tiempo[0]+1 == len(lista_duraciones): # Si es el último elemento
            cadena = segundos_to_hhmmss(tiempo_acumulado) + " Pantallas del final"
            archivo_abierto.write(cadena)
        else:
            cadena = segundos_to_hhmmss(tiempo_acumulado) + " " + marca_nombre + str(indice_tiempo[0]+2) + "\n"
            archivo_abierto.write(cadena)


def obtener_canales(archivo_abierto, canales_dict, rival_nombre, canales_adicionales):
    '''
    Agrega al archivo de descripción los enlaces a los canales de YouTube pertinentes,
    estos son, los del jugador rival más algunos adicionales en caso de haber.
    '''
    if rival_nombre in canales_dict.keys():
        archivo_abierto.write("\nCanales:\n")
        canal_url_lista = canales_dict[rival_nombre]
        canal_descripcion = rival_nombre + ": " + " ".join(canal_url_lista) + "\n"
        archivo_abierto.write(canal_descripcion)
        if canales_adicionales != []:
            for canal in canales_adicionales:
                canal_descripcion = canal + ": " + canales_dict[canal][0]
                archivo_abierto.write(canal_descripcion)
                archivo_abierto.write("\n")
    elif canales_adicionales != []:
        archivo_abierto.write("\nCanales:\n")
        for canal in canales_adicionales:
                canal_descripcion = canal + ": " + canales_dict[canal][0]
                archivo_abierto.write(canal_descripcion)
                archivo_abierto.write("\n")
    
def obtener_listas_de_reproduccion(archivo_abierto, reproduccion_lista, listas_reproduccion_dict, juego_nombre):
    '''
    Agrega al archivo de descripción los enlaces a las listas de reproducción de YouTube pertinentes,
    estas son, la del jugador rival (en caso de existir) y las de los personajes que aparecen en los combates.
    '''
    archivo_abierto.write("Listas de reproducción:\n")
    for lista in reproduccion_lista:
        if lista in listas_reproduccion_dict.keys():
            texto = juego_nombre + " - Combates - " + lista + ": " + listas_reproduccion_dict[lista] + "\n"
            archivo_abierto.write(texto)


def texto_adicional(archivo_abierto):
    '''
    Texto adicional para añadir al final de la descripción del video de YouTube.
    '''
    texto_lista = ["Soul Calibur VI desde 0: https://www.youtube.com/playlist?list=PL90QAKwVH1t4GEDI3Ym8JeL88AyJKcu5S",
                "Soul Calibur VI (2.31) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t5-BK_yFrn6UDBXQQYoaOL7",
                "Soul Calibur VI (2.30) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t5CsrL_ilDpyprz6UwaKLC5",
                "Soul Calibur VI (2.25.01) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t7XcfURbvuIGUXif3zApMQb",
                "Soul Calibur VI (2.25.01) - Combates offline: https://www.youtube.com/playlist?list=PL90QAKwVH1t5Gee5X7k9my0CvdIgajlMb",
                "Soul Calibur VI (2.25) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t7CxstJnE5h68OA-mpGWb-5",
                "Soul Calibur VI (2.21) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t4JWONGVerwdu6GWs6kUowB",
                "Soul Calibur VI (2.12) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t4XUXIaIzrm5tv_OAonfyU9",
                "Soul Calibur VI (2.10.01) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t6MKVd2hJJ-CzBFYykjK_zx",
                "Soul Calibur VI (2.05) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t7L6mlmtX4dArS5V2cGWYtR",
                "Soul Calibur VI (2.02) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t6YwKhGeCki9ONi4eRIpA8f",
                "Soul Calibur VI (2.01) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t6BabI6xP4IIkBPM0pI9OWC",
                "Soul Calibur VI (S1) - Combates offline: https://www.youtube.com/playlist?list=PL90QAKwVH1t5d1ZrcDC7sOssxuvh2opx3",
                "Soul Calibur VI (S1) - Combates online: https://www.youtube.com/playlist?list=PL90QAKwVH1t6g09h8t4dEmNKLL5BtnENW",
                "Soul Calibur III: https://www.youtube.com/playlist?list=PL90QAKwVH1t6vuanXTfU2s6kzO0rNq6Le",
                "Soul Calibur IV: https://www.youtube.com/playlist?list=PL90QAKwVH1t4Ps9-pU3qGUc8wkGpmSgqH",
                "Soul Calibur V: https://www.youtube.com/playlist?list=PL90QAKwVH1t66BTTz0UDi3nTF8ro6BAJa",
                "Soul Calibur - The Legend Will Never Die: https://www.youtube.com/playlist?list=PL90QAKwVH1t6RJZLrQW8aGjbhQFgrA8O4",
                "Soul Calibur VI: https://www.youtube.com/playlist?list=PL90QAKwVH1t7TUmdcc1oGOOWm6a1pQCrG",
                "Soul Calibur VI - Historias: https://www.youtube.com/playlist?list=PL90QAKwVH1t7keR4IGG5vJG9mnvbgAM4N"
    ]
    archivo_abierto.write("\n".join(texto_lista))


def generar_descripcion(nombre_salida_marcas_tiempo,
                        nombre_descripcion,
                        lista_resultado_duraciones,
                        pos_lista,
                        rival_nombre,
                        canales_adicionales,
                        reproduccion_lista,
                        juego_nombre,
                        etiquetas):
    '''
    Devulve la descripción para el video de YouTube.
    Formato:
        * Nombre del video
        * Etiquetas
        * Marcas de tiempos
        * Canales
        * Listas de reproducción
        * Texto adicional
    '''
    with open(nombre_salida_marcas_tiempo, 'w', encoding="utf8") as archivo:
        archivo.write(nombre_descripcion)
        archivo.write("\n")
        archivo.write(etiquetas)
        archivo.write("\n")
        generar_marcas_de_tiempo(archivo, lista_resultado_duraciones, pos_lista)
        archivo.write("\n")
        obtener_canales(archivo, canales_dict, rival_nombre, canales_adicionales)
        archivo.write("\n")
        obtener_listas_de_reproduccion(archivo, reproduccion_lista, listas_reproduccion_dict, juego_nombre)
        archivo.write("\n")
        texto_adicional(archivo)


def seleccionar_pantalla_final(pantallas_final_ruta, plataforma):
    '''
    Selecciona un video de pantalla final de manera aleatoria en base a la plataforma
    en la que se llevaron a cabo los combates.
    '''
    pantallas_final = Path(os.path.join(pantallas_final_ruta,plataforma))
    pantallas_final_rutas_lista = list()
    for archivo in pantallas_final.iterdir():
        pantallas_final_rutas_lista.append(archivo)
    return random.choice(pantallas_final_rutas_lista)


def videos_por_parte(mkvmerge_ruta, # Ruta donde se aloja mkvmerge.exe
                    videos_ruta, # Ruta de los videos a procesar
                    duracion_maxima_por_video, # Debe estar dada en minutos
                    ODatosNombre, # Lista de strings para dar formato al nombre del archivo
                    pantallas_final_ruta):
    '''
    Toma una lista de videos de un directorio y los separa/mueve en subdirectorios
    en base a la duración pasada por parámetro. Luego los une con mkvmerge y finalmente los renombra.
    Además se generan archivos de texto con las marcas de tiempo para colocar en YouTube.
    '''

    archivos = Path(videos_ruta) # Archivos en el directorio
    print("Ruta de los videos: {}".format(archivos)) # Ruta de los videos pasada como parámetro
    duracion_maxima_por_video = duracion_maxima_por_video*60 # Conversión de minutos a segundos

    # Cantidad de videos en el directorio
    videos_cantidad = 0
    for _ in archivos.iterdir():
        videos_cantidad += 1

    # Se calcula la duración total de todos los videos en el directorio
    duracion_total = 0
    # Los elementos de las siguientes listas se corresponden
    videos_duracion_lista = list() # Lista de las duraciones de los videos en el directorio
    videos_nombres_lista = list() # Lista de nombres de los videos en el directorio
    for i,archivo in enumerate(archivos.iterdir()):
        nombre = archivo.name # Nombre del archivo
        print("Procesando el archivo: {} | ({}/{})".format(nombre,i+1,videos_cantidad)) # Progreso mostrado en pantalla
        video = VideoFileClip(str(archivo)) # Apertura de un archivo de video con moviepy
        duracion = video.duration # Extracción de la duración del video
        video.close() # Cierre del archivo de video
        duracion_total += duracion
        videos_duracion_lista.append(duracion)
        videos_nombres_lista.append(archivo)

    # Cálculo de la duración por video teniendo en cuenta duracion_maxima_por_video
    cantidad_videos = math.ceil(duracion_total/duracion_maxima_por_video)
    duracion_por_video = duracion_total/cantidad_videos

    # Se crea una lista_resultado con tantas listas (partes) como archivos resultantes habrá.
    # Cada una de ellas (partes) contienen los nombres de los archivos correspondientes a cada parte.
    # La lista_resultado_duraciones es el equivalente a lista_resultado pero conteniendo las duraciones
    lista_duracion = list()
    lista_nombre = list()
    lista_resultado = list()
    lista_resultado_duraciones = list()
    for i in enumerate(videos_nombres_lista): # o bien enumerate(videos_duracion_lista)
        lista_nombre.append(videos_nombres_lista[i[0]])
        lista_duracion.append(videos_duracion_lista[i[0]])
        duracion_acumulada = lista_sumar_elementos(lista_duracion)
        if duracion_acumulada > duracion_por_video:
            dif1 = abs(duracion_acumulada-duracion_por_video)
            dif2 = abs(lista_sumar_elementos(lista_duracion[:-1])-duracion_por_video)
            if dif1 > dif2:
                lista_resultado.append(lista_nombre[:-1])
                lista_resultado_duraciones.append(lista_duracion[:-1])
                lista_nombre = [lista_nombre[-1]]
                lista_duracion = [lista_duracion[-1]]
            else:
                lista_resultado.append(lista_nombre)
                lista_resultado_duraciones.append(lista_duracion)
                lista_nombre = list()
                lista_duracion = list()
    if lista_nombre != []:
        if len(lista_nombre) > 1:
            lista_resultado.append(lista_nombre)
            lista_resultado_duraciones.append(lista_duracion)
        else:
            lista_resultado[-1].append(lista_nombre[0])
            lista_resultado_duraciones[-1].append(lista_duracion[0])
    
    # Se muestra cómo quedaron conformadas las partes
    for i in enumerate(lista_resultado):
        print("Archivos para la parte {}:".format(i[0]+1))
        for e in i[1]:
            print(e)
        print("\n")

    # Se crean los directorios de las partes y se mueven los archivos correspondientes
    for pos_lista in enumerate(lista_resultado):
        p = Path(os.path.join(archivos,str(pos_lista[0]+1)))
        p.mkdir()
        print("Creado el directorio: {}".format(p))
        videos_union_lista = list() # Lista de videos a unir con mkvmerge
        for ruta_origen in pos_lista[1]:
            ruta_destino = Path(os.path.join(p,os.path.split(ruta_origen)[-1]))
            videos_union_lista.append(ruta_destino)
            print("Copiando el archivo: {}".format(ruta_destino))
            shutil.move(ruta_origen,ruta_destino)
        
        # Formato del nombre de salida en base a datos_nombre
        nombre_salida = str(p) + "/" + ODatosNombre.generar_nombre() + str(pos_lista[0]+1) + "-" + str(len(lista_resultado)) + ").mkv"
        nombre_salida_marcas_tiempo = str(p) + "/" + ODatosNombre.generar_nombre() + str(pos_lista[0]+1) + "-" + str(len(lista_resultado)) + ").txt"
        nombre_descripcion = ODatosNombre.generar_nombre() + str(pos_lista[0]+1) + "/" + str(len(lista_resultado)) + ")"

        # Archivo de descripción del video
        if ODatosNombre.jugador1_nombre == "Seyfer": # El rival es aquel que no soy yo
            rival_nombre = ODatosNombre.jugador2_nombre
        else:
            rival_nombre = ODatosNombre.jugador1_nombre
        if ODatosNombre.combate_formato.startswith("FT"):
            formato = "Duelos"
        elif ODatosNombre.combate_formato == "ranked":
            formato = "Ranked"
        else:
            formato = "Casual"
        personajes_listas_reproduccion = list(set(ODatosNombre.jugador1_personajes.split(", ") + ODatosNombre.jugador2_personajes.split(", "))) # Se eliminan personajes repetidos
        reproduccion_lista = [rival_nombre] + personajes_listas_reproduccion + [formato]
        generar_descripcion(nombre_salida_marcas_tiempo,
                            nombre_descripcion,
                            lista_resultado_duraciones,
                            pos_lista,
                            rival_nombre,
                            ODatosNombre.canales_adicionales,
                            reproduccion_lista,
                            ODatosNombre.juego_nombre,
                            ODatosNombre.generar_etiquetas())

        # Sintaxis para mkvmerge
        mkvmerge_lista = [mkvmerge_ruta,
                          "-o",
                          nombre_salida,
                          str(videos_union_lista[0])
                         ]
        pantalla_final_ruta = seleccionar_pantalla_final(pantallas_final_ruta,ODatosNombre.plataforma)
        for i in range(1,len(videos_union_lista),1):
            mkvmerge_lista.append("+")
            mkvmerge_lista.append(str(videos_union_lista[i]))
        mkvmerge_lista.append("+")
        mkvmerge_lista.append(str(pantalla_final_ruta))

        subprocess.run(mkvmerge_lista) # Unión de archivos con mkvmerge

        # Se mueven los resultados de las uniones al directorio base y se eliminan las carpetas
        shutil.move(nombre_salida,archivos)
        shutil.move(nombre_salida_marcas_tiempo,archivos)
        shutil.rmtree(p)


class datos_nombre: # Datos para nombrar los videos de las peleas
    def __init__(self, # Referencia a la instancia actual
                juego_nombre, # Soul Calibur VI
                juego_version, # 2.31
                combate_tipo, # Online / Offline
                combate_formato, # casual, ranked, FT
                jugador1_nombre,
                jugador1_personajes,
                jugador2_nombre,
                jugador2_personajes,
                plataforma, # PC, PS4
                canales_adicionales):
        self.juego_nombre = juego_nombre
        self.juego_version = juego_version
        self.combate_tipo = combate_tipo
        self.combate_formato = combate_formato
        self.jugador1_nombre = jugador1_nombre
        self.jugador2_nombre = jugador2_nombre
        self.jugador1_personajes = jugador1_personajes
        self.jugador2_personajes = jugador2_personajes
        self.plataforma = plataforma
        self.canales_adicionales = canales_adicionales
    
    def generar_nombre(self):
        return self.juego_nombre + " (" + self.juego_version + ") - " + self.combate_tipo + " " + self.combate_formato + " - " + self.jugador1_nombre + " (" + self.jugador1_personajes + ") VS " + self.jugador2_nombre + " (" + self.jugador2_personajes + ") ("
    
    def generar_etiquetas(self):
        return self.juego_nombre + ", " + self.juego_version + ", " + self.combate_tipo + ", " + self.combate_formato + ", " + self.jugador1_nombre + ", " + self.jugador1_personajes + ", " + self.jugador2_nombre + ", " + self.jugador2_personajes



''' EJECUCIÓN '''

# mkvmerge_ruta = "C:/Program Files/MKVToolNix/mkvmerge.exe"
# pantallas_final_ruta = "E:/Grabaciones/Soulcalibur VI/Pantallas del final"
# ruta = r"E:\Grabaciones\Soulcalibur VI\Peleas\1 E1000\2 Azwel"
# paso = 20 # En minutos. Tiempo máximo por parte.
# ODatosNombre = datos_nombre("Soul Calibur VI",
#                             "2.31",
#                             "Online",
#                             "casual",
#                             "Seyfer",
#                             "Talim",
#                             "E1000",
#                             "Azwel",
#                             "PS4",
#                             [])

# canales_adicionales = ["Soul Calibur Chile"]
# ODatosNombre.canales_adicionales = canales_adicionales

# videos_por_parte(mkvmerge_ruta,ruta,paso,ODatosNombre,pantallas_final_ruta)



''' Pendientes '''
# Hacer un modelo neuronal que corte las peleas solo

# ffmpeg_ruta = "E:/Instaladores/Multimedia/Video/ffmpeg.exe"

# extraer_fotogramas(ffmpeg_ruta,video_ruta,salida_ruta)

# imagenes_ruta = "E:/Grabaciones/Soul Calibur VI/Nueva carpeta/1"
# salida_ruta = "E:/Grabaciones/Soul Calibur VI/Nueva carpeta/1_2"

# crear_dataset(imagenes_ruta, salida_ruta)