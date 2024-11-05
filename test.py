import board as b
import heaton as h
import time

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?


if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = b.next_board_state_v2(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print("Expected:")
        print(expected_next_state1)
        print("Actual:")
        print(actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = b.next_board_state_v2(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print("Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)


    # TEST 3: Timing differences between my code and Heaton's example code
    init_state3 = b.random_state(100,100)
    curr_aaronray = init_state3
    curr_heaton = init_state3

    time_aaronray = 0
    time_heaton = 0
    loops = 1000

    # time for aaronray
    start_aaronray = time.time()
    for i in range(loops):
        #temp_a = b.next_board_state(curr_aaronray)
        temp_a = b.next_board_state_v2(curr_aaronray)
        curr_aaronray = temp_a
    end_aaronray = time.time()
    time_aaronray = end_aaronray - start_aaronray

    # time for heaton
    start_heaton = time.time()
    for i in range(loops):
        temp_h = h.next_board_state(curr_heaton)
        curr_heaton = temp_h
    end_heaton = time.time()
    time_heaton = end_heaton - start_heaton

    print("Time for aaronray: ",time_aaronray)
    print("Time for heaton: ",time_heaton)
    if time_aaronray < time_heaton:
        print("\naaronray ran faster")
        p_faster = round((time_heaton/time_aaronray),2)
        print("     ",p_faster," times faster")
    else:
        print("\nheaton ran faster")
        p_faster = round((time_aaronray/time_heaton),2)
        print("   -> ",p_faster," times faster")