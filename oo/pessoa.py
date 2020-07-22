class Pessoa:
    #atributo da classe
    #métodos
    def __init__(self, *filhos, nome= None, idade=30):
        #atributos de instancia ou atributos de objeto - atributos criado peelo __init__
        #atributo nome com valor do parâmetro passado nome
        self.nome = nome
        self.idade = idade
        #atributo complexo lista
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    #p = Pessoa()
    #p = Pessoa('Tassiani')
    tassiani = Pessoa(nome='Tassiani')
    Mari = Pessoa(tassiani, nome='Mari')
    print(Pessoa.cumprimentar(tassiani))
    print(id(tassiani))
    print(tassiani.cumprimentar())
    print(Mari.nome)
    print(Mari.idade)
    for filho in Mari.filhos:
        print(filho.nome)
    #atributo dinâmico. Python cria atributo não definido na classe

    Mari.sobrenome = 'Freitas'
    print(Mari.sobrenome)
    #remoção de atributos dinamicamente
    del Mari.filhos
    #confere os atributos de instância de um objeto
    print(Mari.__dict__)
    print(tassiani.__dict__)
    # p.nome = 'Tassi'
    #print(p.nome)

