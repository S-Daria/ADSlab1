# public class Selection
# {
#     public static void sort(Comparable[] a)
#         { // Sort a[] into increasing order.
#         int N = a.length; // array length
#         for (int i = 0; i < N; i++)
#             { // Exchange a[i] with smallest entry in a[i+1...N).
#                 int min = i; // index of minimal entr.
#                 for (int j = i+1; j < N; j++)
#                     if (less(a[j], a[min])) min = j;
#                 exch(a, i, min);
#             }
#         }
#     // See page 245 for less(), exch(), isSorted(), and main().
# }

def selection_sort(arr):
    compares = 0
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
            compares += 1
        arr[i], arr[mini] = arr[mini], arr[i]
    return compares

