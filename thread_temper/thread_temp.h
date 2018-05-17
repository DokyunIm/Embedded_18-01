#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <pthread.h>
#include <assert.h>
#include <stdint.h>
#include <errno.h>
#include <mysql/mysql.h>
#include <time.h>
#include <math.h>
#include <signal.h>

static uint8_t sizecvt(const int read);
int read_dht22_dat();
int get_temp();

int send_db(int temp);

void put(int value);
int get();
void *producer(void *arg);
void *consumer(void *arg);
