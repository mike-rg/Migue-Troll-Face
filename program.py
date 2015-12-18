"""
        Pequenio 'Troll Program'
"""

import sys
import argparse
import textwrap
import PIL
import string
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Defincion de posicion del texto en la imagen
TAMANIO_SANGRIA = 12
TAMANIO_RENGLON = 8
# Definicion de delimitadores
MAXLINEAS = 7
MAXCHARS_POR_LINEA = 24
MAXCHARS = 130
# Importar fuente
FSIZE = 10
FTYPE = "/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf"
FONT = ImageFont.truetype(FTYPE, FSIZE)
# Imagen por defecto
IFILE = "dice.png"


MJE_NONE_TEXTO = "Ingresa un texto ;)"


def dibujar_texto(string):
    if string is None:
        string = MJE_NONE_TEXTO
    linea = ""
    X = TAMANIO_SANGRIA
    Y = TAMANIO_RENGLON
    imagen = Image.open(IFILE)
    dibujar = ImageDraw.Draw(imagen)
    # Procesa el texto
    while len(string) > 0:
        t = string.partition(" ")
        if len(linea) + len(t[0]) >= MAXCHARS_POR_LINEA:
            dibujar.text((X, Y), linea, (0, 0, 0), font=FONT)
            Y = Y + TAMANIO_RENGLON
            linea = ""
        linea = linea + t[0] + " "
        string = t[2]
    # Dibuja la ultima linea menor a MAXCHARS_POR_LINEA
    dibujar.text((X, Y), linea, (0, 0, 0), font=FONT)
    dibujar = ImageDraw.Draw(imagen)
    imagen.save("escribido.png")


def _checkear_texto(string):
    if len(string) > MAXCHARS:
        mensaje = 'El texto supera la cantidad de caracteres aceptados.'
        raise argparse.ArgumentTypeError(mensaje)
    return string


def main():
    epilogmsj = '''
    Advertencias:
    -----------------------------------
    Se imprime solo el argumento 'hola'
    Para:
    ie. program.py -i hola

    Cantidad maxima de caracteres = 24

    '''
    epilog_format = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description='--- El migue dice ---',
                                     formatter_class= epilog_format,
                                     epilog=epilogmsj)
    parser.add_argument('-i', type=_checkear_texto,
                        help='''Texto de entrada.
                        ie. program.py -i "Hola mundo''')
    args = parser.parse_args()
    texto = args.i
    dibujar_texto(texto)
    sys.exit()

if __name__ == "__main__":
    main()
