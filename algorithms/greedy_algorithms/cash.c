// Change making problem assuming only 4 coin types 

#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents
    int change;
    do
    {
        printf("Change owed: ");
        scanf("%i", &change);
    }
    while (change < 0);

    // number of quarters
    int n = 0;
    while (change >= 25)
    {
        change -= 25;
        n ++;
    }

    // number of dimes
    while (change >= 10)
    {
        change -= 10;
        n++;
    }

    // number of nickels
    while (change >= 5)
    {
        change -= 5;
        n ++;
    }

    // number of pennies
    while (change >= 1)
    {
        change -= 1;
        n ++;
    }

    printf("%i\n", n);
}
