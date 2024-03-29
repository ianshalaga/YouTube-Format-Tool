''' BIBLIOTECAS '''

import PySimpleGUI as psg
import os.path
import youtube_format as ytf
import json

''' DISEÑO '''

# Datos por defecto y elementos de menú desplegable
# mkvmerge_ruta = "C:/Archivos de programa/MKVToolNix/mkvmerge.exe"
mkvmerge_ruta = "C:/Program Files/MKVToolNix/mkvmerge.exe"
# pantallas_del_final_ruta = "E:/Grabaciones/Soulcalibur VI/Pantallas del final"
pantallas_del_final_ruta = "E:/SEYFER/GRABACIONES/SOULCALIBURVI/PANTALLAS DEL FINAL"
# videos_ruta = "E:/Grabaciones/Soulcalibur VI/Peleas"
videos_ruta = "E:\SEYFER\GRABACIONES\SOULCALIBURVI\PELEAS"
tipo = ["Online", "Offline"]
formato = ["casual", "ranked", "FT2", "FT3", "FT5", "FT10"]
plataforma = ["PS4", "PC"]

# Load json5
scvi_db_path = "scvi_db.json5"
with open(scvi_db_path, "r", encoding="utf8") as f:
    db_dict = json.load(f)

jugadores_lista = list()
personajes_lista = list()
for key, value in db_dict.items():
    if isinstance(value, dict):
        if value["type"] == "player":
            jugadores_lista.append(key)
        if value["type"] == "character":
            personajes_lista.append(key)

# jugadores_lista = [
#     "Bad Gato",
#     "DonMarlboro",
#     "estebangris",
#     "Edu Bushi",
#     "Skymathiana",
#     "Kovas",
#     "team ninja",
#     "Toshiaki",
#     "Karol",
#     "Rodol_Foffo",
#     "Fire red",
#     "ozkuervo",
#     "JaffarWolf",
#     "leospirandio",
#     "Nightwing_Ialmar",
#     "Ubitreides",
#     "Saiyajino",
#     "Adrianncr",
#     "RYUDO",
#     "SigFrancis",
#     "Camus",
#     "Junixart",
#     "zen-x",
#     "Eche",
#     "Gontranno",
#     "DemonioGarudaCL",
#     "raynarrok",
#     "Eddy_Beowulf",
#     "Maxxus",
#     "E1000",
#     "Lang_FFXIII",
#     "LN_Mastodon",
#     "SaimonChaild",
#     "Sonix-X",
#     "wylde",
#     "Estaries",
#     "Marv_995",
#     "Albhed_x",
#     "Seyfer",
#     "Sebas_ep90",
#     "KenkaOni",
#     "DuCaine",
#     "Kyoragecl"
# ]
jugadores_lista.sort()

# personajes_lista = [
#     "Taki",
#     "Talim",
#     "Setsuka",
#     "Hilde",
#     "2B",
#     "Azwel",
#     "Geralt",
#     "Groh",
#     "Haohmaru",
#     "Zasalamel",
#     "Tira",
#     "Amy",
#     "Cassandra",
#     "Hwang",
#     "Raphael",
#     "Xianghua",
#     "Astaroth",
#     "Ivy",
#     "Kilik",
#     "Maxi",
#     "Seong Mi-na",
#     "Sophitia",
#     "Yoshimitsu",
#     "Cervantes",
#     "Mitsurugi",
#     "Nightmare",
#     "Siegfried",
#     "Voldo"
# ]
personajes_lista.sort()

formulario = [
    [
        psg.Text("mkvmerge.exe ruta: ", size=(20,1)),
        psg.Input(default_text=mkvmerge_ruta, size=(50, 1), enable_events=True, key="MKVMERGE"),
        psg.FileBrowse()
    ],
    [
        psg.Text("Pantallas del final ruta: ", size=(20,1)),
        psg.Input(default_text=pantallas_del_final_ruta, size=(50, 1), enable_events=True, key="PANTALLAS_FINAL"),
        psg.FolderBrowse()
    ],
    [
        psg.Text("Videos directorio: ", size=(20,1)),
        psg.Input(default_text=videos_ruta, size=(50, 1), enable_events=True, key="VIDEOS"),
        psg.FolderBrowse()
    ],
    [
        psg.HSeparator()
    ],
    [
        psg.Text("Duración de las partes (en minutos): "),
        psg.Input(default_text="20", key="PASO", size=(10, 1), justification="center"),
        psg.Text("Plataforma: "),
        psg.Combo(values=plataforma, default_value=plataforma[0], key="PLATAFORMA")
    ],
    [
        psg.HSeparator()
    ],
    [
        psg.Text("Juego: "),
        psg.Input(justification="center", size=(14,1), default_text="Soul Calibur VI", enable_events=True, key="JUEGO"),
        psg.Text("Versión: "),
        psg.Input(justification="center", size=(14,1), default_text="2.31", enable_events=True, key="VERSION"),
        psg.Text("Tipo: "),
        psg.Combo(values=tipo, default_value=tipo[0], key="TIPO"),
        psg.Text("Formato: "),
        psg.Combo(values=formato, default_value=formato[0], key="FORMATO"),
    ],
    [
        psg.Text("Jugador 1: ", size=(20,1), justification="right"),
        psg.Combo(values=jugadores_lista, default_value=jugadores_lista[0], key="J1", size=(18, 1)),
        psg.Text("Personajes: ", size=(10,1), justification="right"),
        # psg.Input(size=(19, 1), enable_events=True, key="PJ1"),
        psg.Combo(values=personajes_lista, default_value=personajes_lista[0], key="PJ1", size=(18, 1)),
    ],
    [
        psg.Text("Jugador 2: ", size=(20,1), justification="right"),
        psg.Combo(values=jugadores_lista, default_value=jugadores_lista[0], key="J2", size=(18, 1)),
        psg.Text("Personajes: ", size=(10,1), justification="right"),
        # psg.Input(size=(19, 1), enable_events=True, key="PJ2"),
        psg.Combo(values=personajes_lista, default_value=personajes_lista[0], key="PJ2", size=(18, 1)),
    ],
    # [
    #     psg.HSeparator()
    # ],
    # [
    #     psg.Checkbox("Canales adicionales: ", enable_events=True, key="CA_CHK"),
    #     psg.Input(default_text="Soul Calibur Chile", size=(60, 1), enable_events=True, key="CA"),  
    # ],
    [
        psg.HSeparator()
    ],
    [
        psg.Button("Iniciar", key="INICIAR")
    ],
    [
        psg.Listbox(values=[], enable_events=True, size=(80, 15), key=("ARCHIVOS"))
    ],
    [
        psg.Output(size=(80, 15))
    ]
]

layout = [
    [
        psg.Column(formulario, justification="center")
    ]
]

# psg.theme("DarkAmber")
ventana = psg.Window("YouTube Format Tool", layout=layout, resizable=True, font="Helvetica")



''' LÓGICA '''

while True:
    event, values = ventana.read()
    ventana["ARCHIVOS"].update(os.listdir(values["VIDEOS"]))
    if event == "Exit" or event == psg.WIN_CLOSED:
        break
    # if values["CA_CHK"]:
    #     canales_adicionales = values["CA"].split(", ")
    # else:
    #     canales_adicionales = []
    if event == "INICIAR":
        ODatosNombre = ytf.datos_nombre(values["JUEGO"],
                                        values["VERSION"],
                                        values["TIPO"],
                                        values["FORMATO"],
                                        values["J1"],
                                        values["PJ1"],
                                        values["J2"],
                                        values["PJ2"],
                                        values["PLATAFORMA"]) #,
                                        # canales_adicionales)
        try:
            ytf.videos_por_parte(values["MKVMERGE"],
                                 values["VIDEOS"],
                                 int(values["PASO"]),
                                 ODatosNombre,
                                 values["PANTALLAS_FINAL"],
                                 scvi_db_path)
            ventana["ARCHIVOS"].update(os.listdir(values["VIDEOS"]))
        except:
            pass
    
