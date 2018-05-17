#include "thread_temp.h"
#define MAX 100

int buffer[MAX];
int fill_ptr = 0;
int use_ptr = 0;
int count = 0;
int loops = 10;

pthread_cond_t empty, fill;
pthread_mutex_t mutex;

int main(int argc, char *argv[]){
	printf("main start\n");
	pthread_t p,c;
	
	pthread_create(&c, NULL, producer, NULL);
	pthread_create(&p, NULL, consumer, NULL);

	pthread_join(c, NULL);
	pthread_join(p, NULL);

	printf("main end\n");
	return 0;
}

void put(int value){
	buffer[fill_ptr] = value;
	fill_ptr = (fill_ptr+1)%MAX;
	count++;
}

int get(){
	int tmp = buffer[use_ptr];
	use_ptr = (use_ptr+1)%MAX;
	count--;
	return tmp;
}


void *producer(void *arg){
	int i;
	for (i=0; i<loops; i++){
		pthread_mutex_lock(&mutex);
		while(count==MAX){
			printf("producer waiting\n");
			pthread_cond_wait(&empty, &mutex);
		}
		put(get_temp());
		pthread_cond_signal(&fill);
		pthread_mutex_unlock(&mutex);
		sleep(3);
	}
}

void *consumer(void *arg){
	int i,tmp;
	for(i=0; i<loops; i++){
		pthread_mutex_lock(&mutex);
		while(count == 0){
			printf("consumer waiting\n");	
			pthread_cond_wait(&fill, &mutex);
		}
		tmp = get();
		printf("consumer get temp : %d\n", tmp);
		send_db(tmp);
		pthread_cond_signal(&empty);
		pthread_mutex_unlock(&mutex);
		printf("%d\n", tmp);
	}
}
