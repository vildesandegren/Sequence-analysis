def read_fasta_file(input_file):
    sequence = {}
    current_name = None
    current_sequence = ""

    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_name:
                    sequence[current_name] = current_sequence
                current_name = line[1:]  # fjern ">" og bruk som navn
                current_sequence = ""
            else:
                current_sequence += line

        # legg til siste sekvens etter siste linje
        if current_name:
            sequence[current_name] = current_sequence

    return sequence


if __name__ == "__main__":
    print(read_fasta_file("example_FASTA.txt"))