import sys
from PIL import Image
import numpy as np

#1
def valido(tam):
    try:
        tam = tam.split(',')
        if len(tam) == 2:
            if tam[0] == "x":
                return isinstance(int(tam[1]), int)
            elif tam[1] == "x":
                return isinstance(int(tam[0]), int)
            else:
                return (int(tam[1]) and int(tam[0]))
        else:
            return False
    except Exception:
        return False

def tratador(tam):
    tam = tam.split(',')
    if tam[0] == "x":
        return [0,int(tam[1])]
    elif tam[1] == "x":
        return [int(tam[0]),0]
    else:
        return [int(tam[0]), int(tam[1])]

def seleciona_tipo():
    ###################
    # LISTAS DE CORES #
    ###################

    cores_gratuitas = [
        (0, 0, 0),
        (60, 60, 60),
        (120, 120, 120),
        (210, 210, 210),
        (255, 255, 255),
        (96, 0, 24),
        (237, 28, 36),
        (255, 127, 39),
        (246, 170, 9),
        (249, 221, 59),
        (255, 250, 188),
        (14, 185, 104),
        (19, 230, 123),
        (135, 255, 94),
        (12, 129, 110),
        (16, 174, 166),
        (19, 225, 190),
        (96, 247, 242),
        (40, 80, 158),
        (64, 147, 228),
        (77, 49, 184),
        (107, 80, 246),
        (153, 177, 251),
        (74, 66, 132),
        (120, 12, 153),
        (170, 56, 185),
        (224, 159, 249),
        (203, 0, 122),
        (236, 31, 128),
        (243, 141, 169),
        (104, 70, 52),
        (149, 104, 42),
        (248, 178, 119)
    ]
    cores_pagas = [
        (170, 170, 170),
        (165, 14, 30),
        (250, 128, 114),
        (228, 92, 26),
        (156, 132, 49),
        (197, 173, 49),
        (232, 212, 95),
        (15, 121, 159),
        (74, 107, 58),
        (90, 148, 74),
        (132, 197, 115),
        (187, 250, 242),
        (125, 199, 255),
        (122, 113, 196),
        (181, 174, 241),
        (155, 82, 73),
        (209, 128, 120),
        (250, 182, 164),
        (219, 164, 99),
        (123, 99, 82),
        (156, 132, 107),
        (214, 181, 148),
        (209, 128, 81),
        (255, 197, 165),
        (109, 100, 63),
        (148, 140, 107),
        (205, 197, 158),
        (51, 57, 65),
        (109, 117, 141),
        (179, 185, 209)
    ]
    cores = cores_gratuitas + cores_pagas
    preto_e_branco = [
        (0, 0, 0),
        (60, 60, 60),
        (120, 120, 120),
        (170, 170, 170),
        (210, 210, 210),
        (255, 255, 255),
    ]
    print('\nQual tipo de pixelart você deseja?')
    print('\n[1] mantem todas as cores')
    print('[2] WPlace cores gratuitas')
    print('[3] WPlace todas as cores')
    print('[4] WPlace preto e branco')

    while(1):
        tipo = input("\nOpção: ")
        if tipo == '1':
            return []
        elif tipo == '2':
            return cores_gratuitas
        elif tipo == '3':
            return cores
        elif tipo == '4':
            return preto_e_branco
        else:
            print('Selecione uma opção válida')

def replace_color(rgb, tipo):
    rgb = np.array(rgb)
    cor_mais_proxima = (0,0,0)
    menor_dist = np.linalg.norm(rgb - np.array([0,0,0]))
    for i in tipo:
        dist = np.linalg.norm(rgb - np.array(i))
        if dist < menor_dist:
            cor_mais_proxima = i
            menor_dist = dist
    return cor_mais_proxima
                
def main(name):
    img = Image.open(name)
    print("PixelArt Genererator v0.1\n")
    print("Qual o tamanho você deseja para sua pixelart?")
    print("Use numeros naturais separados por vírgula para largura e altura, use x em um deles para manter proporção segundo o outro (recomendável)")
    print("Ex: x,30 gera uma pixelart com 30 de altura e largura proporcional\n")
    while(1):
        tam = input("")
        if not valido(tam):
            print("Formato inválido, tente novamente")
        else:
            tam = tratador(tam)
            break
    if 0 in tam:
        w,h = img.size
        if tam[0] == 0:
            fator = tam[1]/h
            tam[0] = round(w*fator)
        else:
            fator = tam[0]/w
            tam[1] = round(h*fator)

    resized = img.resize(tam)
    
    tipo = seleciona_tipo()
    
    if tipo:
        pixels = resized.load()
        for y in range(resized.height):
            for x in range(resized.width): 
                pixels[x, y] = replace_color(pixels[x, y], tipo)

    ind = name.find('.')
    resized.save(name[:ind] + "_pixelart" + name[ind:])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(input("Qual o nome da imagem? "))
    else:
        main(sys.argv[1])