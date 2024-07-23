#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int x;
    printf("Digite um valor\n");
    scanf("%i", &x);

    // Teste l√≥gico

    if (x % 2 == 0) {
        printf("Par!");
    }
    else {
        printf("Õmpar!");
    }


    return 0;
}