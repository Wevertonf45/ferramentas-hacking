#!/bin/bash

#Parar a execução ao apertar control C
trap "kill 0; exit 1" SIGINT


echo "Informe o domímio alvo: "
read dominio

for i in $(cat word-list.txt)
do
	host $i.$dominio
done
