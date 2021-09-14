from random import *
import time
import os

def main():

    operadores_nomes = ["ADISSON", "AISLAN", "ALLAN", "ANDRÉ", "BRUNO DIAS", "BRUNO RODRIGUES", "CARLOS HENRIQUE", "CESAR", "DANIEL", "EVERTON", "FÁBIO", "GABRIEL", "ISAIAS", "JANISON", "JOÃO PAULO", "CRISTIAN", "RONALD", "LUCAS", "MACIEL", "MARCO ANTONIO", "NEILSON", "ORLEAN", "REGIVAN", "ROBSON", "RUBENS", "SAMUEL" , "SÉRGIO"]
    operadores_letra = ["5", "R", "H", "S", "D", "B", "M", "3", "4", "V", "F", "P", "L", "9", "T", "K", "Z", "8", "E", "C", "X", "1", "U", "O", "6", "A", "Q"]

    dias_do_mes = 0
    contador_dia = 0
    ultimo_operador_manha = ""
    ultimo_operador_tarde = ""
    ultimo_operador_noite = ""
    
    caminho_entrada = str(imput("Entre com um caminho: "))
    ler = open(caminho_entrada, 'r')
    conteudo_arquivo = ler.read()

    split = conteudo_arquivo.split("\n\n")

    dias_do_mes = split[0]
    ler_escala_manha = split[1]
    ler_escala_tarde = split[2]
    ler_escala_noite = split[3]

    escala_manha = ler_escala_manha.split("|") 
    escala_tarde = ler_escala_tarde.split("|")
    escala_noite = ler_escala_noite.split("|")

    caminho_saída = str(imput("Entre com um caminho: "))
    escala_dds = open(caminho_saída, 'w')

    while contador_dia != dias_do_mes:   

        os.system("cls")
        print("A escala do DDS está sendo Escrita.\nAguarde um momento.\n")
        print("ESCREVENDO\n")    
        time.sleep(1)
        os.system("cls")

        print("A escala do DDS está sendo Escrita.\nAguarde um momento.\n")
        print("ESCREVENDO.\n")
        time.sleep(1)    
        os.system("cls")

        print("A escala do DDS está sendo Escrita.\nAguarde um momento.\n")
        print("ESCREVENDO..\n")
        time.sleep(1)   
        os.system("cls")

        print("A escala do DDS está sendo Escrita.\nAguarde um momento.\n")
        print("ESCREVENDO...\n")    

        len_manha = len(escala_manha[contador_dia]) 
        len_tarde = len(escala_tarde[contador_dia]) 
        len_noite = len(escala_noite[contador_dia]) 
        
        apresentação = randrange(0,len_manha)

        if (apresentação != ultimo_operador_manha):
            #print ("Data: {}".format(contador_dia+1))
            escala_dds.write("Data: {}\n".format(contador_dia+1))
            lista1 = []
            for i in escala_manha[contador_dia]:
                lista1.append(i)
            if lista1[apresentação] in operadores_letra:
                b = operadores_letra.index(lista1[apresentação])
            #print("Operador da manhã: {}".format(operadores_nomes[b]))
            escala_dds.write("Operador da manhã: {}\n".format(operadores_nomes[b])) 
            ultimo_operador_manha = apresentação
            ok1 = 0

            while ok1 == 0:

                apresentação1 = randrange(0, len_tarde)

                if (apresentação1 != ultimo_operador_tarde):
                    lista1 = []
                    for i in escala_tarde[contador_dia]:
                        lista1.append(i)
                    if lista1[apresentação1] in operadores_letra:
                        b = operadores_letra.index(lista1[apresentação1])
                    #print("Operador da tarde: {}".format(operadores_nomes[b]))
                    escala_dds.write("Operador da tarde: {}\n".format(operadores_nomes[b])) 
                    ultimo_operador_tarde = apresentação1
                    ok1 = 1
                    ok2 = 0
            
            while ok2 == 0:

                apresentação2 = randrange(0, len_noite)

                if (apresentação2 != ultimo_operador_noite):
                    lista1 = []
                    for i in escala_noite[contador_dia]:
                        lista1.append(i)
                    if lista1[apresentação2] in operadores_letra:
                        b = operadores_letra.index(lista1[apresentação2])
                    #print("Operador da noite: {}".format(operadores_nomes[b]))
                    escala_dds.write("Operador da noite: {}\n\n".format(operadores_nomes[b])) 
                    ultimo_operador_noite = apresentação2
                    contador_dia = contador_dia + 1
                   #print("=======================================")
                    escala_dds.write("=======================================\n\n")
                    ok2 = 1

                else:
                    time.sleep(1)

            else:
                time.sleep(1)
        
        else:
            time.sleep(1)
    
    escala_dds.close()

main()

