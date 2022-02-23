#include <stdio.h>
#include <string.h>

#define MAXBUF 2048

const char* convert_to_lower(char buf[]) 
{
    return "TO DO\n";
}

const char* aliza_says(char input[]) 
{
    return "TO DO\n";
}

void start() 
{
    printf("To do\n");
}

int main() 
{
    printf("\n");
    printf("\n");
    printf("*************************** ALIZA CHATBOT ***************************\n");
    printf("*********************** By Rafael Sanchez ***************************\n");
    printf("***************** To stop Aliza, type Bye ***************************\n");
    printf("\n");
    printf("-------------------- Conversation Started ---------------------------\n");
    printf("\n");
    start();
    while (1) 
    {
        char input[MAXBUF];
        printf("User: ");
        scanf("%s", input);
        printf("Aliza: %s", aliza_says(input));
        if (strcmp(convert_to_lower(input),"bye")==0)
        {
            break;
        }
             
    }
    printf("\n");
    printf("-------------------- Conversation Ended -----------------------------\n");
    return 0;
}
