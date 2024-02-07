'''
Write solutions to 4. New Mouse Release here.

Author: Kayven Chen
SID: 530654658
Unikey: kche4026
'''



from mouse import generate_mouse, TYPE_OF_MOUSE

# hint generate a lot of mouses ????

def mouse_test():
    # generating a lot of mouses to check that the distribution of mice spawned 
    # is roughly equal to the expected amount.

    # expected amount of mice if 10000 are spawned

    probabilities = [0.5, 0.1, 0.15, 0.1, 0.1, 0.05]
    expected_amount_of_each_mouse = {
        TYPE_OF_MOUSE[0]: int(probabilities[0] * 10000), # None
        TYPE_OF_MOUSE[1]: int(probabilities[1] * 10000), # Brown
        TYPE_OF_MOUSE[2]: int(probabilities[2] * 10000), # Field
        TYPE_OF_MOUSE[3]: int(probabilities[3] * 10000), # Grey
        TYPE_OF_MOUSE[4]: int(probabilities[4] * 10000), # White
        TYPE_OF_MOUSE[5]: int(probabilities[5] * 10000), # Tiny
    }

    # initalising count
    count = {
        TYPE_OF_MOUSE[0]: 0, # None
        TYPE_OF_MOUSE[1]: 0, # Brown
        TYPE_OF_MOUSE[2]: 0, # Field
        TYPE_OF_MOUSE[3]: 0, # Grey
        TYPE_OF_MOUSE[4]: 0, # White
        TYPE_OF_MOUSE[5]: 0, # Tiny
    }

    # generate 10000 mice and count the number of each mouse spawned.
    i = 0
    while i < 10000:
        mouse = generate_mouse()
        count[mouse] += 1
        i += 1

    # check that it is similar to expected
    # allow a error of +/- 10%
    i = 0
    while i < len(tuple(expected_amount_of_each_mouse.items())):
        actual_count = tuple(count.items())[i][1]
        expected_count = tuple(expected_amount_of_each_mouse.items())[i][1]
        # get the upper and lower bounds
        lower_bound = expected_count * 0.9
        upper_bound = expected_count * 1.1 
        assert lower_bound < actual_count
        assert actual_count < upper_bound
        print(f"{TYPE_OF_MOUSE[i]} is approximately equal to the expected value "
              "with a error of +/- 10%\n"
              f"{actual_count} {TYPE_OF_MOUSE[i]} mice spawned\n"
              f"{expected_count} {TYPE_OF_MOUSE[i]} mice were expected\n")
        i += 1


mouse_test()
