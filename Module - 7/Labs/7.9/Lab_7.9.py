# function to read the input file and create a dictionary
def create_tv_show_dict(file_name):
    tv_shows = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()

        # loop through lines and add to the dictionary
        for i in range(0, len(lines), 2):
            seasons = int(lines[i].strip())
            show = lines[i + 1].strip()

            if seasons not in tv_shows:
                tv_shows[seasons] = []
            tv_shows[seasons].append(show)

    return tv_shows


# function to write sorted output by keys to a file
def write_sorted_by_keys(tv_shows):
    with open('output_keys.txt', 'w') as file:
        for seasons in sorted(tv_shows.keys()):
            shows = '; '.join(tv_shows[seasons])  # join shows with a semicolon
            file.write(f"{seasons}: {shows}\n")


# function to write sorted output by titles to a file
def write_sorted_by_titles(tv_shows):
    with open('output_titles.txt', 'w') as file:
        # create a sorted list of all shows
        all_shows = [show for shows in tv_shows.values() for show in shows]
        for show in sorted(all_shows):
            file.write(f"{show}\n")


# main program
if __name__ == "__main__":
    input_file = input()  # read input file name
    tv_shows = create_tv_show_dict(input_file)  # create dictionary
    write_sorted_by_keys(tv_shows)  # output sorted by keys
    write_sorted_by_titles(tv_shows)  # output sorted by titles