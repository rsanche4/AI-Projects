// The code in C for ALIZA UNFINISHED
// By Rafael Sanchez
//
// #TODO we have to implement the question of why do you say that random response
// #TODO add a ? or a . when returning from a +
// #TODO implement the + functionality
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <time.h>
#include <fnmatch.h>

#define FILENAME "brain.txt"
#define MAXBUF 2048
#define MAXREP 501
int conv_ended = 0;
time_t rawtime;
struct tm *timeinfo;

// Structure of a category with 1 pattern and multiple replies
typedef struct
{
    char pattern[MAXBUF];
    char replies[MAXREP][MAXBUF];
    int reply_count;
} Category;

// return how many lines are there in the brain, important for allocating the right memory block for category array
int len_brain(char filename[])
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    int count = 0;

    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        return -1;
    }

    while ((read = getline(&line, &len, fp)) != -1)
    {
        count++;
    }

    fclose(fp);
    if (line)
        free(line);
    return count;
}

// Swaps you words with I words and viceversa
void swaps()
{ // #TODO we have to implement this
    return;
}

// puts the null terminated character everywhere in an array
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

    if (!str || !*str)
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
    if (length <= 0)
    {
        return;
    }
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
    if (len <= 0)
    {
        return;
    }
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
    if (len <= 0)
    {
        return;
    }
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
    if (len <= 0)
    {
        return;
    }
    char new_buf[len];
    int j = 0;
    for (int i = 0; i < len; i++)
    {

        if ((buf[i] == '.') || (buf[i] == '!') || (buf[i] == '?') || (buf[i] == ',') || (buf[i] == '\'') || (buf[i] == '"') || (buf[i] == '#') || (buf[i] == '$') || (buf[i] == '*') || (buf[i] == '+') || (buf[i] == '-'))
        {
            continue;
        }
        else
        {
            new_buf[j] = buf[i];
            // printf("%c - %c\n", new_buf[j], buf[i]);
            j++;
        }
    }
    // j++;
    // printf("%d\n", j);
    new_buf[j] = '\0';
    // printf("%ld\n", strlen(new_buf));
    strcpy(buf, new_buf);
}

// important for pattern matching. returns 1 when found
// int wldcmp(char pattern[], char candidate[], int p, int c)
// {
//     //printf("%c - %c\n", pattern[p], candidate[c]);
//     if (pattern[p] == '\0')
//     {
//         return candidate[c] == '\0';
//     }
//     else if (pattern[p] == '*')
//     {
//         for (; candidate[c] != '\0'; c++)
//         {
//             if (wldcmp(pattern, candidate, p + 1, c))
//                 return 1;
//         }
//         return wldcmp(pattern, candidate, p + 1, c);
//     }
//     else
//     {
//         return wldcmp(pattern, candidate, p + 1, c + 1);
//     }
// }

// parses the text file, writing all the categories to the array cats. reply is an array of null terminated strings
void parser(Category cats[], char filename[], int total_lines)
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(FILENAME, "r");
    if (fp == NULL)
        return;

    int m = 0;
    while ((read = getline(&line, &len, fp)) != -1)
    {

        size_t n = strlen(line);
        line[n - 1] = '\0'; // change \n for \0
        int i = 0;
        int k = -1;
        int j = 0;
        int last_ind_q = 0;
        char question[MAXBUF];
        char reply[MAXREP][MAXBUF];
        int flag_que = 0;
        int flag_rep = 0;
        while (line[i] != '\0')
        {
            if (line[i] == '#')
            {
                flag_que = 1;
                i++;
                continue;
            }
            if (line[i] == '$')
            {
                if (k != -1)
                {
                    reply[k][j] = '\0';
                }
                flag_que = 0;
                flag_rep = 1;
                i++;
                k++;
                j = 0;
                continue;
            }
            if (flag_que)
            {
                question[j] = line[i];
                j++;
                last_ind_q = j;
            }
            if (flag_rep)
            {
                reply[k][j] = line[i];
                j++;
            }
            i++;
        }
        question[last_ind_q] = '\0';
        reply[k][j] = '\0';
        k++;
        reply[k][0] = '\0';

        strcpy(cats[m].pattern, question);
        int l = 0;
        while (reply[l][0] != '\0')
        {
            strcpy(cats[m].replies[l], reply[l]);
            cats[m].reply_count++;
            l++;
        }
        cats[m].replies[l][0] = '\0';
        m++;
    }

    fclose(fp);
    if (line)
        free(line);

    /* for (int i=0; i<total_lines;i++)
    {
     printf("#%s\n", cats[i].pattern);
     int ju = 0;
     while(cats[i].replies[ju][0]!='\0')
     {
         printf("$%s\n", cats[i].replies[ju]);
         ju++;
     }
    }*/
}

// stores one of the answers found randomly in buf to a given query. If it doesn't find anything, it returns -1. Else, it returns 0.
int category_finder(Category cats[], char query[], int total_cats, char buf[])
{
    // if (fnmatch("*you * fat", query, FNM_EXTMATCH))
    //     printf("HERE");
    // //printf("%s, %s\n", cats[56].pattern, query);
    // return 1;
    srand(time(NULL));
    int l = 0;
    while (l < total_cats)
    {
        if (strstr(query, cats[l].pattern))
        {
            strcpy(buf, cats[l].replies[rand() % cats[l].reply_count]);
            return 0;
        }
        else if (strstr(cats[l].pattern, "*"))
        {
            // #TODO more work
        }
        else if (strstr(cats[l].pattern, "+"))
        {
            // #TODO more work
        }
        l++;
    }
    return -1;
}

// stores in reply what aliza will say to the user. reply does not contain newline char
void aliza_says(char input[], char reply[], size_t input_len, int total_categories, Category cats[])
{
    // COMMANDS SECTION
    if (strstr(input, "repeat"))
    {
        for (size_t i = 0; i < input_len; i++)
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
                if (input[i] == '\0')
                {
                    strcat(reply, "\0");
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
    }
    else if (strstr(input, "say"))
    {
        // printf("%ld\n", input_len);
        for (size_t i = 0; i < input_len; i++)
        {
            if (((input[i] == 's') && (i == 0)))
            {
                continue;
            }
            else if ((!(input[i] == 's') && (i == 0)))
            {
                strcpy(reply, "I can say whatever you say! Just say: say <text>");
                return;
            }
            else if (((input[i] == 'a') && (i == 1)))
            {
                continue;
            }
            else if ((!(input[i] == 'a') && (i == 1)))
            {
                strcpy(reply, "I can say whatever you say! Just say: say <text>");
                return;
            }
            else if (((input[i] == 'y') && (i == 2)))
            {
                continue;
            }
            else if ((!(input[i] == 'y') && (i == 2)))
            {
                strcpy(reply, "I can say whatever you say! Just say: say <text>");
                return;
            }
            else if (((input[i] == ' ') && (i == 3)))
            {
                continue;
            }
            else if ((!(input[i] == ' ') && (i == 3)))
            {
                strcpy(reply, "I can say whatever you say! Just say: say <text>");
                return;
            }
            else
            {
                if (input[i] == '\0')
                {
                    strcat(reply, "\0");
                    return;
                }
                else
                {
                    // printf("%c - %ld\n", input[i], i);
                    char str[1];
                    str[0] = input[i];
                    strcat(reply, str);
                }
            }
        }
    }
    else if (input_len == 0)
    {
        category_finder(cats, "NORESP", total_categories, reply);
    }
    else
    {
        if (category_finder(cats, input, total_categories, reply) == -1)
        {
            flushArr(reply, strlen(reply));
            category_finder(cats, "NOTFOUND", total_categories, reply);
        }

        if (strstr(reply, "INSULT DETECTED"))
        {
            flushArr(reply, strlen(reply));
            category_finder(cats, "INSULT", total_categories, reply);
        }

        if (strstr(reply, "SALUTE MODE"))
        {
            flushArr(reply, strlen(reply));
            category_finder(cats, "SALUTE", total_categories, reply);
        }

        if (strstr(reply, "END IT"))
        {
            conv_ended = 1;
            flushArr(reply, strlen(reply));
            category_finder(cats, "FIN", total_categories, reply);
        }
    }
}

// main function
int main()
{
    printf("\n***************************\n");
    printf("ALIZA CHATBOT\n");
    printf("By Rafael Sanchez\n");
    printf("To stop talking to Aliza, say goodbye!\n");
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Conversation start: %s\n", asctime(timeinfo));

    // initialize the cats array
    int line_num = len_brain(FILENAME);
    if (line_num < 0)
    {
        printf("Error: Failed to open file '%s'.", FILENAME);
        return 1;
    }
    Category *cats = malloc(sizeof(Category) * line_num);
    if (cats == NULL)
    {
        printf("Error: malloc failed.\n");
    }
    parser(cats, FILENAME, line_num);
    // printf("%s", cats[0].pattern);
    //   call finder on the greets

    char *st = malloc(sizeof(char) * MAXBUF);
    category_finder(cats, "START", line_num, st);
    printf("%s\n", st);
    free(st);

    while (1)
    {
        char *reply = calloc(MAXBUF, sizeof(char));
        char input[MAXBUF];
        printf("> ");
        fgets(input, MAXBUF, stdin); // #TODO check if fgets failed, overflow, too long input
        size_t n = strlen(input);
        input[n - 1] = '\0';
        n = strlen(input);
        int c = 0;
        for (int ss = 0; ss < n; ss++)
        {
            if (input[ss] != ' ')
            {
                break;
            }
            else
            {
                c++;
            }
        }
        if (c == n)
        {
            input[0] = '\0';
            n = 0;
        }
        removeLeadingSpaces(input, n);
        removeTrail(input, n);
        getRoot(input, n);
        n = strlen(input);
        // printf("%s\n", input);
        // printf("%ld\n", strlen(input));
        string_to_lowercase(input, n);
        removeLeadingSpaces(input, n);
        removeTrail(input, n);
        // printf("%s\n", input);
        // printf("%ld\n", strlen(input));
        aliza_says(input, reply, n, line_num, cats);
        printf("%s\n", reply);
        free(reply);
        if (conv_ended == 1)
        {
            break;
        }
    }
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    free(cats);
    printf("\nConversation end: %s\n", asctime(timeinfo));
    return 0;
}
