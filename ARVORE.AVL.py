import csv

class NoFilme:
    def __init__(self, filme):
        self.filme = filme
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, filme):
        self.raiz = self._inserir_no(self.raiz, filme)

    def _inserir_no(self, no, filme):
        if no is None:
            return NoFilme(filme)
        
        if int(no.filme["movieId"]) == int(filme["movieId"]):
            return no

        if int(no.filme["movieId"]) < int(filme["movieId"]):
            no.direita = self._inserir_no(no.direita, filme)
        else:
            no.esquerda = self._inserir_no(no.esquerda, filme)
        
        no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))
        
        balanceamento = self._obter_balanceamento(no)
        
        if balanceamento > 1:
            if int(filme["movieId"]) < int(no.esquerda.filme["movieId"]):
                return self._rotacionar_direita(no)
            else:
                no.esquerda = self._rotacionar_esquerda(no.esquerda)
                return self._rotacionar_direita(no)
        
        if balanceamento < -1:
            if int(filme["movieId"]) > int(no.direita.filme["movieId"]):
                return self._rotacionar_esquerda(no)
            else:
                no.direita = self._rotacionar_direita(no.direita)
                return self._rotacionar_esquerda(no)
        
        return no

    def _obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _obter_balanceamento(self, no):
        if no is None:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        
        y.esquerda = z
        z.direita = T2
        
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))
        
        return y

    def _rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        
        y.direita = z
        z.esquerda = T3
        
        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))
        
        return y

    def buscar(self, chave, criterio):
        return self._buscar_no(self.raiz, chave, criterio)

    def _buscar_no(self, no, chave, criterio):
        if no is None:
            return None

        if criterio == "movieId" and str(no.filme["movieId"]) == chave:
            return no.filme
        if criterio == "title" and no.filme["title"].lower() == chave.lower():
            return no.filme
        if criterio == "genres" and chave.lower() in no.filme["genres"].lower():
            return no.filme
        
        if int(chave) < int(no.filme["movieId"]):
            return self._buscar_no(no.esquerda, chave, criterio)
        else:
            return self._buscar_no(no.direita, chave, criterio)

def carregar_filmes_da_base(caminho_arquivo):
    filmes = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            filmes.append(linha)
    return filmes

caminho_arquivo = "C:/Users/adina/Desktop/MOVIES/movies.csv"
filmes = carregar_filmes_da_base(caminho_arquivo)

arvore = ArvoreAVL()

for filme in filmes:
    arvore.inserir(filme)

criterios_validos = ["movieId", "title", "genres"]
pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")

while pesquisa_criterio not in criterios_validos:
    print("CRITÉRIO INVÁLIDO. INSIRA UM CRITÉRIO VÁLIDO.")
    pesquisa_criterio = input("INFORME O CRITÉRIO DE PESQUISA DESEJADO (movieId, title ou genres): ")

pesquisa_chave = input("INFORME O ID / NOME / GÊNERO A SER PESQUISADO: ")

resultado = arvore.buscar(pesquisa_chave, pesquisa_criterio)

if resultado:
    print("FILME ENCONTRADO PELO CRITÉRIO", pesquisa_criterio + ":", resultado)
else:
    print("NENHUM FILME ENCONTRADO PELO CRITÉRIO", pesquisa_criterio + ".")

