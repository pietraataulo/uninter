#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");

    
    for(int x = 0; x <= 100; x++)
    {
        if (x % 2 == 0) 
        {
            printf("O n�mero %i � par!\n", x);
        }
        else 
        {
           printf("O n�mero %i � �mpar!\n", x);
        }
       
    }

    return 0;
}