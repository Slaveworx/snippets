#encoding: ISO-8859-1

require 'colorize'

$pontuacao = 0
$saida = false
jogar_novamente = false

print "
=======================================================
=========BEM VINDO AO PEDRA, PAPEL OU TESOURA==========
==================por Tiago Galvão=====================
=======================================================
".bold.black

def novojogo
$pontuacao = 0
$saida = false
end

def sair
$pontuacao = 0
end

while $saida == false
elementos = [:pedra, :papel, :tesoura]
$mao = elementos.sample
puts "Pedra: ".black + "p".blue.bold + " | Papel: ".black + "pp".blue.bold + " | Tesoura: ".black + "t".blue.bold + " | ".black + "Pontuação: ".bold.blue + "#{$pontuacao}".red.bold
print "\nInsira a sua jogada ".black.bold + "(".black.bold + "p ".yellow + ", ".black.bold + "pp".yellow + " ou ".black.bold + "t".yellow + "):".black.bold
$input =gets.chomp 


def verificar
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


case $input
when "p" then verificar
when "pp" then verificar
when "t" then verificar
when "sair" then verificar
else puts "**Jogada Inválida**\n\n".bold
end

if $pontuacao == -2
$saida = true
jogar_novamente = true
puts "\n\n *************Você perdeu**************".bold.red



while jogar_novamente == true 

print "\n Deseja jogar novamente? (s/n) ?".bold.blue
novo_jogo = gets.chomp

case novo_jogo
when "s" then jogar_novamente = false, novojogo 
when "n" then $saida = true, sair && jogar_novamente = false
else puts "Opção Inválida! Escreva 's' para SIM e 'n' para NÃO!"
end
end



end

end
