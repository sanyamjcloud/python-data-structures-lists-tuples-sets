#include <iostream>
using namespace std;

int LinearSearch(int arr[], int size, int target, int index) {
    if (index >= size) {
        return -1;
    }

    if (arr[index] == target) {
        return index;
    }

    return LinearSearch(arr, size, target, index + 1);
}

int main() {
    int arr[] = {2, 3, 4, 1, 56, 2, 8, 33, 7, 333};
    int size = sizeof(arr) / sizeof(arr[0]);

    int target;
    cin >> target;

    int result = LinearSearch(arr, size, target, 0);
    cout << result;

    return 0;
}
