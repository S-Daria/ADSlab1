from random import random, choice
from time import time
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort import shell_sort

N = pow(2, 7)
po = 7

selection_stats = {
    "random_time" : [],
    "random_compares" : [],
    "incr_time" : [],
    "incr_compares" : [],
    "decr_time" : [],
    "decr_compares" : [],
    "same_time" : [],
    "same_compares": []
}
insertion_stats = {
    "random_time" : [],
    "random_compares" : [],
    "incr_time" : [],
    "incr_compares" : [],
    "decr_time" : [],
    "decr_compares" : [],
    "same_time" : [],
    "same_compares": []
}
shell_stats = {
    "random_time" : [],
    "random_compares" : [],
    "incr_time" : [],
    "incr_compares" : [],
    "decr_time" : [],
    "decr_compares" : [],
    "same_time" : [],
    "same_compares": []
}
merge_stats = {
    "random_time" : [],
    "random_compares" : [],
    "incr_time" : [],
    "incr_compares" : [],
    "decr_time" : [],
    "decr_compares" : [],
    "same_time" : [],
    "same_compares": []
}
# creating file & starting the experiment
#with open("experiments.txt", 'w', encoding='utf-8') as file: 

print("start experiment:\n\n")

while po != 16:
    # creating the arrays
    print("generating massives ... ", end='')
    rand_repeat = 5
    rand_arrays = [[random() for i in range(N)] for j in range(rand_repeat)]
    incr_repeat = 1
    incr_array = [i for i in range(N)]
    decr_repeat = 1
    decr_array = [i for i in reversed(range(N))]
    same_repeat = 3
    same_arrays = [[choice([1, 2, 3]) for i in range(N)] for j in range(same_repeat)]
    
    print("generated")


    #******************** SELECTION SORT ****************************** 

    print("*" * 20)
    print(f"\nselection sort (pow = {po})...\n")
    
    #************************

    took = 0
    compares = 0
    print("rand array ... ")
    for i in range(rand_repeat):
        rand_array = rand_arrays[i]
        start = time()
        compares += selection_sort(rand_array.copy())
        took += time() - start
    print(f"time: {took/rand_repeat} ... ")
    selection_stats["random_time"].append(took/rand_repeat)
    print(f"compares: {compares/rand_repeat}\n")
    selection_stats["random_compares"].append(compares/rand_repeat)

    #************************

    took = 0
    compares = 0
    print("inсreasing array ... ")
    for _ in range(incr_repeat):
        start = time()
        compares += selection_sort(incr_array.copy())
        took += time() - start
    print(f"time: {took/incr_repeat} ... ")
    selection_stats["incr_time"].append(took/incr_repeat)
    print(f"compares: {compares/incr_repeat}\n")
    selection_stats["incr_compares"].append(compares/incr_repeat)

    #************************

    took = 0
    compares = 0
    print("deсreasing array ... ")
    for _ in range(decr_repeat):
        start = time()
        compares += selection_sort(decr_array.copy())
        took += time() - start
    print(f"time: {took/decr_repeat} ... ")
    selection_stats["decr_time"].append(took/decr_repeat)
    print(f"compares: {compares/decr_repeat}\n")
    selection_stats["decr_compares"].append(compares/decr_repeat)

    #************************

    took = 0
    compares = 0
    print("repetitive array ... ")
    for i in range(same_repeat):
        same_array = same_arrays[i]
        start = time()
        compares += selection_sort(same_array.copy())
        took += time() - start
    print(f"time: {took/same_repeat} ... ")
    selection_stats["same_time"].append(took/same_repeat)
    print(f"compares: {compares/same_repeat}\n")
    selection_stats["same_compares"].append(compares/same_repeat)


    #******************** INSERTION SORT ****************************** 

    print("*" * 20)
    print(f"\ninsertion sort (pow = {po})...\n")
    
    #************************

    took = 0
    compares = 0
    print("rand array ... ")
    for i in range(rand_repeat):
        rand_array = rand_arrays[i]
        start = time()
        compares += insertion_sort(rand_array.copy())
        took += time() - start
    print(f"time: {took/rand_repeat} ... ")
    insertion_stats["random_time"].append(took/rand_repeat)
    print(f"compares: {compares/rand_repeat}\n")
    insertion_stats["random_compares"].append(compares/rand_repeat)

    #************************

    took = 0
    compares = 0
    print("inсreasing array ... ")
    for _ in range(incr_repeat):
        start = time()
        compares += insertion_sort(incr_array.copy())
        took += time() - start
    print(f"time: {took/incr_repeat} ... ")
    insertion_stats["incr_time"].append(took/incr_repeat)
    print(f"compares: {compares/incr_repeat}\n")
    insertion_stats["incr_compares"].append(compares/incr_repeat)

    #************************

    took = 0
    compares = 0
    print("deсreasing array ... ")
    for _ in range(decr_repeat):
        start = time()
        compares += insertion_sort(decr_array.copy())
        took += time() - start
    print(f"time: {took/decr_repeat} ... ")
    insertion_stats["decr_time"].append(took/decr_repeat)
    print(f"compares: {compares/decr_repeat}\n")
    insertion_stats["decr_compares"].append(compares/decr_repeat)

    #************************

    took = 0
    compares = 0
    print("repetitive array ... ")
    for i in range(same_repeat):
        same_array = same_arrays[i]
        start = time()
        compares += insertion_sort(same_array.copy())
        took += time() - start
    print(f"time: {took/same_repeat} ... ")
    insertion_stats["same_time"].append(took/same_repeat)
    print(f"compares: {compares/same_repeat}\n")
    insertion_stats["same_compares"].append(compares/same_repeat)


    #******************** MERGE SORT ****************************** 

    print("*" * 20)
    print(f"\nmerge sort (pow = {po})...\n")
    
    #************************

    took = 0
    compares = 0
    print("rand array ... ")
    for i in range(rand_repeat):
        rand_array = rand_arrays[i]
        start = time()
        compares += merge_sort(rand_array.copy())
        took += time() - start
    print(f"time: {took/rand_repeat} ... ")
    merge_stats["random_time"].append(took/rand_repeat)
    print(f"compares: {compares/rand_repeat}\n")
    merge_stats["random_compares"].append(compares/rand_repeat)

    #************************

    took = 0
    compares = 0
    print("inсreasing array ... ")
    for _ in range(incr_repeat):
        start = time()
        compares += merge_sort(incr_array.copy())
        took += time() - start
    print(f"time: {took/incr_repeat} ... ")
    merge_stats["incr_time"].append(took/incr_repeat)
    print(f"compares: {compares/incr_repeat}\n")
    merge_stats["incr_compares"].append(compares/incr_repeat)

    #************************

    took = 0
    compares = 0
    print("deсreasing array ... ")
    for _ in range(decr_repeat):
        start = time()
        compares += merge_sort(decr_array.copy())
        took += time() - start
    print(f"time: {took/decr_repeat} ... ")
    merge_stats["decr_time"].append(took/decr_repeat)
    print(f"compares: {compares/decr_repeat}\n")
    merge_stats["decr_compares"].append(compares/decr_repeat)

    #************************

    took = 0
    compares = 0
    print("repetitive array ... ")
    for i in range(same_repeat):
        same_array = same_arrays[i]
        start = time()
        compares += merge_sort(same_array.copy())
        took += time() - start
    print(f"time: {took/same_repeat} ... ")
    merge_stats["same_time"].append(took/same_repeat)
    print(f"compares: {compares/same_repeat}\n")
    merge_stats["same_compares"].append(compares/same_repeat)

    #******************** SHELL SORT ****************************** 

    print("*" * 20)
    print(f"\nshell sort (pow = {po})...\n")
    
    #************************

    took = 0
    compares = 0
    print("rand array ... ")
    for i in range(rand_repeat):
        rand_array = rand_arrays[i]
        start = time()
        compares += shell_sort(rand_array.copy())
        took += time() - start
    print(f"time: {took/rand_repeat} ... ")
    shell_stats["random_time"].append(took/rand_repeat)
    print(f"compares: {compares/rand_repeat}\n")
    shell_stats["random_compares"].append(compares/rand_repeat)

    #************************

    took = 0
    compares = 0
    print("inсreasing array ... ")
    for _ in range(incr_repeat):
        start = time()
        compares += shell_sort(incr_array.copy())
        took += time() - start
    print(f"time: {took/incr_repeat} ... ")
    shell_stats["incr_time"].append(took/incr_repeat)
    print(f"compares: {compares/incr_repeat}\n")
    shell_stats["incr_compares"].append(compares/incr_repeat)

    #************************

    took = 0
    compares = 0
    print("deсreasing array ... ")
    for _ in range(decr_repeat):
        start = time()
        compares += shell_sort(decr_array.copy())
        took += time() - start
    print(f"time: {took/decr_repeat} ... ")
    shell_stats["decr_time"].append(took/decr_repeat)
    print(f"compares: {compares/decr_repeat}\n")
    shell_stats["decr_compares"].append(compares/decr_repeat)

    #************************

    took = 0
    compares = 0
    print("repetitive array ... ")
    for i in range(same_repeat):
        same_array = same_arrays[i]
        start = time()
        compares += shell_sort(same_array.copy())
        took += time() - start
    print(f"time: {took/same_repeat} ... ")
    shell_stats["same_time"].append(took/same_repeat)
    print(f"compares: {compares/same_repeat}\n")
    shell_stats["same_compares"].append(compares/same_repeat)

    N *= 2
    po += 1
print("\n\n")
print(str(insertion_stats))
print("\n\n")
print(str(merge_stats))
print("\n\n")
print(str(selection_stats))
print("\n\n")
print(str(shell_stats))