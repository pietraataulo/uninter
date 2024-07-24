#include <stdio.h>
#include <locale.h>

int ParImpar(int x);

int main(){
    setlocale(LC_ALL, "Portuguese");

    int valor, res; 
    printf("Digite um valor:\n");
    scanf("%i", &valor);
    res = ParImpar(valor);
    printf("%i", &res);


    return 0;
}

 int ParImpar(int x)
 {
      if (x % 2 == 0) 
        {
           return 1;
        }
        else 
        {
           return 0;
        }
       
 }