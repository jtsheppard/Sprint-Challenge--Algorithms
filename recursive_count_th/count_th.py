'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Break the arr into a list of individual characters
    arr = list(word)

    # If the list is empty, return 0
    if not arr:
        return 0

    # If len of arr is greater than 1
    elif len(arr) > 1:

        # If arr[0] is "t" and arr[1] is "h"
        if arr[0] == "t" and arr[1] == "h":

            # Return 1 + a re-run of this function that takes off the first letter of the arr. This will re-run until a break case, and return this final value.
            return 1 + count_th("".join(arr[1:]))
        else:

            # Return 0 + a re-run of this function that takes off the first letter of the arr. This will re-run until a break case, and return this final value.
            return 0 + count_th("".join(arr[1:]))

    # If array is less than 1, there are no more possible matches. Return 0.
    else:
        return 0
