class Pessoa:
    #atributo da classe ou atributo default
    olhos=2
    #métodos - atributos de classe
    def __init__(self, *filhos, nome= None, idade=30):
        #atributos de instancia ou atributos de objeto - atributos criado peelo __init__
        #atributo nome com valor do parâmetro passado nome
        self.nome = nome
        self.idade = idade
        #atributo complexo lista
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


    #método de classe - está atrelado a classe. Independe de um objeto
    #decorato @staticmethod @classmethod
    @staticmethod
    def metodo_estatico():
        return 42

    @ classmethod
    #cls faz alusão a classe que está executando neste caso classe Pessoa
    # Se usa classmethod quando se quer acesssar dados da própria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    #__dict__ - confere apenas os atributos de instância de um objeto os atributos de classe não
    print(Mari.__dict__)
    tassiani.olhos = 2
    del tassiani.olhos
    print(tassiani.__dict__)
    Pessoa.olhos = 3
    # p.nome = 'Tassi'
    #print(p.nome)
    print(Pessoa.olhos)
    print(Mari.olhos)
    print(tassiani.olhos)
    print(id(Pessoa.olhos), id(Mari.olhos), id(tassiani.olhos))
    print(Pessoa.metodo_estatico(), Mari.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Mari.nome_e_atributos_de_classe())