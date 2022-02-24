#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAXBUF 2048
#define NUMBEROFGREET 14

// Turns strings to lowercase provided in buffer
void string_to_lowercase(char *buf, size_t length)
{
    for (size_t i = 0; i < length; i++)
    {
        buf[i] = tolower(buf[i]);
    }
}

const char *aliza_says(char input[])
{
    return "TO DO";
}

int main()
{
    printf("\n");
    printf("*************************** ALIZA CHATBOT ***************************\n");
    printf("*********************** By Rafael Sanchez ***************************\n");
    printf("***************** To stop Aliza, type bye ***************************\n");
    printf("\n");
    printf("-------------------- CONVERSATION STARTED ---------------------------\n");
    printf("\n");
    
    char greetings[NUMBEROFGREET][MAXBUF] = {"Hey there...", "How do you do?", "How have you been?", "Hello there.", "Hi!", "How are you doing?", "How's it going?", "It's great to see you.", "What's up?", "Yo!", "Lovely to see you.", "Ahoy!", "Heyo.", "HOLA."};
    printf("Aliza: %s\n", greetings[rand() % NUMBEROFGREET]);

    while (1)
    {
        char input[MAXBUF];
        printf("User: ");
        // use fgets to parse the user input
        printf("Aliza: %s\n", aliza_says(input));
        string_to_lowercase(input, strlen(input));
        if (strcmp(input, "bye") == 0)
        {
            break;
        }
    }
    printf("\n");
    printf("-------------------- CONVERSATION ENDED -----------------------------\n");
    printf("\n");
    return 0;
}
