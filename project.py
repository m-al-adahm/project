def heapify(arr, n, i):
    largest = i  # اعتبر العنصر الحالي هو الأكبر
    left = 2 * i + 1  # الابن الأيسر
    right = 2 * i + 2  # الابن الأيمن

    # إذا كان الابن الأيسر أكبر من الجذر
    if left < n and arr[left] > arr[largest]:
        largest = left

    # إذا كان الابن الأيمن أكبر من الجذر
    if right < n and arr[right] > arr[largest]:
        largest = right

    # إذا تغيّر الجذر
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # التبديل
        # قم بترتيب الشجرة الفرعية المتأثرة
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # بناء الكومة (Heap) من المصفوفة
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # استخراج العناصر واحدًا تلو الآخر
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # التبديل
        heapify(arr, i, 0)