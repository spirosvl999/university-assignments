#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
pthread_mutex_t the_mutex;
pthread_cond_t condh, condt, condwon, condwor;

#define NUMBER_OF_THREADS 10

void *thread_Hello(void *tid)
{
    printf("Hello");
    pthread_exit(NULL);
}

void *thread_there(void *tid)
{
    printf(" there");
    pthread_exit(NULL);
}

void *thread_wonderful(void *tid)
{
    printf(" wonderful");
    pthread_exit(NULL);
}

void *thread_world(void *tid)
{
    printf(" world! \n");
    pthread_exit(NULL);
}

int main()
{
    pthread_tthreads[NUMBER_OF_THREADS];
    int i, status;

        pthread_t hello, there, wonderful, world;
        pthread_create(&hello,NULL,thread_Hello,NULL);
        pthread_create(&there,NULL,thread_there,NULL);
        pthread_create(&wonderful,NULL,thread_wonderful,NULL);
        pthread_create(&world,NULL,thread_world,NULL);
        pthread_cond_init(&condh, NULL);
        pthread_cond_init(&condt, NULL);
        pthread_cond_init(&condwon, NULL);
        pthread_cond_init(&condwor, NULL);

    for(i=0; i < NUMBER_OF_THREADS; i++)
    {
        pthread_join(hello, NULL);
        pthread_join(there, NULL);
        pthread_join(wonderful, NULL);
        pthread_join(world, NULL);
    }
    pthread_cond_destroy(&condh);
    pthread_cond_destroy(&condt);
    pthread_cond_destroy(&condwon);
    pthread_cond_destroy(&condwor);
    pthread_mutex_destroy(&the_mutex);
}