// Implementation of Bubble Sort

#include <stdio.h>

void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void print_array(int arr[], int n)
{
    printf("[");
    for (int i = 0; i < n; i++)
    {
        printf("%d", arr[i]);
        if (i < n-1)
        {
            printf(",");

        }
    }
    printf("]");
}


int main()
{
    int arr[] = {101, 21, 44, 32, 47, 2};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Before sorting: ");
    print_array(arr, n);

    bubble_sort(arr, n);

    printf("\nAfter bubble sorting: ");
    print_array(arr, n);
    printf("\n");
}