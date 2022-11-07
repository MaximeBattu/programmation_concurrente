CFLAGS=-Wall -Wextra -g

TARGETS=main

all: $(TARGETS)

main: T1 T2 T3 createSemaphores deleteSemaphores

T1: T1.o fonction.o
	gcc $^ -o $@ $(LIBS)

T2: T2.o fonction.o
	gcc $^ -o $@ $(LIBS)

T3: T3.o fonction.o
	gcc $^ -o $@ $(LIBS)

createSemaphores: createSemaphores.o fonction.o

deleteSemaphores: deleteSemaphores.o fonction.o

T1.o: fonction.h T1.c

T2.o: fonction.h T2.c

T3.o: fonction.h T3.c

fonction.o: fonction.h fonction.c

createSemaphores.o: fonction.h createSemaphores.c

deleteSemaphores.o: fonction.h deleteSemaphores.c

clean:
	rm *.o $(TARGETS)