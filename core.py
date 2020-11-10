import telebot
import urllib3
from random import randint
from time import sleep

bot = telebot.TeleBot("1252122617:AAGcEUa7WTZzLoaoQPXRp4-U20T2CIVG9-s")


@bot.message_handler(func=lambda message: message.text == 'Olá, Planck!' and message.content_type == 'text')
def oi(message):
    cid = message.chat.id
    bot.send_message(cid, 'Olá! Meu nome é Max Planck e eu sou um cientista alemão, considerado por muitos como o pai '
                          'da física quântica. Minhas principais descobertas estão relacionadas com a descoberta do '
                          'quantum e da famosa constante de Planck. ')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Vamos lá!')
    markup.add(itembtn1)
    sleep(1.5)
    bot.send_message(cid, 'Para iniciar a nossa conversa, vou te contar um pouco sobre mim!', reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_start_message(message):
    cid = message.chat.id
    bot.send_message(cid, 'Olá! Meu nome é Max Planck e eu sou um cientista alemão, considerado por muitos como o pai '
                          'da física quântica. Minhas principais descobertas estão relacionadas com a descoberta do '
                          'quantum e da famosa constante de Planck. ')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Vamos lá!')
    markup.add(itembtn1)
    sleep(1.5)
    bot.send_message(cid, 'Para iniciar a nossa conversa, vou te contar um pouco sobre mim!', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Vamos lá!' and message.content_type == 'text')
def bio(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Que interessante! Poderia me contar mais sobre sua história?')
    itembtn2 = telebot.types.KeyboardButton('Que legal! Mas poderíamos falar sobre suas descobertas?')
    markup.add(itembtn1)
    markup.add(itembtn2)
    bot.send_message(cid, 'Eu nasci no ano de 1858 e vim a falecer em 1947 aos 89 anos. Minha história começa em Kiel '
                          'um condado no norte da Alemanha.')
    sleep(2)
    bot.send_message(cid, 'Desde de pequeno eu apresentava muitos talentos diversos, tanto para a música como para as '
                          'línguas antigas, a matemática e a física.')
    sleep(3)
    bot.send_message(cid, 'Após meu nascimento fui batizado com o nome Karl Ernst Ludwig Marx Planck, onde Marx é '
                          'abreviação de Markus, porém eu não me lembro ao certo o motivo mas aos dez anos assinei com '
                          'o nome Max que é abreviação de Maximilian e utilizei esse nome pelo resto da minha vida.')
    sleep(3)
    bot.send_message(cid, 'Meus estudos contribuíram muito para o avanço científico e por conta deles eu sou '
                          'considerado o criador da "teoria da física quântica" e até ganhei um prêmio nobel por isso.'
                          ' ')
    sleep(3)
    bot.send_message(cid, 'Minhas descobertas foram tão importantes que após minha morte a Academia de Ciências Kaiser '
                          'Wilhelm recebeu o nome de Max Planck e o maior prêmio científico da Alemanha passou a ser a '
                          'chamado de "Medalha Planck".', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Que interessante! Poderia me contar mais sobre sua história?' and message.content_type == 'text')
def vida(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Pode me contar um poucos a respeito da sua vida pessoal?')
    itembtn2 = telebot.types.KeyboardButton('Eu gostaria de saber mais sobre a sua vida acadêmica!')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    bot.send_message(cid, 'Com certeza! Sobre qual parte de minha vida você gostaria de saber?', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Poderia me contar um poucos a respeito da sua vida pessoal?' and message.content_type == 'text')
def pessoal(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Que legal! Mas poderíamos falar sobre suas descobertas?')
    itembtn2 = telebot.types.KeyboardButton('Eu gostaria de saber mais sobre a sua vida acadêmica!')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    bot.send_message(cid, 'Eu vim de uma família  tradicional, na qual existiam muitos juízes, cientistas e teólogos')
    sleep(2)
    bot.send_message(cid,
                     'Nasci em Kiel um porto do Mar Báltico, capital de Schleswig-Holstein, norte da Alemanha, '
                     'no dia no dia 23 de abril de 1858.')
    sleep(2)
    bot.send_message(cid,
                     'Meu pai Johann Julius Wilhelm Planck, professor de direito Constitucional na Universidade de '
                     'Kiel, teve duas esposas embora dois de meus irmãos fossem do primeiro casamento de meu pai eu '
                     'era o sexto filho dele. ')
    sleep(3)
    bot.send_message(cid,
                     'Em 1867 minha família se mudou para Munique, e eu fui matriculado na escola ginasial '
                     'Maximilians, onde fiquei sob a tutela de Hermann Müller, que me ensinou astronomia, mecânica e '
                     'matemática, e por conta disso meus primeiros trabalhos foram sobre termodinâmica. ')
    sleep(3)
    bot.send_message(cid,
                     'Algo interessante, foi que meu professor Philipp von Jolly me aconselhou a não estudar física, '
                     'dizendo que na física não tinha mais quase nada relevante a pesquisar e eu respondi dizendo que '
                     'não queria descobrir coisas novas, apenas compreender os fundamentos conhecidos do assunto. ')
    sleep(3)
    bot.send_message(cid,
                     'Felizmente para a ciência atual eu não segui o conselho de Jolly e em 1874, com apenas 16 anos, '
                     'ingressei na Universidade de Munique. E em 1879, com apenas 21 anos, me doutorei.')
    sleep(3)
    bot.send_message(cid,
                     'Após voltar para Kiel me casei com Marie Merck em 1886 que infelizmente ela veio a falecer em '
                     '1909 por conta de uma tuberculose. Depois disso, vim a me casar no ano seguinte com Marga von '
                     'Hoesslin. ')
    sleep(3)
    bot.send_message(cid,
                     'A partir daqui só houveram desgraças em minha vida pessoal como a morte do meu filho '
                     'primogênito em 1916 na batalha de Verdun, morte das minhas gêmeas (Emma e Grete) que morreram '
                     'ao dar a luz aos seus filhos em 1917 e 1919.')
    sleep(3)
    bot.send_message(cid,
                     'Por fim, o que tirou minha vontade de viver foi a morte do filho mais novo Erwin, em janeiro de '
                     '1945, que foi executado após ser acusado de traição relacionado a um atentado para matar '
                     'Hitler. Minha casa e minha biblioteca foram destruídas pelos bombardeiros da guerra.')
    sleep(3)
    bot.send_message(cid,
                     'Depois disso, minha morte veio logo em seguida no dia 4 de outubro de 1947, aos 89 anos, '
                     'tendo como consequência uma queda e diversos derrames. Além disso, minha morte segundo James '
                     'Franck, veio a mim "como uma redenção."', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Eu gostaria de saber mais sobre a sua vida acadêmica!' and message.content_type == 'text')
def acad(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Que legal! Mas poderíamos falar sobre suas descobertas?')
    itembtn2 = telebot.types.KeyboardButton('Pode me contar um poucos a respeito da sua vida pessoal?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    sleep(2)
    bot.send_message(cid, 'Confesso que eu não gostava muito de experimentos, porém em 1974 comecei meus estudos na '
                          'Universidade de Munique onde realizei um dos únicos experimentos de minha carreira '
                          'estudando a difusão de hidrogênio através de platina aquecida, sob supervisão de  Philipp '
                          'von Jolly.')
    sleep(3)
    bot.send_message(cid, 'Em 1877 fui para Berlim estudar um ano com Hermann von Helmholtz e Gustav Kirchhoff e Karl '
                          'Weierstrass')
    sleep(3)
    bot.send_message(cid, 'Logo em seguida, passei nos exames de qualificação em outubro de 1878 Planck, '
                          'e em fevereiro de 1879 defendi minha dissertação sobre “o segundo teorema fundamental da '
                          'teoria mecânica do calor”.')
    sleep(3)
    bot.send_message(cid, 'Depois em junho de 1880, apresentei a minha tese de habilitação sobre “Estados de '
                          'equilíbrio de corpos isotrópicos em diferentes temperaturas”, e então me tornei professor '
                          'na Universidade de Munique.')
    sleep(3)
    bot.send_message(cid, 'Após isso em 1889, eu fui nomeado para a cadeira de Física da Universidade de Berlim e '
                          'depois dois anos fui nomeado professor de Física Teórica, substituindo Gustav Kirchhoff.')
    sleep(3)
    bot.send_message(cid, 'Em 1899, descobri uma nova constante fundamental, após pesquisar as radiações '
                          'eletromagnéticas, que foi batizada anos depois como Constante de Planck, que colaborou para '
                          'os estudos de  Albert Einstein e Niels Bohr.')
    sleep(3.5)
    bot.send_message(cid, 'Em 1900 eu utilizei a estatística de Boltzmann e a interpolação matemática para obter uma '
                          'nova equação que concordava com os resultados experimentais para todos comprimentos de '
                          'onda, e assim dei um fim a  “catástrofe do ultravioleta”. ')
    sleep(3)
    bot.send_message(cid, 'De 1905 a 1909, eu atuei como diretor-chefe da Sociedade Alemã de Física.')
    sleep(3)
    bot.send_message(cid, 'Em 1913, fui nomeado reitor da Universidade de Berlim, e em 1918 como consequência do '
                          'nascimento da física quântica, foi laureado com o Nobel de Física. ')
    sleep(3)
    bot.send_message(cid, 'De 1930 a 1937, eu fui presidente da KWG, Sociedade para o Avanço das Ciências do '
                          'Imperador Guilherme e fui senador da Sociedade Kaiser Wilhelm de 1916 a 1947. Além disso, '
                          'participei da da 1ª e da 5ª Conferência de Solvay.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Que legal! Mas poderíamos falar sobre suas descobertas?' and message.content_type == 'text')
def discover(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Por que estudar espectro da radiação do corpo negro?')
    itembtn2 = telebot.types.KeyboardButton('Mas o que é a constante de Planck?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    bot.send_message(cid, 'Claro!')
    sleep(3)
    bot.send_message(cid, 'Como eu disse anteriormente, o principal foco dos meus trabalhos era a Termodinâmica, '
                          'mas embora eu tivesse dedicado grande parte da minha carreira aos estudos dessa área, '
                          'meu nome ficou marcado pelo início dos estudos em uma nova área da Física, '
                          'a chamada Mecânica Quântica. 	')
    sleep(3)
    bot.send_message(cid, 'Tudo isso partiu da investigação de um problema sem solução até aquele momento, que era o '
                          'comportamento da radiação do corpo negro, no qual físicos tentavam investigar as '
                          'caracterísitca da luz emitida por um corpo que absorve toda a radiação incidente')
    sleep(3)
    bot.send_message(cid, 'Partindo deste estudo, consegui chegar a algumas conclusões que revolucionaram a Física.')
    sleep(3)
    bot.send_message(cid, 'A mais importante delas foi a de que a energia não se comporta de maneira contínua, '
                          'como acreditavam antigamente, mas sim de maneira discreta, sendo transmitida através de '
                          'pequenos “pacotes” denominados quantum, com um valor específico.')
    sleep(3)
    bot.send_message(cid, 'A partir disso também cheguei a um valor útil no cálculo da energia de um fóton, a chamada '
                          'constante de Planck.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Mas o que é a constante de Planck?' and message.content_type == 'text')
def constante(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Por que estudar espectro da radiação do corpo negro?')
    itembtn2 = telebot.types.KeyboardButton('Que interessante! Poderia me contar mais sobre sua história?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    bot.send_message(cid, 'Essa constante é um número definido pela natureza, que eu encontrei em meio aos meus '
                          'estudos.')
    sleep(3)
    bot.send_message(cid, 'Sua descoberta se deu em uma tentativa de descobrir novas maneiras de interpretar a '
                          'energia, uma delas era a de contrariar a interpretação feita na época, tratando a energia '
                          'como uma variável discreta, e não contínua.')
    sleep(3)
    bot.send_message(cid, 'Optei pela tentativa de escrever a energia como um conjunto de valores, e depois atribuir '
                          'uma variável à diferença média do intervalo entre esse valores.')
    sleep(3)
    bot.send_message(cid, 'Depois disso, escrevi essa variável do intervalo em função da frequência de '
                          'emissão/absorção, o que me levou a observar que havia uma proporcionalidade entre essa '
                          'frequência e o intervalo médio entre os valores de energia.')
    sleep(3)
    bot.send_message(cid, 'Tal proporcionalidade era regida por essa constante da natureza, que identifiquei como o '
                          'número 6,63x10^-34 J*s (bem próximo do valor considerado hoje, 6,62607015x10^-34 J*s), '
                          'a chamada constante de Planck. ', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Por que estudar espectro da radiação do corpo negro?' and message.content_type == 'text')
def why(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Catástrofe do ultravioleta?')
    itembtn2 = telebot.types.KeyboardButton('Mas o que despertou o seu interesse neste campo de estudo?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    sleep(2)
    bot.send_message(cid, 'O problema do corpo negro foi levantado pelo meu professor Gustav Kirchoff, em 1859, '
                          'que questionou o comportamento da radiação eletromagnética emitida por um corpo negro (nome '
                          'dado ao corpo que não reflete luz), dado que este era uma incógnita e não existia uma '
                          'explicação dentro da Física Clássica. ')
    sleep(3)
    bot.send_message(cid, 'Eram realizados vários experimentos com o objetivo de obter informações a respeito do corpo '
                          'negro, embora nada concreto fosse obtido. ')
    sleep(4)
    bot.send_message(cid, 'Wilheilm Wien propôs a aproximação de Wien, que possuía falhas ao prever o comportamento em '
                          'altas frequências; e Lord Rayleigh propôs a lei de Rayleigh-Jeans, que também era capaz de '
                          'prever os valores corretamente para baixas frequências, no entanto, resultava na famosa '
                          '"catástrofe do ultravioleta" em altas frequências, indicando que segundo esta teoria, '
                          'um corpo humano poderia até brilhar em algumas circunstâncias.')
    sleep(3)
    bot.send_message(cid, 'Dessa forma, essa área possuía um grande buraco na explicação deste fenômeno, '
                          'o que despertava o interesse de diversos físicos da época.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Catástrofe do ultravioleta?' and message.content_type == 'text')
def uv(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Mas o que despertou o seu interesse neste campo de estudo?')
    itembtn2 = telebot.types.KeyboardButton('Entendi! Mas quais são as contribuições dos seus estudos para a ciência?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    sleep(1)
    bot.send_message(cid, 'Isso mesmo!')
    sleep(3)
    bot.send_message(cid, 'A catástrofe do ultravioleta foi uma falha na teoria da física clássica, na minha época, '
                          'em explicar a emissão eletromagnética em um corpo negro.')
    sleep(3.5)
    bot.send_message(cid, 'Os cientistas John William Strutt e James Hopwwod Jeans erraram em utilizar o teorema da '
                          'equipartição da mecânica estatística clássica que estabelece que todo harmônico de um '
                          'sistema em equilíbrio tem uma média de energia correspondente ao produto da temperatura '
                          'com a constante de Boltzmann , prevendo que conforme o comprimento de onda diminua a '
                          'intensidade da radiação emitida tenderia ao infinito.')
    sleep(3)
    bot.send_message(cid, 'Para mim a catástrofe do ultravioleta não foi um problema, pois diferente de dos outros '
                          'cientistas, eu não considerava esse teorema como algo fundamental.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Mas o que despertou o seu interesse neste campo de estudo?' and message.content_type == 'text')
def interesse(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Interessante! Mas como você partiu disso e chegou na teoria do quantum?')
    itembtn2 = telebot.types.KeyboardButton('Entendi! Mas quais são as contribuições dos seus estudos para a ciência?')
    itembtn3 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    markup.add(itembtn3)
    sleep(1)
    bot.send_message(cid, 'Minha área de pesquisa sempre foi concentrada na Teoria Mecânica do Calor, tendo grande '
                          'parte de meus estudos sendo focados nas ideias de Clausius sobre a entropia.')
    sleep(3)
    bot.send_message(cid, 'Com base nisso, as incertezas acerca da situação indicada por Kirchoff me chamaram a '
                          'atenção, e essa necessidade de elaborar uma interpretação matemática para o espectro de '
                          'radiação do corpo negro foi a minha principal motivação para iniciar as investigações neste '
                          'assunto.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Interessante! Mas como você partiu disso e chegou na teoria do quantum?' and message.content_type == 'text')
def quantum(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Entendi! Mas quais são as contribuições dos seus estudos para a ciência?')
    itembtn2 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    markup.add(itembtn2)
    bot.send_message(cid, 'Posso lhe dizer que foi fruto de muita tentativa e muito trabalho.')
    sleep(2)
    bot.send_message(cid, 'A primeira solução que encontrei foi denominada de “princípio da desordem elementar”, '
                          'que partindo da lei de Wien, busquei definir a entropia de um oscilador ideal, '
                          'sem identificar a composição molecular deste oscilador.')
    sleep(3)
    bot.send_message(cid, 'Esta teoria não se sustentava em estudos mecânicos ou eletrodinâmicos, sendo fundamentada '
                          'com base na teoria cinética dos gases.')
    sleep(3)
    bot.send_message(cid, 'Embora parecesse ter chegado em uma ótima solução, pouco tempo depois foram feitos '
                          'experimentos que mostraram falhas no resultado em frequências baixas, o que derrubou toda '
                          'a minha teoria e me trouxe de volta aos trabalhos em busca de uma nova solução.')
    sleep(3)
    bot.send_message(cid, 'Após isso, me encontrei em uma situação na qual qualquer saída seria válida para encontrar '
                          'uma solução para esse trabalho. ')
    sleep(3)
    bot.send_message(cid, 'A mecânica estatística é uma área da física que interpreta os fenômenos com base em '
                          'probabilidade, essa área era utilizada em diversos trabalhos na época porém eu não '
                          'compactuava com essa perspectiva, pois eu possuía uma visão absoluta em relação a lei da '
                          'entropia, tendo ignorado esse recurso por muito tempo.')
    sleep(3.5)
    bot.send_message(cid, 'Dado esse momento de desespero, decidi ceder e utilizar de recursos da interpretação '
                          'estatística de Boltzmann da segunda lei da termodinâmica (sem abrir mão do meu ponto de '
                          'vista, claro), para tentar achar explicações, e nesse processo, me deparei com a '
                          'necessidade de contar o número de maneiras que a energia podia se distribuir entre os '
                          'osciladores.')
    sleep(3.5)
    bot.send_message(cid, 'Foi na tentativa de descobrir como realizar essa contagem que cheguei a conclusão que a '
                          'energia estava dividida em pequenas porções, em um processo denominado “quantização”, '
                          'enunciado assim a famosa equação E = hv.', reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Entendi! Mas quais são as contribuições dos seus estudos para a ciência?' and message.content_type == 'text')
def quantum(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Incrível! Agradeço a sua atenção, até mais!')
    markup.add(itembtn1)
    bot.send_message(cid, 'Honestamente, meus contribuíram de uma maneira expressiva para a ciência de modo global.')
    sleep(3)
    bot.send_message(cid, 'A constante de Planck é utilizada em diversos estudos, como por exemplo o príncipio da '
                          'incerteza de Heisenberg ou a equaçaõ de Schrödinger, que utilizam dela em seu '
                          'desenvolvimento.')
    sleep(2.5)
    bot.send_message(cid, 'Porém as maiores contribuições sem dúvidas são em relação ao modelo atômico de Bohr e ao '
                          'efeito fotoelétrico de Einstein. ')
    sleep(3)
    bot.send_message(cid, 'Rutherford não considerou os níveis de energia como quantizados, nesse caso, não haveria '
                          'uma explicação para os elétrons não perderem movimento acabarem em colisão com o núcleo. ')
    sleep(3)
    bot.send_message(cid, 'Então com base em meus estudos, Bohr foi guiado pela quantização da energia para propôr um '
                          'modelo que representasse os níveis de energia do átomo.')
    sleep(3)
    bot.send_message(cid, 'O efeito fotoelétrico de Einstein é basicamente uma confirmação da minha teoria! ')
    sleep(3)
    bot.send_message(cid, 'Ele indica a emissão de fótons em um material incandescido em determinadas frequências, '
                          'onde há transmissão de energia dos fótons para o material, também associando a energia e a '
                          'frequência à quantização da energia. ',reply_markup=markup)


@bot.message_handler(func=lambda
        message: message.text == 'Incrível! Agradeço a sua atenção, até mais!' and message.content_type == 'text')
def tchau(message):
    cid = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = telebot.types.KeyboardButton('Olá, Planck!')
    markup.add(itembtn1)
    bot.send_message(cid, 'Eu que agradeço, até mais!', reply_markup=markup)


bot.polling()
