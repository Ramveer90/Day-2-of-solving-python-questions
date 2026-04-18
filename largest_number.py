# find largest number


#Logic
nums = [10, 20, 30, 40, 50, 60]
largest = nums[0]
for num in nums:
      if num > largest:
           largest = num
print(largest)



# function

def largest_num(nums_list: list[float]) -> float:
    if not isinstance(nums_list, list):
        raise TypeError("Input must be a list")

    if not nums_list:
        raise ValueError("List cannot be empty")

    for num in nums_list:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")

    largest = nums_list[0]

    for num in nums_list:
        if num > largest:
            largest = num

    return largest


if __name__ == "__main__":
    try:
        user_input = input("Enter numbers (space separated): ")
        number_list = [float(item) for item in user_input.split()]

        result = largest_num(number_list)
        print("Largest number is:", result)

    except Exception as e:
        print("Error:", e)