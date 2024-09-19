import random
import time
from src.insertion_sort.sort import insertion_sort

# Do not change the following lines
def test_insertion_sort():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
    print("tests passed")

def test_reference():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sorted(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
    print("tests passed")

if __name__ == "__main__":
    N=100
    random.seed(int(time.time()))
    test_reference()