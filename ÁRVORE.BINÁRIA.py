import csv


class FilmeArvoreBinaria:
    def __init__(self, filme):
        self.filme = filme
        self.left = None
        self.right = None


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def insere_filme(self, filme):
        if self.root is None:
            self.root = FilmeArvoreBinaria(filme)
        else:
            self._insere_filme_recursivo(filme, self.root)

    def _insere_filme_recursivo(self, filme, no_atual):
        if filme["movieId"] < no_atual.filme["movieId"]:
            if no_atual.left is None:
                no_atual.left = FilmeArvoreBinaria(filme)
            else:
                self._insere_filme_recursivo(filme, no_atual.left)
        else:
            if no_atual.right is None:
                no_atual.right = FilmeArvoreBinaria(filme)
            else:
                self._insere_filme_recursivo(filme, no_atual.right)

    def pesquisa_filme(self, pesquisa_chave, criterio):
        return self._pesquisa_filme_recursivo(pesquisa_chave, criterio, self.root)

    def _pesquisa_filme_recursivo(self, pesquisa_chave, criterio, no_atual):
        if no_atual is None:
            return None

        if criterio == "movieId" and str(no_atual.filme["movieId"]) == pesquisa_chave:
            return no_atual.filme
        if criterio == "title" and no_atual.filme["title"].lower() == pesquisa_chave.lower():
            return no_atual.filme
        if criterio == "genres" and pesquisa_chave.lower() in no_atual.filme["genres"].lower():
            return no_atual.filme

        if pesquisa_chave < str(no_atual.filme["movieId"]):
            return self._pesquisa_filme_recursivo(pesquisa_chave, criterio, no_atual.left)
        else:
            return self._pesquisa_filme_recursivo(pesquisa_chave, criterio, no_atual.right)


def carrega_filmes_da_base(caminho_arquivo):
    filmes = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            filmes.append(linha)
    return filmes


caminho_arquivo = "C:/Users/adina/Desktop/MOVIES/movies.csv"
filmes = carrega_filmes_da_base(caminho_arquivo)

arvore_binaria = ArvoreBinaria()

for filme in filmes:
    arvore_binaria.insere_filme(filme)

criterios_validos = ["movieId", "title", "genres"]
pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")
while pesquisa_criterio not in criterios_validos:
    print("CRITERIO INVALIDO, INSIRA UM CRITERIO VALIDO")
    pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")

pesquisa_chave = input("INFORME O ID / NOME / GENERO A SER PESQUISADO: ")
resultado = arvore_binaria.pesquisa_filme(pesquisa_chave, pesquisa_criterio)

if resultado:
    print("FILME ENCONTRADO PELO CRITERIO", pesquisa_criterio + ":", resultado)
else:
    print("NENHUM FILME ENCONTRADO PELO CRITERIO", pesquisa_criterio + ".")
