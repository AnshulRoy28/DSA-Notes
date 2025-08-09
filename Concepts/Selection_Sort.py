def selection_sort(arr):
    """
    Input:
        arr (list): A list of numbers to be sorted.

    Output:
        None - The list is sorted in place (the original list is modified).

    Purpose:
        Selection Sort works by repeatedly selecting the smallest element from the 
        unsorted portion of the list and swapping it with the element at the current position.

    How it works:
        1. Assume the current position i is the smallest.
        2. Search the rest of the list (from i+1 to end) to find the actual smallest element.
        3. Swap the smallest found element with the element at position i.
        4. Move i one step forward and repeat until the array is fully sorted.
    Time complexity:
    O(N^2) in all cases
    """

    n=len(arr)
    for i in range(n-1):
        #Assume current index is the minimum
        min_index=i

        #Iterate through the rest of the list to find the index of minimum element 
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        
        #Swap the min index with the i'th index
        arr[i],arr[min_index]=arr[min_index],arr[i]
    
arr=[5,4,3,2,8,9]
selection_sort(arr)
print(arr)


'''
Java Version 
import java.util.*;

public class SelectionSort {

    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            // Assuming i index as minimum value index
            int min_index = i;

            // Finding the minimum value index
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min_index]) {
                    min_index = j;
                }
            }

            // Swapping the i index with the minimum value index
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = { 43, 21, 44, 12, 5, 10, 2, 90 };

        System.out.println("Before Sorting:");
        for (int ele : arr) {
            System.out.print(ele + " ");
        }
        System.out.println();

        selectionSort(arr);

        System.out.println("After Sorting:");
        for (int ele : arr) {
            System.out.print(ele + " ");
        }
    }
}

'''