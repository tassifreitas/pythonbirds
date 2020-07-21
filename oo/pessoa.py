class Pessoa:
    #atributo da classe
    #métodos
    def __init__(self, nome = None, idade=30):
        #atributos de instancia ou atributos de objeto - atributos criado peelo __init__
        #atributo nome com valor do parâmetro passado nome
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    #p = Pessoa()
    p = Pessoa('Tassiani')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Tassi'
    print(p.nome)
    print(p.idade)

