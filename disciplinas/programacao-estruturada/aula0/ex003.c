#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");

    int val1, val2;
    char op;
    printf("Qual operação deseja fazer?\n");
    scanf("%c", &op);
    printf("Digite o primeiro valor:\n");
    scanf("%i", &val1);
    printf("Digite o segundo valor:\n");   
    scanf("%i", &val2);

    switch (op)
    {
    case '+': 
        printf("%i + %i = %i\n", val1, val2, val1 + val2);
        break;
    case '-': 
        printf("%i - %i = %i\n", val1, val2, val1 - val2);
        break;
    case '*':
        printf("%i * %i = %i\n", val1, val2, val1 * val2); 
        break;
    case '/': 
        printf("%i / %i = %i\n", val1, val2, val1 / val2);
        break;
    default:
        printf("Opção inválida!\n");
        break;
    }

    return 0;
}