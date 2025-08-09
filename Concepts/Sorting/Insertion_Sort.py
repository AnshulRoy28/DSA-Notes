
def insertion_sort(arr):
    """
    Sorts a given list of numbers in ascending order using the Insertion Sort algorithm.
    Input:
        arr (list): A list of numbers to be sorted.

    Output:
        None-The list is sorted in place (the original list is modified).
    
    Purpose:
        Insertion sort works by building a sorted portion of the list one element at a time.
        For each element, it is compared with elements in the sorted part and inserted in the correct position.
    """
    #If array is empty or it has only one element just return 
    if arr==None or len(arr)==1:
        return 
    
    # We assume the first element is already sorted so we loop ahead
    for i in range(1,len(arr)):
        key=arr[i]          #element we want to place in correct position
        j=i-1               #Start comparison from previous element 

        #Shift elements that are already sorted if they are greater than key
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j] #right shift
            j-=1            #move left one step

        #Placing key in correct position
        arr[j+1]=key

#Example usage
arr=[1,4,3,5,2,3]
insertion_sort(arr)
print(arr)

'''
Java Version 
import java.util.*;

public class InsertionSorting {

    public static void insertionSort(int[] arr) {
        if (arr == null || arr.length == 1) {
            return;
        }
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            // Placing/Inserting the current key at the right place
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = { 43, 21, 44, 12, 5, 10, 2, 5, 90 };

        for (int ele : arr) {
            System.out.print(ele + " ");
        }

        insertionSort(arr);

        System.out.println();
        for (int ele : arr) {
            System.out.print(ele + " ");
        }
    }
}
'''