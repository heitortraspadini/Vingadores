from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def casa():
    return render_template("home.html")

@app.route("/ola")
def hello_world():
    return "<p>Olá, mundo!</p>"

# from codigo import Interface
# from vingador import Vingador

# def main():
#     # Pré-cadastrados
#     Vingador.lista_vingadores = [
#         Vingador("Thor", "Thor Odinson", "Deidade", ["Força", "Raio"], "Mjolnir", ["Arrogância"], 9000),
#         Vingador("Hulk", "Bruce Banner", "Meta-humano", ["Força", "Regeneração"], "Transformação", ["Raiva"], 10000)
#     ]

#     while True:
#         opcao = Interface.menu()
#         if opcao == "1":
#             Interface.cadastrar_vingador()
#         elif opcao == "2":
#             Interface.listar_vingadores()
#         elif opcao == "3":
#             Interface.detalhar_vingador()
#         elif opcao == "4":
#             Interface.convocar_vingador()
#         elif opcao == "5":
#             Interface.acao_em_vingador(lambda v: v.aplicar_tornozeleira())
#         elif opcao == "6":
#             Interface.acao_em_vingador(lambda v: v.aplicar_chip_gps())
#         elif opcao == "0":
#             Interface.ciencia()
#             print("Encerrando o sistema...")
#             break
#         input("\nPressione Enter para continuar...")

# if __name__ == "__main__":
#     main()