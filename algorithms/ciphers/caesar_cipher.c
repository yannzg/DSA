#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>


bool only_digits(const char *s);
char rotate(char c, int n);

int main(int argc, char *argv[])
{
    // Make sure program is run with just one command-line argument

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Make sure every character in the command-line argument is a digit
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert the command-line argument to an integer
    int n = atoi(argv[1]);

    // Prompt user for plaintext
    char plaintext[1024];
    printf("Plaintext: ");
    if (fgets(plaintext, sizeof(plaintext), stdin) == NULL)
    {
        printf("Error reading input.\n");
        return 1;
    }

    // Encipher entire plaintext
    printf("Ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        printf("%c", rotate(plaintext[i], n));
    }
    printf("\n");
    return 0;
}


// Function checking if command-line argument is an integer
bool only_digits(const char *s)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}


//Function to rotate a character
char rotate(char c, int n)
{
    if (!isalpha(c))
    {
        return c;
    }

    if (isupper(c))
    {
        return ((c - 'A' + n) % 26) + 'A';
    }
    else
    {
        return ((c - 'a' + n) % 26) + 'a';
    }
}
