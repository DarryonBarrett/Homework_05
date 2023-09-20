def print_operation_table(operation, num_rows=6, num_columns=6):
    for col in range(1, num_columns + 1):
        print(col, end=" ")
    print()

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(result, end=" ")
        print()

# Пример использования: умножение элементов таблицы
print_operation_table(lambda x, y: x * y)
