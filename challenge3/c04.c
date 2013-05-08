// Credit: To the StackOverflow answer that was in the front page
// of /r/programming a few months ago (I also readed it :)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define BSIZE 1024

int main(){
    FILE *fr = fopen("integers", "rb");
    uint16_t count[1<<16];

    unsigned int buf[BSIZE]; // Buffer to read in big chunks

    unsigned int i, j, l, read_len, tmp;
    printf("Reading...\n");

    for (i = 0; i < 1<<16; i++) {
        count[i] = 0;
    }

    i = 0;
    l = 2147483548;

    for (; i < l; i += BSIZE) {
        read_len = MIN(i+BSIZE,l) - i;

        if((fread(buf, 4, read_len, fr)) != read_len){
            printf("Error reading!\n");
            exit(1);
        }

        for (j = 0; j < read_len; j++) {
            tmp = buf[j];
            if(count[tmp >> 15 ] == 1<<16){
                printf("Full counter\n");
                exit(1);
            }
            count[tmp >> 15] ++;
        }
        if(i%(1<<24) == 0){
            printf("progress = %f%%\n", (((float)i)/l)*100);
        }
    }
    printf("termina o ke ase\n");

    for (i = 0; i < 1<<16; i++) {
        if(count[i] != 1<<15){
            printf("%d %d\n", i, (1<<15) - count[i]);
        }
    }

    return 0;
}


