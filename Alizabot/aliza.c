// The original code in C for ALIZA UNFINISHED
// By Rafael Sanchez

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define MAXBUF 2048

int conv_ended = 0;

// Structure of a category with 1 pattern and multiple replies
typedef struct
{
    char pattern[MAXBUF];
    char replies[MAXBUF][MAXBUF];
} Category;

void flushArr(char array[], int len)
{
    for (int i = 0; i < len; i++)
    {
        array[i] = '\0';
    }
}

// reverses a string
char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

// turns strings to lowercase provided in buffer
void string_to_lowercase(char buf[], int length)
{
    for (int i = 0; i < length; i++)
    {
        buf[i] = tolower(buf[i]);
    }
}

// searches if a character is in an array
int is_elem(char c, char str[], int len)
{
    for (int i = 0; i < len; i++)
    {
        if (str[i] == c)
        {
            return 1;
        }
    }
    return 0;
}

// removes leading spaces
void removeLeadingSpaces(char *str, int len)
{
    char str1[len];
    int count = 0, j, k;

    while (str[count] == ' ')
    {
        count++;
    }

    for (j = count, k = 0;
         str[j] != '\0'; j++, k++)
    {
        str1[k] = str[j];
    }
    str1[k] = '\0';

    for (int i = 0; i < len; i++)
    {
        str[i] = str1[i];
    }
}

// removes trailing spaces
void removeTrail(char *str, int len)
{
    int count = 0;
    int i = 0;
    while (i < len)
    {
        if (isspace(str[i]) && (count == 0))
        {
            count++;
        }
        else if (isspace(str[i]) && (count == 1))
        {
            str[i - 1] = '\0';
            return;
        }
        else
        {
            count = 0;
        }
        i++;
    }
}

// replaces . ? ! ' " , of a string, with empty string
void getRoot(char buf[], int len)
{
    char new_buf[len];
    int j = 0;
    for (int i = 0; i < len; i++)
    {

        if ((buf[i] == '.') || (buf[i] == '!') || (buf[i] == '?') || (buf[i] == ',') || (buf[i] == '\'') || (buf[i] == '"') || (buf[i] == '#') || (buf[i] == '$') || (buf[i] == '*') || (buf[i] == '+'))
        {
            continue;
        }
        else
        {
            new_buf[j] = buf[i];
            j++;
        }
    }
    j++;
    new_buf[j] = '\0';
    strcpy(buf, new_buf);
}

// important for pattern matching
int wildCmp(char *pattern, char *string)
{
	if(*pattern=='\0' && *string=='\0')
		return 1;
		
	if(*pattern=='?' || *pattern==*string)
		return wildCmp(pattern+1,string+1);
		
	if(*pattern=='*') 
		return wildCmp(pattern+1,string) || wildCmp(pattern,string+1);
		
	return 0;
}

// parses the text file, writing all the categories to the array cats
void parser(char filename[], Category cats[])
{
    return;
}

// stores in reply what aliza will say to the user
void aliza_says(char input[], char reply[], int input_len)
{
    // COMMANDS SECTION
    if (strstr(input, "repeat"))
    {
        for (int i = 0; i < input_len; i++)
        {
            if (((input[i] == 'r') && (i == 0)))
            {
                continue;
            }
            else if ((!(input[i] == 'r') && (i == 0)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == 'e') && (i == 1)))
            {
                continue;
            }
            else if ((!(input[i] == 'e') && (i == 1)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == 'p') && (i == 2)))
            {
                continue;
            }
            else if ((!(input[i] == 'p') && (i == 2)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == 'e') && (i == 3)))
            {
                continue;
            }
            else if ((!(input[i] == 'e') && (i == 3)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == 'a') && (i == 4)))
            {
                continue;
            }
            else if ((!(input[i] == 'a') && (i == 4)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == 't') && (i == 5)))
            {
                continue;
            }
            else if ((!(input[i] == 't') && (i == 5)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else if (((input[i] == ' ') && (i == 6)))
            {
                continue;
            }
            else if ((!(input[i] == ' ') && (i == 6)))
            {
                strcpy(reply, "I can repeat whatever you say! Just say: repeat <text>");
                return;
            }
            else
            {
                char str[1];
                str[0] = input[i];
                strcat(reply, str);
            }
        }
    }
    else if (input_len == 0)
    {
        // call parser on the no responses brain0.txt
    }
    else
    {
        // parse the txt
    }
}

// main function
int main()
{
    printf("\n");
    printf("*************************** ALIZA CHATBOT ***************************\n");
    printf("*********************** By Rafael Sanchez ***************************\n");
    printf("***************** To stop Aliza, type bye ***************************\n");
    printf("\n");
    printf("-------------------- CONVERSATION STARTED ---------------------------\n");
    printf("\n");

    // call parser on the greets

    while (1)
    {
        char *reply = calloc(MAXBUF, sizeof(char));
        char input[MAXBUF];
        printf("User: ");
        fgets(input, MAXBUF, stdin);
        removeLeadingSpaces(input, strlen(input));
        removeTrail(input, strlen(input));
        getRoot(input, strlen(input));
        string_to_lowercase(input, strlen(input));
        removeLeadingSpaces(input, strlen(input));
        removeTrail(input, strlen(input));
        input[strlen(input)] = '\0';
        aliza_says(input, reply, strlen(input));
        printf("Aliza: %s\n", reply);
        free(reply);
        if (conv_ended==1)
        {
            break;
        }
    }
    printf("\n");
    printf("-------------------- CONVERSATION ENDED -----------------------------\n");
    printf("\n");
    return 0;
}
