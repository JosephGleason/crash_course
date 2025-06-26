def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []          # Start with an empty triangle
    triangle.append([1])   # First row is always [1]

    for i in range(1, n):                # For the next n-1 rows
        prev_row = triangle[i - 1]       # Get the previous row
        new_row = [1]                    # Start the new row with 1

        for j in range(1, len(prev_row)):
            value = prev_row[j - 1] + prev_row[j]
            new_row.append(value)

        new_row.append(1)               # End each row with 1
        triangle.append(new_row)        # Add the new row to the triangle

    return triangle
