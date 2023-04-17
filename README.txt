Agenda:
1.0 O problema de negocio
2.0 Planejamento de solucao
3.0 O que e' Python?
4.0 Como escrever codigo Python?
5.0 Os primeiros comandos Python
6.0 Responder as questoes de negocio
7.0 Exerciocios


1.0 O problema de negocio

    Qual a Empresa: House Rocket 
    
    O que a empresa faz: House Rocket é uma plataforma de compra de venda de imóveis
    
    Qual o problema: O CEO gostaria de Maximizar o lucro encontrando bons negocios, encontar imoveis barratos e comprar depois vender mais caro.
    
    Qual a principal estrategia: Fontes externas para encontrar bons negocios.
    As perguntas do CEO da House Rocket: 
        1. Quantas casas estao disponiveis para compra?
        2. Quantos atributos as casas possuem?
        3. Quais sao esses atributos?
        4. Qual a casa mais cara do portfolio( casa com maior valor)?
        5. Qual a casa com o maior numero de quarto?

2.0 Planejamento de solucao
    2.1 Planejamento do PRODUTO FINAL, como vou entregar
        1. O que vou entregar ?(Planilha, Texto, Email, Modelo de ML, ...)
        R: Texto com as respostas.

        2. Como vai ser a entrega?
        R: Perguntas | Respostas

        Exemplo:
            1. Quantas casas estao disponiveis para compra?
            R: 2300 imoveis disponiveis para compra
            
            2. Quantos atributos as casas possuem?
            R: As casas possuem 10 atributos

    2.2 Planejamento do PROCESSO, como planejo fazer
        1. Onde esta a informacao? (Excel, DB, API, manual)
            R: https://www.kaggle.com/harlfoxem/housesalesprediction

        2. Como vou colectar essas informacoes? (SQL, Python, Streamlit, ...)
            R: Download(Apertar o botao)

        3. Responder as perguntas?
            1. Quantas casas estao disponiveis para compra?
                R: Contar o numero de linhas do conjunto de dados

            2. Quantos atributos as casas possuem?
                R: Contar o numero de colunas do conjunto de dados

            3. Quais sao esses atributos?
                R: Mostrar o nome das colunas(automatica)

            4. Qual a casa mais cara do portfolio( casa com maior valor)?
                R: Ordenar as linhas pela coluna de preco.

            5. Qual a casa com o maior numero de quarto?
                R: Contar o numero de linhas pela coluna numero de quartos
            
            
    2.2 Planejamento das FERRAMENTAS, como planejo fazer 

    Novas perguntas do CEO
    6. Qual a soma total de quartos do conjunto de dados