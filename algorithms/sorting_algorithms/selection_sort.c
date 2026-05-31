#include <stdio.h>

void select_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min])
                min = j;
        }
        
        if (min != i)
        {
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}

void print_array(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {12, 88, 21, 13, 74};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    print_array(arr, n);
    
    select_sort(arr, n);
    
    printf("Sorted array:   ");
    print_array(arr, n);
    
    return 0;
}