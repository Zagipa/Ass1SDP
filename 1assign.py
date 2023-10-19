class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Bubble Sort")
        return sorted(data)

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using Quick Sort")
        return sorted(data)

class SorterContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

if __name__ == "__main__":
    data = [5, 1, 3, 9, 2, 6]

    bubble_sorter = SorterContext(BubbleSort())
    bubble_sorted_data = bubble_sorter.sort_data(data)

    quick_sorter = SorterContext(QuickSort())
    quick_sorted_data = quick_sorter.sort_data(data)

    print("Original Data:", data)
    print("Bubble Sorted Data:", bubble_sorted_data)
    print("Quick Sorted Data:", quick_sorted_data)
