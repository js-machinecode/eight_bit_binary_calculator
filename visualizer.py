def visualize_add_bin(num1, num2):
    # Holds the carry from the previous column.
    # Starts at 0 because there is no carry before addition begins.
    carry = 0

    # Stores the binary answer as it is built.
    # We build it from right to left, so new bits are added 
    # to the front.
    result = ''

    # Visual representation of carry bits.
    # Starts as 8 blank spaces.
    # Example:
    # "   1 1  "
    carry_row = [' '] * 8

    print('Binary Addition Visualizer')

    # Pause so the user can begin when ready.
    input('\nPress Enter to start...')

    # Used to label each step.
    step = 1

    # Process bits from rightmost (index 7)
    # to leftmost (index 0).
    for bit in range(7, -1, -1):

        # Convert current characters ('0' or '1')
        # into integers for arithmetic.
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        # Add the two bits plus any carry from
        # the previous column.
        total = bit1 + bit2 + carry

        # Result bit is remainder when dividing by 2.
        #
        # Examples:
        # total = 0 -> result_bit = 0
        # total = 1 -> result_bit = 1
        # total = 2 -> result_bit = 0
        # total = 3 -> result_bit = 1
        result_bit = total % 2

        # Determine carry for next column.
        #
        # Examples:
        # total = 0 -> carry = 0
        # total = 1 -> carry = 0
        # total = 2 -> carry = 1
        # total = 3 -> carry = 1
        new_carry = total // 2

        # Add newest result bit to the FRONT
        # because we are moving right-to-left.
        result = str(result_bit) + result

        # If a carry was generated,
        # display it above the next column.
        if new_carry and bit > 0:
            carry_row[bit - 1] = '1'
        carry_display = ''.join(carry_row)

            
            

        # Print several blank lines to create
        # a simple animation effect.
        print('\n' * 3)

        print(f'Step {step}')

        # Show carry row.
        if new_carry and bit == 0:
            print(f'   1{carry_display:>8}')
        else:
            print(f'    {carry_display:>8}')
            
        # Show the two binary numbers.
        print(f'    {num1}')
        print(f'+   {num2}')

        # Divider line.
        print('------------')

        # Show partial result generated so far.
        print(f'    {result:>8}')

        # Save carry for next iteration.
        carry = new_carry

        # Move to next step number.
        step += 1

        # Wait for user before continuing.
        input('\nPress Enter for next step...')

    # After all 8 bits have been processed,
    # determine whether there is a final carry.
    if carry:

        # Create 9-bit answer.
        final_result = '1' + result

        print('\nFinal Answer:')
        print('This addition produced a 9-bit result.')
        print('The extra leftmost 1 is the final carry bit.\n')

    else:
        # Normal 8-bit result.
        final_result = result

        print('\nFinal Answer:')

    # Display final completed addition.
    print(f'    {num1:>9}')
    print(f'+   {num2:>9}')
    print('-------------')
    print(f'    {final_result:>9}')

def visualize_sub_bin(num1, num2):
    # Borrow coming into the current column.
    # Starts at 0 because no borrow exists initially.
    borrow = 0

    # Stores the binary answer as it is built.
    result = ''

    # Visual representation of borrows.
    # A '1' indicates that a borrow was taken
    # from that position.
    borrow_row = [' '] * 8

    print('Binary Subtraction Visualizer')

    # Wait for user before beginning.
    input('\nPress Enter to start...')

    # Step counter for display.
    step = 1

    # Process bits from rightmost to leftmost.
    for bit in range(7, -1, -1):

        # Convert current binary characters
        # into integers.
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        # Apply any borrow from the previous column.
        #
        # Example:
        # If bit1 = 1 and borrow = 1:
        # adjusted_bit1 = 0
        #
        # If bit1 = 0 and borrow = 1:
        # adjusted_bit1 = -1
        adjusted_bit1 = bit1 - borrow

        # Determine whether borrowing is needed.
        #
        # Example:
        # 0 - 1 cannot be done directly.
        #
        # In binary, borrowing gives us:
        # 10₂ = 2 decimal
        #
        # So:
        # adjusted_bit1 += 2
        if adjusted_bit1 < bit2:

            # Simulate borrowing from the column
            # to the left.
            adjusted_bit1 += 2

            # Tell the next column that it must
            # give up one value.
            new_borrow = 1

            # Record borrow visually.
            if bit > 0:
                borrow_row[bit - 1] = '1'

        else:
            # No borrow needed.
            new_borrow = 0

        # Compute result bit.
        #
        # Possible outcomes:
        #
        # 0 - 0 = 0
        # 1 - 0 = 1
        # 1 - 1 = 0
        # 2 - 1 = 1  (after borrowing)
        result_bit = adjusted_bit1 - bit2

        # Add new bit to front of answer
        # because we are moving right-to-left.
        result = str(result_bit) + result

        # Print several blank lines to create
        # a simple animation effect.
        print('\n' * 3)

        print(f'Step {step}')

        # Display borrow indicators.
        print(f'    {"".join(borrow_row)}')

        # Display subtraction problem.
        print(f'    {num1}')
        print(f'-   {num2}')

        print('------------')

        # Show partial result so far.
        print(f'    {result:>8}')

        # Borrow becomes active for the next column.
        borrow = new_borrow

        # Advance step counter.
        step += 1

        # Pause before next column.
        input('\nPress Enter for next step...')

    print('\nFinal Answer:')

    # If a borrow still exists after the
    # leftmost column, the true mathematical
    # result is negative.
    #
    # Example:
    # 00000000 - 00000001
    #
    # Requires borrowing beyond the most
    # significant bit.
    if borrow:
        print('This subtraction generated a borrow out.')
        print('The true mathematical result is negative.\n')

    # Display final subtraction.
    print(f'    {"".join(borrow_row)}')
    print(f'    {num1:>8}')
    print(f'-   {num2:>8}')
    print('-------------')
    print(f'    {result:>8}')


if __name__ == '__main__':
    # visualize_add_bin('00010010', '00000001')
    # visualize_add_bin('10000000', '10000000')
    visualize_add_bin('1'*8, '1'*8)
    # visualize_sub_bin('00000001', '00000001')
    # visualize_sub_bin('1' * 8, '1' * 8)
    # visualize_sub_bin('11111111', '0' * 8)
    # visualize_sub_bin('0' * 8, '1' * 8)
    # visualize_sub_bin('00010001', '00000011')