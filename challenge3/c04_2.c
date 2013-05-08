#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define BSIZE 1024



int main(){
    FILE *fr = fopen("integers", "rb");
    unsigned char count[(1<<15)*7];  // I don't even care about memory...

    unsigned int buf[BSIZE]; // Buffer to read in big chunks

    unsigned int i, j, l, read_len, tmp, block, index, ls;
    printf("Reading...\n");

    for (j=0; j<7; j++) {
        for (i = 0; i < (1<<15); i++) {
            count[j + i*7] = 0;
        }
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
            block = tmp>>15;
            if(block <=3 || block >= 65533){
                index = block<=3?block:block-65529;
                ls = tmp&0x7fff;
                count[index + ls*7]++;
            }
        }
        if(i%(1<<24) == 0){
            printf("progress = %f%%\n", (((float)i)/l)*100);
        }
    }
    printf("termina o ke ase\n");

    for (j=0; j<7; j++) {
        for (i = 0; i < (1<<15); i++) {
            if(count[j + i*7] != 1){
                printf("%d\n", ((j<=3?j:j+65529)<<15) | i );
            }
        }
    }

    return 0;
}


