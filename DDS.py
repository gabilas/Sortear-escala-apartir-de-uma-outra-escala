from random import *
import time

def main():

    operadores_nomes = ["ADISSON", "AISLAN", "ALLAN", "ANDRÉ", "BRUNO DIAS", "BRUNO RODRIGUES", "CARLOS HENRIQUE", "CESAR", "DANIEL", "EVERTON", "FÁBIO", "GABRIEL", "ISAIAS", "JANISON", "JOÃO PAULO", "CRISTIAN", "RONALD", "LUCAS", "MACIEL", "MARCO ANTONIO", "NEILSON", "ORLEAN", "REGIVAN", "ROBSON", "RUBENS", "SAMUEL" , "SÉRGIO"]
    operadores_letra = ["5", "R", "H", "S", "D", "B", "M", "3", "4", "V", "F", "P", "L", "9", "T", "K", "Z", "8", "E", "C", "X", "1", "U", "O", "6", "A", "Q"]
    
    n_deoperadores = len(operadores_letra)

    dias_do_mes = 0
    contador_dia = 0
    ultimo_operador_manha = ""
    ultimo_operador_tarde = ""
    ultimo_operador_noite = ""

    ##caminho_entrada = input(str("Entre com um caminho para ler a escala COD: "))
    ler = open('ESCALA_COD.txt', 'r') #Se for ler entrada trocar o arquivo pela variavel "Caminho_entrada"
    conteudo_arquivo = ler.read()

    split = conteudo_arquivo.split("\n\n")

    dias_do_mes = split[0]
    ler_escala_manha = split[1]
    ler_escala_tarde = split[2]
    ler_escala_noite = split[3]

    escala_manha = ler_escala_manha.split("|") 
    escala_tarde = ler_escala_tarde.split("|")
    escala_noite = ler_escala_noite.split("|")
    escala = ""

    ##caminho_saida = input(str("Entre com um caminho para escrever a escala DDS: "))
    escala_dds = open('ESCALA_DDS.txt', 'w')#Se for escrever em um arquivo entrada trocar o arquivo pela variavel "Caminho_saida"

    #print("\n\n")   


    while contador_dia != dias_do_mes:
        
        apresentação = randrange(0, n_deoperadores)

        if ((apresentação != ultimo_operador_manha) and (operadores_letra[apresentação] in escala_manha[contador_dia])):
            print ("Data: {}".format(contador_dia+1))
            escala_dds.write("Data: {}\n".format(contador_dia+1))      
            print("Operador da manhã: {}".format(operadores_nomes[apresentação]))
            escala_dds.write("Operador da manhã: {}\n".format(operadores_nomes[apresentação])) 
            ultimo_operador_manha = apresentação
            ok1 = 0

            while ok1 == 0:

                apresentação1 = randrange(0, n_deoperadores)

                if ((apresentação1 != ultimo_operador_tarde) and (operadores_letra[apresentação1] in escala_tarde[contador_dia])):
                    print("Operador da tarde: {}".format(operadores_nomes[apresentação1]))
                    escala_dds.write("Operador da tarde: {}\n".format(operadores_nomes[apresentação1])) 
                    ultimo_operador_tarde = apresentação1
                    ok1 = 1
                    ok2 = 0
            
            while ok2 == 0:

                apresentação2 = randrange(0, n_deoperadores)

                if ((apresentação2 != ultimo_operador_noite) and (operadores_letra[apresentação2] in escala_noite[contador_dia])):
                    print("Operador da noite: {}".format(operadores_nomes[apresentação2]))
                    escala_dds.write("Operador da noite: {}\n\n".format(operadores_nomes[apresentação2])) 
                    ultimo_operador_noite = apresentação2
                    contador_dia = contador_dia + 1
                    print("=======================================")
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

