#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int x, y, res;
    printf("Digite um valor:\n");
    scanf("%i", &x);
    printf("Digite um valor:\n");
    scanf("%i", &y);

    res = x + y;
    printf("O resultado da soma de %i com %i é %i.",x, y, res);


    return 0;
}