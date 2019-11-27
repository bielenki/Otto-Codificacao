# Otto Codificação

[Vídeo no Youtube de exemplo de uso da ferramenta](https://youtu.be/HsCwkopj6mY)

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

![toolbox](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/toolbox.png?raw=true)

O script Codificação Otto Pfafstetter realiza a codificação dos trechos da rede de drenagem. Ao executar a
ferramenta os campos [Pfaf] e [cocurso] são adicionados a tabela de atributos.

![script](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/script.png?raw=true)

**Botão de seleção a montante**

![icone2](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/icone2.png?raw=true)

![barra4](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra4.png?raw=true)

A partir deste botão, e com uma feição do layer selecionada a ferramenta seleciona todas as feições do layer
que estão a montante.

![figmont](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/figmont.png?raw=true)

**Botão de seleção a jusante**

![icone3](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/icone3.png?raw=true)

![barra5](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra5.png?raw=true)

A partir deste botão, e com uma feição do layer selecionada a ferramenta seleciona todas as feições do layer
que estão a jusante, ou seja, o caminho até a foz.

![figjus](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/figjus.png?raw=true)

**Botão para gerar os códigos dos cursos d’agua**

![icone4](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/codigo.png?raw=true)

![barra6](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra6.png?raw=true)

Adiciona o campo [COCURSO] na tabela de atributos.

**Botão de acumulação**

![icone5](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/acumula.png?raw=true)

![barra7](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra7.png?raw=true)

Realiza a acumulação de um determinado atributo de montante para jusante, adicionando um novo layer ao
projeto que é uma cópia do layer da rede de drenagem adicionado de um campo na tabela de atributos que
é o valor acumulado do atributo selecionado a partir da combobox Atributo. O campo adicionado recebe o
nome do campo selecionado acrescido do sufixo “_Acum”.

**ComboBox Atributo**

A partir desta combobox seleciona-se o campo da tabela de atributos que se deseja acumular com a função
acumulação.

![barra8](https://github.com/bielenki/Otto-Codificacao/blob/master/Fig/barra8.png?raw=true)
