#include <iostream>
using namespace std;

// Recursive linear search function
int LinearSearch(int arr[], int size, int target, int index = 0) {
    // Base case: if index reaches size, target not found
    if (index >= size) {
        return -1;
    }

    // Check current element
    if (arr[index] == target) {
        return index;
    }

    // Recursive call: move to next index
    return LinearSearch(arr, size, target, index + 1);
}

int main() {
    int arr[] = {2, 3, 4, 1, 56, 2, 8, 33, 7, 333};
    int size = sizeof(arr) / sizeof(arr[0]);

    int target;
    cout << "Enter the element to search: ";
    cin >> target;

    int result = LinearSearch(arr, size, target);

    if (result != -1) {
        cout << "Element " << target << " found at index " << result << endl;
    } else {
        cout << "Element " << target << " not found in the array" << endl;
    }

    return 0;
}