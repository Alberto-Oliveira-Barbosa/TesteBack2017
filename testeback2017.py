#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from random import randrange



#PATH COM O ENDEREÇO DO BANCO DE DADOS
path = 'banco.db'



menu = '''\nSelecione uma opcão:
I - Incluir um novo registro no banco de dados manualmente.
C - Calcular média do saldo dos clientes em um intervalo.
M - Mostrar todos os dados cadastrados no banco.
P - Popular o banco usando uma lista pré estabelecida - Insere 100 registros 
S - Sair

'''



################################ MÉTODOS ##################################################################################


def seleciona_opcao():

    opcao = str(input(menu)).strip().upper()[0]

    while opcao not in 'ICMPS':

        opcao = str(input("Opção inválida! \n" + menu)).strip().upper()[0]
    return opcao

def abre_conexao():
    conn = sqlite3.connect(path)
    return conn

def cria_banco():
    conn = abre_conexao()
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_customer_account (
id_customer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nm_customer VARCHAR(50),
cpf_cnpj VARCHAR(13),
is_active BOOLEAN,
vl_total FLOAT(7,2),
UNIQUE (id_customer)
);
""")
    conn.close()


def mostrar_dados():
    conn = abre_conexao()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tb_customer_account;')

    for f in cursor.fetchall():
        print('Código do cliente: %s'% f[0])
        print('Nome: %s'% f[1])
        print('Numero do CPF ou CNPJ: %s'% f[2])
        print ('Situação: %s' % ('Cliente Ativo' if f[3]==1 else 'Cliente NÃO ativo'))
        print('Saldo: %s'% f[4])
        print('\n----------------------------------------------------------------------')
              

    conn.close()




    
def cadastrar():
    
    nm_customer = str(input('Qual é o nome do cliente? '))
    cpf_cnpj = str(input('Informe o CPF ou CNPJ do cliente '))
    is_active =  1 if (str(input('Informe se o cliente está ativo atualmente [S/N]: ')).strip().upper()[0]) == 'S' else 0
    vl_total = float(input('Qual é o saldo? '))

    conn = abre_conexao()
    cursor = conn.cursor()

    cursor.execute("""
INSERT INTO tb_customer_account (nm_customer, cpf_cnpj, is_active, vl_total)
VALUES (?,?,?,?)
""",(nm_customer, cpf_cnpj, is_active, vl_total))

    conn.commit()
    conn.close() 


      



def calcular_media():
    conn = abre_conexao()
    cursor = conn.cursor()

    #calcula a média dos registros com o ID entre 1500 e 2700 e saldo maior que 560
    
    cursor.execute( 'SELECT * FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700 ORDER BY vl_total DESC')

    saldo_total = 0.0
    ocorrencias = 0

    for f in cursor.fetchall():
        print('Código do cliente: %s'% f[0])
        print('Nome: %s'% f[1])
        print('Numero do CPF ou CNPJ: %s'% f[2])
        print ('Situação: %s' % ('Cliente Ativo' if f[3]==1 else 'Cliente NÃO ativo'))
        print('Saldo: %s'% f[4])
        print('\n----------------------------------------------------------------------')
        saldo_total += f[4]
        ocorrencias+=1

    print('\nA média dos valores dos saldos dos clientes é: %.2f' % float(saldo_total/ocorrencias))
    print('De um total de %s clientes'% ocorrencias )

    conn.close()




def popular_com_lista():

    conn = abre_conexao()
    cursor = conn.cursor()

    
    dados = [("Vanna",757019,1,4675),("Serina",934989,1,3688),("Odysseus",356570,1,4334),("Lamar",124396,0,4664),("Gray",796973,1,2858),("Velma",95836,1,2576),("Allen",24575,0,4307),("Clio",573264,0,2713),("Lawrence",217963,1,1695),("Alexander",903538,0,4747),("TaShya",82068,0,4924),("Kennan",380043,0,125),("Ava",12567,1,716),("Elijah",187219,1,4213),("Tyrone",836088,0,3557),("Jordan",132439,0,3274),("Seth",550433,0,4295),("Orla",771049,1,207),("Charissa",652422,1,1851),("Merritt",230916,1,1447),("Gage",936667,0,4647),("Arden",7920,1,2735),("Blaze",941209,0,3492),("Amal",158905,0,3348),("Bethany",605799,0,1657),("Dale",61126,0,469),("Lois",170550,0,3363),("Xantha",93881,1,2464),("Idona",522752,1,4453),("Gannon",674000,0,1196),("Maxwell",831754,0,179),("Kaseem",100649,1,2082),("Shaine",92773,1,3907),("Gregory",648625,1,3856),("Delilah",202570,1,396),("Rashad",776544,1,3509),("Dakota",904815,1,2826),("Brenna",263044,0,464),("Donovan",952279,1,4988),("Aline",376990,1,255),("Zephania",767408,0,1819),("Jared",960722,0,892),("Sierra",1222,0,4179),("Angelica",747598,0,3243),("Imogene",961202,1,1699),("Brenden",832231,0,64),("Rose",569843,0,4797),("Uma",89236,0,3776),("Hanna",902695,0,12),("Cole",728574,0,1560),("Avye",751161,1,34),("Joshua",897758,1,152),("Sade",655848,0,2709),("Bethany",924956,0,3023),("Yeo",363967,1,379),("Ivor",854794,0,3290),("Lionel",305716,1,994),("Piper",152866,0,4614),("Giselle",272841,1,4103),("Garrett",170792,0,541),("Sloane",756429,1,248),("Autumn",320125,0,770),("Willow",39151,0,1361),("Upton",762579,0,2086),("Elaine",949104,1,4672),("Cora",923110,0,214),("Michael",639239,0,3113),("Ethan",376107,0,123),("Skyler",737530,0,296),("Ali",489458,1,3365),("Holmes",327898,1,3476),("Alfonso",83941,1,1982),("Zoe",297466,1,3921),("Nadine",704505,1,4836),("Alvin",798815,1,2777),("Carla",522980,1,1358),("Whitney",572015,0,770),("Preston",163024,0,2813),("Renee",568169,1,3754),("Ila",440852,1,301),("Steel",843398,0,4395),("Rudyard",213991,1,4238),("Magee",292833,1,3311),("Kathleen",593740,1,790),("Erich",713703,1,1525),("Kessie",541026,0,705),("Xena",398216,0,3563),("Skyler",951588,1,2327),("Illana",840694,0,867),("Rhoda",473334,1,108),("Brittany",362763,0,4456),("Tad",895588,1,4314),("Fuller",660226,1,1740),("Honorato",697148,0,906),("Dolan",16992,0,2024),("Brady",407291,0,2453),("Otto",252027,1,3725),("Martena",124896,1,4468),("Bethany",505651,1,96),("Kibo",33730,0,4505)]

    cursor.executemany("""
INSERT INTO tb_customer_account(nm_customer,cpf_cnpj,is_active,vl_total)
VALUES(?,?,?,?)""",dados)

    
    conn.commit()

    conn.close()


#####################################################################################################






    

print('---------------------------------------------------------')
print('--------Desenvolvido por Alberto Oliveira Barbosa--------')
print('---------------------------------------------------------')



cria_banco()



while True:
    
    op = seleciona_opcao()

    if (op == 'I'):
        cadastrar()
    elif (op == 'C'):
        calcular_media()
    elif (op == 'M'):
        mostrar_dados()
    elif (op == 'P'):
        popular_com_lista()
    else:
        exit()
