// Implementation of Binary Search Algorithm

#include <stdio.h>


int binary_search(int arr[], int n, int target)
{
    int low = 0;
    int high = n-1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
        {
            return mid;
        }
        if (arr[mid] < target)
        {
            low = mid + 1;
        }
        else 
        {
            high = mid - 1;
        }
    }
    return -1;
}

int main()
{
    int arr[] = {44, 23, 192, 223, 513, 25};
    int n = sizeof(arr)/sizeof(arr[0]);

    int target = 513;
    printf("Element %d found at index %d\n", target, binary_search(arr, n, target));
}
