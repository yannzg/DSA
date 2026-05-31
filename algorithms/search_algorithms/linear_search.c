#include <stdio.h>


int linear_search(int arr[], int n, int target)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int arr[] = {21, 93, 18, 23, 99, 112, 666};
    int n = sizeof(arr) / sizeof(arr[0]);

    int target = 112;
    printf("Element %d found at index %d\n", target, linear_search(arr, n, target));

}