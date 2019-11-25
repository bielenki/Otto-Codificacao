# Otto Codificação
Algoritmo para codificação automática de rede de drenagem, segundo a classificação de Otto Pfafstetter.

Foi desenvolvida uma barra de ferramentas para o ArcGIS.

![barra](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra.png?raw=true)
**ComboBox Rede de Drenagem**

![barra2](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra2.png?raw=true)
A partir deste combobox deve-se selecionar o Layer da rede de drenagem sobre a qual serão executadas as
tarefas da barra de ferramenta.

**Botão para codificação de Otto Pfafstetter**
![icone1](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/icone1.png?raw=true)
![barra3](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra3.png?raw=true)
A partir deste botão tem-se acesso ao script de codificação que está na ToolBox Otto Pfafstetter. Caso a
ToolBox ainda não esteja adicionada ao projeto ela será adicionada.

O script Codificação Otto Pfafstetter realiza a codificação dos trechos da rede de drenagem. Ao executar a
ferramenta os campos [Pfaf] e [cocurso] são adicionados a tabela de atributos.


**Botão de seleção a montante**

A partir deste botão, e com uma feição do layer selecionada a ferramenta seleciona todas as feições do layer
que estão a montante.

**Botão de seleção a jusante**

A partir deste botão, e com uma feição do layer selecionada a ferramenta seleciona todas as feições do layer
que estão a jusante, ou seja, o caminho até a foz.


**Botão para gerar os códigos dos cursos d’agua**

Adiciona o campo [COCURSO] na tabela de atributos.

**Botão de acumulação**

Realiza a acumulação de um determinado atributo de montante para jusante, adicionando um novo layer ao
projeto que é uma cópia do layer da rede de drenagem adicionado de um campo na tabela de atributos que
é o valor acumulado do atributo selecionado a partir da combobox Atributo. O campo adicionado recebe o
nome do campo selecionado acrescido do sufixo “_Acum”.

**ComboBox Atributo**

A partir desta combobox seleciona-se o campo da tabela de atributos que se deseja acumular com a função
acumulação.
