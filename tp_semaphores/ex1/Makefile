CFLAGS=-Wall -Wextra -g

TARGETS=toto

all: $(TARGETS)

main: T1 T2

T1: T1.o fonction.o
	gcc $^ -o $@ $(LIBS)

T2: T2.o fonction.o
	gcc $^ -o $@ $(LIBS)

T1.o: fonction.h T1.c

T2.o: fonction.h T2.c

fonction.o: fonction.h fonction.c

clean:
	rm *.o $(TARGETS)