def main():
    with open("input.txt") as f:
        elf_list = []
        elf = 0
        for calorie in [line.rstrip() for line in f.readlines()]:
            if calorie:
                elf += int(calorie)
            else:
                elf_list.append(elf)
                elf = 0

        print(max(elf_list))


if __name__ == "__main__":
    main()