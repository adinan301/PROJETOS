import csv
import bisect

class FilmeBTree:
    def __init__(self):
        self.btree = []  # Lista para armazenar os filmes
        self.filmes_dict = {}  # Dicionário para mapear filme_id para filme completo

    def insere_filme(self, filme):
        filme_id = filme["movieId"]
        bisect.insort(self.btree, filme_id)
        self.filmes_dict[filme_id] = filme

    def pesquisa_filme(self, pesquisa_chave, criterio):
        if criterio == "movieId":
            if pesquisa_chave in self.filmes_dict:
                return self.filmes_dict[pesquisa_chave]
        elif criterio == "title":
            for filme_id in self.btree:
                filme = self.filmes_dict[filme_id]
                if filme["title"].lower() == pesquisa_chave.lower():
                    return filme
        elif criterio == "genres":
            for filme_id in self.btree:
                filme = self.filmes_dict[filme_id]
                if pesquisa_chave.lower() in filme["genres"].lower():
                    return filme
        return None

# CARREGA O ARQUIVO CSV DA BASE

def carrega_filmes_da_base(caminho_arquivo):
    filmes = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            filmes.append(linha)
    return filmes

caminho_arquivo = "C:/Users/adina/Desktop/MOVIES/movies.csv"
filmes = carrega_filmes_da_base(caminho_arquivo)

btree_filmes = FilmeBTree()

# INSERE FILMES NA B-TREE

for filme in filmes:
    btree_filmes.insere_filme(filme)

# SOLICITAR AO USUÁRIO QUAL O CRITÉRIO DE PESQUISA
# TRATA AS EXCEÇÕES

criterios_validos = ["movieId", "title", "genres"]
pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")
while pesquisa_criterio not in criterios_validos:
    print("CRITÉRIO INVÁLIDO, INSIRA UM CRITÉRIO VÁLIDO")
    pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")

# PESQUISAR O FILME PELO CRITÉRIO

pesquisa_chave = input("INFORME O ID / NOME / GÊNERO A SER PESQUISADO: ")
resultado = btree_filmes.pesquisa_filme(pesquisa_chave, pesquisa_criterio)

if resultado:
    print("FILME ENCONTRADO PELO CRITÉRIO", pesquisa_criterio + ":", resultado)
else:
    print("NENHUM FILME ENCONTRADO PELO CRITÉRIO", pesquisa_criterio + ".")
