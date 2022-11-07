#ifndef FONCTION_H
#define FONCTION_H
#include <errno.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

int sem_create(key_t cle, int initval);
void P(int semid);
void V(int semid);
void sem_delete(int semid);

#endif