def merge(arr,low,mid,high):
    """
    Input:
        arr (list): The list of numbers being sorted.
        low (int): Starting index of the left half.
        mid (int): Ending index of the left half (midpoint).
        high (int): Ending index of the right half.

    Output:
        None - The function modifies the array in place.

    Purpose:
        The merge step takes two sorted subarrays:
            - Left half: arr[low..mid]
            - Right half: arr[mid+1..high]
        and merges them into a single sorted segment in arr[low..high].
    """
    
    temp=[]                         #temporary list to store the merged elements
    
    left=low                        #Startingg index of left half
    right=mid+1                     #Starting index of right half

    #sort elements and store in temp[]
    while left<=mid and right <=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
    #If elements remain in left half
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    #If elements remain in right half
    while right <=high:
        temp.append(arr[right])
        right+=1

    #Store everything from temp into the arr
    for i in range(low,high+1):
        arr[i]=temp[i-low]

def merge_sort(arr,low,high):
    """
    Input:
        arr (list): A list of numbers to be sorted.
        low (int): The starting index of the portion of the list to be sorted.
        high (int): The ending index of the portion of the list to be sorted.

    Output:
        None - The list is sorted in place

    Purpose:
        Merge Sort is recursive a divide-and-conquer algorithm that:
            1. Divides the array into two halves until each subarray has one element.
            2. Merges these smaller sorted arrays back together to form a fully sorted array.
    """

    #Basecase if subarray only has one element its sorted
    if low>=high:
        return 
    #get the middle element
    mid=(low+high)//2

    #Divide
    merge_sort(arr,low,mid)         #Sorting left half
    merge_sort(arr,mid+1,high)      #Sorting right half

    merge(arr,low,mid,high)

#Sample usage
arr=[1,5,4,3,7,6,2,4,5,9]
merge_sort(arr,0,len(arr)-1)
print(arr)


'''
Java version 

import java.util.*;

public class MergeSort {

    private static void merge(int[] arr, int low, int mid, int high) {
        ArrayList<Integer> temp = new ArrayList<>(); // Temporary array

        int left = low;      // Starting index of left half of arr
        int right = mid + 1; // Starting index of right half of arr

        // Storing elements in the temporary array in a sorted manner
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                temp.add(arr[left]);
                left++;
            } else {
                temp.add(arr[right]);
                right++;
            }
        }

        // If elements on the left half are still left
        while (left <= mid) {
            temp.add(arr[left]);
            left++;
        }

        // If elements on the right half are still left
        while (right <= high) {
            temp.add(arr[right]);
            right++;
        }

        // Transferring all elements from temporary to arr
        for (int i = low; i <= high; i++) {
            arr[i] = temp.get(i - low);
        }
    }

    public static void mergeSort(int[] arr, int low, int high) {
        if (low >= high) return;

        // Middle element
        int mid = (low + high) / 2;

        // Divide
        mergeSort(arr, low, mid);      // Left half
        mergeSort(arr, mid + 1, high); // Right half

        // Conquer
        merge(arr, low, mid, high);    // Merging sorted halves
    }

    public static void main(String[] args) {
        int[] arr = { 9, 4, 7, 6, 3, 1, 5 };

        System.out.println("Before sorting array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();

        mergeSort(arr, 0, arr.length - 1);

        System.out.println("After sorting array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
'''