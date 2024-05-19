#include <stdio.h>

int main() {
    int check[] = {110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125};
    int array[100]; // Assuming a maximum length for array
    int arrayIndex = 0;

    for (int i = 0; i < sizeof(check)/sizeof(check[0]); i++) {
        if (check[i] > 10) {
            array[arrayIndex] = check[i];
            arrayIndex++;
        }
    }

    // Printing characters
    for (int i = 0; i < arrayIndex; i++) {
        printf("%c", array[i]);
    }
    printf("\n");

    return 0;
}
