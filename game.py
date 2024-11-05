from board import *

if __name__ == "__main__":
    while(1):
        c = input("Welcome to the Game of Life!\n\nWould you like to:\n   -> (1) play with soup\n   -> (2) load in a file\n   -> (3) play with soup, in the seed rule space\nEnter Choice: ")
        if c == "1":
            w = input("-> Enter the width (columns) of the game: ")
            h = input("-> Enter the height (rows) of the game: ")
            p = input("-> Enter the starting population, expressed as a number from 0 to 1: ")
            confirm = input("Begin game? Type 'yes' to initialize game.\n")
            if confirm == "yes":
                curr = random_state(int(w),int(h),float(p))
                # play_game_soup(curr)
                play_game_soup_v2(curr)
            else:
                print("\n-------------------------------------------")
                print("   Incorrect input detected.\nRestarting...")
                print("-------------------------------------------\n")
        elif c == "2":
            f = input("-> Which file would you like to load?\n   -> (1) Toad\n   -> (2) Beacon\n   -> (3) Blinker\n   -> (4) Glider\n   -> (5) Gospel Glider Gun\n   -> (6) Pulsar\n   -> (7) Pentadecathlon\n   -> (8) Queen Bee Shuttle\n   -> (9) Seed-space des 1\n   -> (10) Discovery file\nEnter Choice:")
            if f == "1":
                play_game_file("./toad.txt")
            elif f == "2":
                play_game_file("./beacon.txt")
            elif f == "3":
                play_game_file("./blinker.txt")
            elif f == "4":
                play_game_file("./glider.txt")
            elif f == "5":
                play_game_file("./ggg.txt")
            elif f == "6":
                play_game_file("./pulsar.txt")
            elif f == "7":
                play_game_file("./pentadecathlon.txt")
            elif f == "8":
                play_game_file("./queen_bee_shuttle.txt")
            elif f == "9":
                play_game_file_seed("./seed_space_2.txt",0.03)
            elif f == "10":
                play_game_file_seed("./p_discovery_2.txt")
            else:
                print("\n-------------------------------------------")
                print("   Incorrect input detected.\nRestarting...")
                print("-------------------------------------------\n")

        elif c == "3":
            w = input("-> Enter the width (columns) of the game: ")
            h = input("-> Enter the height (rows) of the game: ")
            p = input("-> Enter the starting population, expressed as a number from 0 to 1: ")
            confirm = input("Begin game? Type 'yes' to initialize game.\n")
            if confirm == "yes":
                curr = random_state(int(w),int(h),float(p))
                play_game_seed(curr)
            else:
                print("\n-------------------------------------------")
                print("   Incorrect input detected.\nRestarting...")
                print("-------------------------------------------\n")


        else:
            print("\n-------------------------------------------")
            print("   Incorrect input detected.\nRestarting...")
            print("-------------------------------------------\n")

    
