input_file = "skychallenge_skyphrase_input.txt"


def skyphrases_validator(some_input):
    with open(some_input) as file:
        lines = []
        validated = 0
        not_validated = 0

        for line in file:
            lines.append(line.rstrip().split(" "))

        for line in lines:

            if len(line) != len(set(line)):
                print(f"{line} <- this line is not valid!")
                not_validated += 1

            else:
                print(f"{line} <- this line is valid")
                validated += 1
                
        return (f"Test finished! Found {validated} validated lines and {not_validated} not validated")


print(skyphrases_validator(input_file))
