from math import comb

def calc_differences(seq):
    seq_list = [seq]
    found = False

    for i in seq_list:
        length = len(i)
        temp_list = list()

        for j in range(0, length-1):
            diff = i[j+1] - i[j]
            temp_list.append(diff)

        seq_list.append(temp_list)

        if len(temp_list) == 1:
            break

        elif len(set(temp_list)) == 1:
            found = True
            break

    return found, seq_list


if __name__ == "__main__":

    print("\n==================================================================")
    print("                 WELCOME TO 'WHAT COMES NEXT?'                  ")
    print("       A PROGRAM THAT PREDICTS THE NEXT NUMBER IN SEQUENCE      ")
    print("==================================================================\n\n")

    # sequence = list()
    # n = int(input("Enter the number of terms of the sequence you want to give: "))

    # for i in range(n):
    #     sequence.append(int(input("Enter number {}: ".format(i+1))))
        
    print("Enter the sequence with space separated terms")
    
    sequence = list(map(int, input().strip().split()))
    n = len(sequence)
    
    found, seq_list = calc_differences(sequence)

    if found:
        length = len(seq_list)
        ans = 0
        for i in range(length):
            ans += seq_list[i][0]*comb(n, i)

        print("\n" + str(ans) + " comes next")

    else:
        print("\nThe program was unable to find what comes next.")
        print("This can happen due to 3 reasons:")
        print("1. The sequence provided is random.")
        print("2. The sequence provided is not polynomial.")
        print("3. The sequence provided has a degree higher than 5.")
        print("If your sequence generator has a degree of n, please provide atleast n+2 terms.")
