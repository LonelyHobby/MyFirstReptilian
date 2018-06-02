for num in range(100, 1000):
    if num % 37 == 0:
        num_new_1 = num % 100 *10 + num // 100
        num_new_2 = num % 10 * 100 + num // 10
        if num_new_1 % 37 != 0 or num_new_1 % 37 != 0:
            print("It's a false proposition.")
            break
else:
    print("It's a true proposition.")
