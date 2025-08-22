/*
TITULO: Biblioteca com fun��es para calcular o tempo
DATA: 12/Agosto/2024
Autor: Elgio Schlemer

12/8/2024 - Abandono do gettimeofday para usar a fun��o clock que
� padr�o C ANSI. 
*/

#ifndef __TEMPO__
/* Sempre que se cria uma biblioteca � prudente usar um define para ela.
 * Veja, as defini��es abaixo s� ocorrer�o se N�O HOUVER AINDA a constante
 * __TEMPO__. Isto evita erros com duplas inclus�es, ou seja, dois ou mais
 * #include "tempo.h". Apenas o primeiro ter� efeito e os demais nada
 * definir�o. Todos os .h deveriam usar isto.
 * */
#define __TEMPO__

/* 12/8 Maravilha. Agora de um jeito s� para Linux e Windows. 
 * Testado com sucesso em:
 * - Windows XP 32 bits com Dev++
 * - Windows XP 32 bits com Codeblocks
 * - Linux 64 bits
 * */
 
#include <time.h>

/* para muitos c�digos, um inteiro longo sem sinal � o ideal.
Se for um compilador de 32 bits, isto resultar� em um inteiro
de 32 bits. Por�m se for um compilador de 64 bits, ser� um inteiro
de 64 bits.

Crio um typedef pois � muita coisa ficar digitando unsigned long int
Assim, s� se coloca ulong
*/
typedef unsigned long int ulong;

/* uma fun��o para medir o tempo.
 * Ela retorna a quantidade de microsegundos que se passaram
 * desde a �ltima vez que a mesma fun��o foi chamada.
 *  
 * Em 24 de agosto de 2018 ela passou a ser a mesma para Linux e para Windows, 
 * pois o problema � que no
 * Windows n�o tinha a fun��o gettimeofday, mas agora tem uma implementa��o
 * para Windows no in�cio deste c�digo
*/
ulong tempo()
{
    static clock_t ti, tf;
    static int vezes = 0;
   
    ulong ms;
    
    if (vezes == 0) {
        /* Primeira invoca��o */
        vezes = 1;
        ti = clock();
        /* Clock � ANSI e retorna quantos ciclos de CPU se passaram 
         * desde o in�cio do programa. O padr�o POSIX, segundo manual
         * do clock, estabelece que 1s tem 1.000.000 de clocks independente
         * do sistema. Sendo isso verdade (que � setado pela constante CLOCKS_PER_SEC)
         * ent�o o retorno de clock acaba j� sendo em microssegundos.
         */
        return (0);
    }

/* pega o tempo atual. Funcao para LINUX */
    tf = clock();
		
	ms = (tf - ti);
	
	ti = tf;
    
    vezes++;
    return (ms);
}


/* Retorna uma string com o tempo formatado em  seg,  mseg e useg */
char *formata(ulong m)
{
    static char tempo[30];
    ulong s, ms, us;
    s = m / 1000000;
    ms = (m % 1000000) / 1000;
    us = (m % 1000);
    sprintf(tempo, "%02lus %03lums %03luus", s, ms, us);
    return (tempo);
}
#endif

