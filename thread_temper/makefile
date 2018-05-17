temper: get_temperature.o pcthread.o writedb.o
	gcc -o temper get_temperature.o pcthread.o writedb.o -lwiringPi -pthread -lmysqlclient

get_temperature.o: get_temperature.c
	gcc -O -c get_temperature.c

pcthread.o: pcthread.c
	gcc -O -c pcthread.c

writedb.o: writedb.c
	gcc -O -c writedb.c

clean:
	rm -f get_temperature.o pcthread.o writedb.o temper
