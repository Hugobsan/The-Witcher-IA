import openai


openai.api_key = input("Digite sua API Key do OpenAI: ")

def perguntar(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    print("Alquimia: "+response.choices[0].text.strip())


init_text= "Eu sou um robô altamente inteligente que responde perguntas baseadas em informações fornecidas. Se você me fizer uma pergunta eu responderei com as informações que possuo. Caso eu não saiba responder, minha resposta será \"Não sei.\"\n" 
print("Olá, eu sou um robô criado para funcionar como uma Wiki interativa do jogo The Witcher, atualmente estou equipado para auxiliar em tarefas de Alquimia.")
user_question = 0
wiki= """
As informações que eu possuo sobre as poções, óleos e bombas do jogo são:

Bindweed
Efeitos: Esta poção aumenta a resistência a ácido e venenos
com base ácida.
Preparação: Esta poção é feita misturando-se uma medida cada
de éter, enxofre e cinábrio; álcool forte (strong alcohol) deve
ser usado como base.
Duração: Longa.
Toxicidade: Média.

Black-Blood
Efeitos: Transforma o sangue do bebedor em veneno; o sangue
torna-se mortal para quem bebê-lo.
Preparação: A poção é feita misturando-se três medidas cada
de ácido sulfúrico, uma medida de rebis e éter; álcool de
extrema qualidade (top quality alcohol) deve ser usado como
base.
Duração: Longa.
Toxicidade: Alta.

Blizzard
Efeitos: Blizzard é uma das poções mais poderosas de um
witcher; ela aumenta os reflexos e o tempo de reação,
permitindo ao witcher aparar e esquivar-se de ataques melhor.
Preparação: A poção é feita misturando-se duas medidas cada
de ácido sulfúrico e rebis; álcool de boa qualidade (high quality
alcohol) deve ser usado como base.
Duração: Curta.
Toxicidade: Média.

Cat
Efeitos: Esta poção garante visão na escuridão total.
Preparação: A poção é feita misturando-se uma medida de
rebis e duas medidas de enxofre; álcool forte (strong alcohol)
deve ser usado como base.
Duração: Longa.
Toxicidade: Pequena.

De Vries’ Extract
Efeitos: Esta poção torna visíveis criaturas ocultas.
Preparação: A poção é feita misturando-se uma medida cada de
rebis, éter e mercúrio com duas medidas de enxofre; álcool
de extrema qualidade (top quality alcohol) deve ser usado
como base.
Duração: Curta.
Toxicidade: Média.

Fisstech
Efeitos: Fisstech não tem nenhum efeito benéfico; ao contrário,
o narcótico causa ao seu usuário confusão e perda de
consciência.
Preparação: A droga é feita misturando-se uma medida cada de
cinábrio e enxofre com três medidas de mercúrio; álcool de
extrema qualidade (strong, top quality alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Nenhuma.

Full Moon
Efeitos: Esta poção aumenta significativamente a vitalidade
máxima.
Preparação: A poção é feita misturando-se duas medidas cada
de cinábrio e mercúrio com uma medida de enxofre; álcool
de extrema qualidade (strong, top quality alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Alta.

Golden Oriole
Efeitos: Esta poção torna o sangue do witcher imune a venenos
e neutraliza os efeitos de venenos já presentes em sua corrente
sanguínea.
Preparação: A poção é feita misturando-se duas medidas cada
de éter e ácido sulfúrico; álcool de boa qualidade (strong, high
quality alcohol) deve ser usado como base.
Duração: Longa.
Toxicidade: Média.

Kiss
Efeitos: A Kiss aumenta a resistência à sangramento e estanca
qualquer sangramento atual.
Preparação: A poção é feita misturando-se uma medida de
ácido sulfúrico e duas de cinábrio; álcool forte (strong
alcohol) deve ser usado como base.
Duração: Longa.
Toxicidade: Média.

Maribor Forest
Efeitos: Esta poção aumenta significativamente a Resistência
(Endurance) máxima; é usada predominantemente por witchers
treinados no uso de sinais.
Preparação: A poção é feita misturando-se duas medidas de
rebis com uma medida cada de éter e enxofre; álcool de boa
qualidade (strong, high quality alcohol) deve ser usado como
base.
Duração: Longa.
Toxicidade: Média.

Perfume
Efeitos: Perfume tem um bom cheiro e é um presente que
quase qualquer mulher apreciará; ele pode frequentemente
servir como um benvindo substituto para outros presentes.
Preparação: O perfume é feito misturando-se uma medida cada
de ácido sulfúrico, éter e enxofre; álcool forte (strong alcohol)
deve ser usado como base.
Duração: Longa.
Toxicidade: Baixa.

Petri’s Philter
Efeitos: Petri's Philter aumenta a intensidade de todos os sinais
do witcher.
Preparação: A poção é feita misturando-se uma medida cada de
enxofre, mercúrio e cinábrio com duas de rebis; álcool
concentrado de boa qualidade (concentrated, high quality
alcohol) deve ser usado como base.
Duração: Longa.
Toxicidade: Muito Alta.

Shrike
Efeitos: Provoca dor aos agressores durante o combate.
Preparação: A poção é feita misturando-se uma medida cada de
enxofre, mercúrio e rebis com duas de cinábrio; álcool forte
de extrema qualidade (strong, top quality alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Alta.

Swallow
Efeitos: Acelera a regeneração da vitalidade.
Preparação: A poção é feita misturando-se uma medida cada de
ácido sulfúrico e éter com duas de rebis; álcool forte de boa
qualidade (strong, high quality alcohol) deve ser usado como
base.
Duração: Curta.
Toxicidade: Média.

Tawny Owl
Efeitos: Aumenta significativamente a regeneração da
Resistência (Endurance); é particularmente valiosa para
witchers que usam sinais em combate.
Preparação: A poção é feita misturando-se uma medida de
ácido sulfúrico com duas de éter; álcool forte (strong alcohol)
deve ser usado como base.
Duração: Longa.
Toxicidade: Média.

Thunderbolt
Efeitos: Aumenta o dano infligido durante o combate, mas
torna impossível desviar ou aparar um golpe.
Preparação: A poção é feita misturando-se uma medida cada de
ácido sulfúrico, mercúrio e rebis com duas de cinábrio; álcool
forte de extrema qualidade (strong, top quality alcohol)
deve ser usado como base.
Duração: Longa.
Toxicidade: Alta.

White Gull
Efeitos: White Gull é uma bebida alucinógena, mas pode ser
usada também para criar outras poções; serve como base para
poções complexas, permitindo até cinco outros ingredientes.
Preparação: A poção é feita misturando-se uma medida de
rebis com duas de ácido sulfúrico; álcool forte (strong alcohol)
deve ser usado como base.
Duração: Longa.
Toxicidade: Média.

White Honey
Efeitos: Reduz a toxicidade à zero e anula o efeito de outras
poções.
Preparação: A poção é feita misturando-se uma medida cada de
ácido sulfúrico, éter e rebis; álcool forte (strong alcohol)
deve ser usado como base.
Duração: Instantânea.
Toxicidade: Nenhuma.

White Raffard's Decoction
Efeitos: Restaura imediatamente uma grande parte da
Vitalidade perdida.
Preparação: A poção é feita misturando-se uma medida cada de
ácido sulfúrico e rebis com duas de mercúrio; álcool forte de
boa qualidade (strong, high-quality alcohol) deve ser usado
como base.
Duração: Instantânea.
Toxicidade: Alta.

Willow
Efeitos: Garante imunidade aos efeitos de atordoamento (stun)
e nocaute (knockdown).
Preparação: A poção é feita misturando-se uma medida de
enxofre com duas de éter; álcool forte (strong alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Alta.

Wives’ Tears
Efeitos: Cura a embriaguez instantaneamente, restaurando a
sobriedade sem os efeitos de uma ressaca.
Preparação: A poção é feita misturando-se uma medida cada de
enxofre, éter e rebis; álcool forte de boa qualidade (strong,
high-quality alcohol) deve ser usado como base.
Duração: Instantânea.
Toxicidade: Baixa.

Wolf
Efeitos: Melhora a concentração e a coordenação, aumentando
as chances de infligir dano crítico.
Preparação: A poção é feita misturando-se duas medidas cada
de ácido sulfúrico e mercúrio com uma de cinábrio; álcool forte
de extrema qualidade (strong, top quality alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Média.

Wolverine
Efeitos: Aumenta o dano infligido quando a Vitalidade do
witcher cai abaixo da metade.
Preparação: A poção é feita misturando-se uma medida cada de
enxofre, mercúrio e cinábrio com duas de éter; álcool forte de
extrema qualidade (strong, top quality alcohol) deve ser
usado como base.
Duração: Longa.
Toxicidade: Alta.

No jogo também existem as substâncias secundárias para criar as poções, cada substância tem um efeito diferente.
Para que a poção fique com um efeito secundário, todas as substâncias utilizadas no preparo devem conter a substância secundária concatenada. Ou seja, se deseja fazer uma poção com uma substância secundária, deve utilizar ácido sulfúrico com [nome da substância], rebis com [nome da substância], enxofe com [nome da substância], mercúrio com [nome da substância] ou cinábrio com [nome da substância] para todas as medidas de substâncias empregadas. 
As substâncias secundárias são: Albedo, Nigredo e Rubedo. 
As poções de "Albedo" reduzem o nível de toxina por uma hora, além disso, reduzem o nível de toxicidade das poções (Se o nível de toxicidade é Pequeno, com albedo será Nenhum, se for Médio, com albedo será Pequeno). 
As poções de "Nigredo" aumentam o poder de ataque.
As poções de "Rubedo" regeneram sua vitalidade. 
Elas não são obrigatórias para fazer uma poção, mas podem dar um bonus extra quando adicionadas.

"""
while user_question != "exit" or user_question != "Exit":
    text = init_text+wiki

    user_question = input("\nFaça sua pergunta (ou digite 'exit' para finalizar): ");
    if(user_question=="exit") or (user_question)=="Exit":
        break;
    query = "\nQ: "+ user_question +"\nA:"

    text += query
    perguntar(text)
