def partition(arr,low,high):

    """
    Input:
        arr (list): The list of numbers to be sorted.
        low (int): The starting index of the portion of the list to be partitioned.
        high (int): The ending index of the portion of the list to be partitioned.

    Output:
        int: The partition index (point where the array is divided).

    Purpose:
        Partitioning step in QuickSort
        - Selects the middle element as the pivot.
        - Rearranges elements so that:
            * All elements less than pivot are on the left.
            * All elements greater than pivot are on the right.
    """
    #Take middle element as pivot 
    pivot=arr[low+(high-low)//2]
    i=low-1
    j=high+1

    while True:
        #i goes up until we find an element > the pivot
        while True:
            i+=1
            if arr[i]>=pivot:
                break

        #Decrement j until we find element <= pivot
        while True:
            j-=1
            if arr[j]<=pivot:
                break
        
        #If pointers meet return j (is partition index)
        if i>=j:
            return j
        
        #Swap arr[i] and arr[j]
        arr[i],arr[j]=arr[j],arr[i]

def quick_sort(arr,low,high):
    """
    Input:
        arr (list): A list of numbers to be sorted.
        low (int): The starting index of the portion of the list to be sorted.
        high (int): The ending index of the portion of the list to be sorted.
    Output:
        None - The list is sorted in place.
    Purpose:
        QuickSort is a recursive divide-and-conquer sorting algorithm that:
            1. Partitions the list into two halves around a pivot.
            2. Recursively sorts the left and right halves.
    """

    if low<high:
        #Partition the array and get the split index
        part=partition(arr,low,high)
        quick_sort(arr,low,part)
        quick_sort(arr,part+1,high)

arr=[9,4,3,2,5,2,5,7,5,34,7,86,33]
quick_sort(arr,0,len(arr)-1)
print(arr)

'''
Java Version
import java.util.*;

public class QuickSort {

    public static int partition(int[] arr, int low, int high) {
        // Choose the middle element as pivot
        int pivot = arr[low + (high - low) / 2];
        int i = low - 1;
        int j = high + 1;

        while (true) {
            // Increment i while arr[i] < pivot
            do {
                i++;
            } while (arr[i] < pivot);

            // Decrement j while arr[j] > pivot
            do {
                j--;
            } while (arr[j] > pivot);

            // If pointers cross, return j
            if (i >= j) {
                return j;
            }

            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Main function to sort an array using QuickSort
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // pi is the partitioning index
            int pi = partition(arr, low, high);

            // Recursively sort elements before and after partition
            quickSort(arr, low, pi);
            quickSort(arr, pi + 1, high);
        }
    }

    // To print an array
    public static void printArr(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // Driver Code
    public static void main(String[] args) {
        int[] arr = { 10, 7, 8, 9, 1, 5, 12 };

        System.out.println("Before Sorting:");
        printArr(arr);

        // Function call
        quickSort(arr, 0, arr.length - 1);

        System.out.println("After Sorting:");
        printArr(arr);
    }
}

'''