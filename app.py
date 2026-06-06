def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def main():
    marks = [85, 90, 78, 92, 88]

    average = calculate_average(marks)

    print("Student Marks:", marks)
    print("Average Marks:", average)

    if average >= 80:
        print("Result: PASS")
    else:
        print("Result: FAIL")


if __name__ == "__main__":
    main()

