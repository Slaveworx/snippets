#encoding: ISO-8859-1


#vai incluir a biblioteca colorize que permite imprimir string coloridas
require 'colorize'

#variaveis globais
$pontuacao = 0
$saida = false
jogar_novamente = false

print "
=======================================================
=========BEM VINDO AO PEDRA, PAPEL OU TESOURA==========
==================por Tiago Galvão=====================
=======================================================
".bold.black

#metodo que define um novo jogo
def novojogo
  $pontuacao = 0
  $saida = false
end

#metodo que possibilita saida do jogo terminado o loop principal
def sair
  $pontuacao = 0
end

###############################################################
#                                                             #
#                 LOOP PRINCIPAL DO JOGO                      #
#                                                             #
###############################################################

while $saida == false
  elementos = [:pedra, :papel, :tesoura] #elementos da IA
  $mao = elementos.sample #vai selecionar aleatoriamente um valor do array

  puts "Pedra: ".black + "p".blue.bold + " | Papel: ".black + "pp".blue.bold + " | Tesoura: ".black + "t".blue.bold + " | ".black + "Pontuação: ".bold.blue + "#{$pontuacao}".red.bold
  print "\nInsira a sua jogada ".black.bold + "(".black.bold + "p ".yellow + ", ".black.bold + "pp".yellow + " ou ".black.bold + "t".yellow + "):".black.bold
  $input =gets.chomp #recebe o input do jogador


def verificar #METODO QUE COMPARA O INPUT DO JOGADOR COM O RETORNO DO ARRAY E MOSTRA O OUTPUT
  if $input == "p" && $mao == :pedra || $input == "pp" && $mao == :papel || $input == "t" && $mao == :tesoura  
   puts "****EMPATOU! contra #{$mao}**** \n\n".yellow
 
  elsif $input == "p" && $mao == :papel || $input == "pp" && $mao == :tesoura || $input == "t" && $mao == :pedra 
   puts "****PERDEU! contra #{$mao}**** \n\n".red
   $pontuacao -= 1
 
  elsif $input == "p" && $mao == :tesoura || $input == "pp" && $mao == :pedra || $input == "t" && $mao == :papel  
   puts "****GANHOU! contra #{$mao}**** \n\n".green
   $pontuacao += 1

  else
   if $input == "sair"
    puts "\n Obrigado por jogar este jogo! A sua pontuação foi de #{$pontuacao} pontos.".green
    $pontuacao = 0
    $saida = true
   end
 end
end


case $input #Este Switch vai recolher o input e encaminha-lo para o método "verificar"
  when "p" then verificar #pedra
  when "pp" then verificar #papel
  when "t" then verificar #tesoura
  when "sair" then verificar
  else puts "**Jogada Inválida**\n\n".bold
end

#GAMEOVER
if $pontuacao == -2
$saida = true #dá-nos a saída do loop principal do jogo
jogar_novamente = true #Cria condições para perguntar se o jogador quer tentar novamente
puts "\n\n *************Você perdeu**************".bold.red

while jogar_novamente == true 

print "\n Deseja jogar novamente? (s/n) ?".bold.blue
novo_jogo = gets.chomp

case novo_jogo #recebe o input e vai tratá-lo
when "s" then jogar_novamente = false, novojogo 
when "n" then $saida = true, sair && jogar_novamente = false
else puts "Opção Inválida! Escreva 's' para SIM e 'n' para NÃO!"
end
end
end
end
