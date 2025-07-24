from plot import plot_frequencies
from input_output import read_fasta_file


# Bestemmer om sekvensen er DNA-, RNA- eller proteinsekvens. 
def detect_sequence_type(sequence):
    sequence = sequence.upper()
    valid_dna = set("ACGT")
    valid_rna = set("ACGU")
    valid_protein = set("ACDEFGHIKLMNPQRSTVWY")

    if set(sequence).issubset(valid_dna):
        sequence_type = "DNA"
        return sequence_type
    elif set(sequence).issubset(valid_rna):
        sequence_type = "RNA"
        return sequence_type
    elif set(sequence).issubset(valid_protein):
        sequence_type = "protein"
        return sequence_type
    else:
        return "unknown"

# Teller baser/aminosyrer og totalt antall baser/aminosyrer i sekvensen. 
def count_bases(sequence_type: str, sequence: dict):
    total_count = 0
    counts = {}
    for letter in sequence.upper():
            counts[letter] = counts.get(letter, 0) + 1
            total_count += 1
    return counts, total_count

# Printer ut sekvenstittel, totalantall baser/aa, antall av hver base/aa og dens prosentandel, og G-C innhold i prosent. 
def print_counts_and_percentages(counts: dict, total_count: int, sequence_type: str):
    print(f"Total count: {total_count}")
    for key, value in counts.items():
        print(f"{key}: {value} ({(value / total_count * 100):.1f}%)")
    if sequence_type != "protein":
        gc = counts.get("G", 0) + counts.get("C", 0)
        print(f"G-C content: {(gc/total_count*100):.1f}%")


def analyze_sequence_file(input_file: str, save_y_n: str):
    sequence_dict = read_fasta_file(input_file)
    for seq_name, sequence in sequence_dict.items():
            sequence_type = detect_sequence_type(sequence)
            counts, total_count = count_bases(sequence_type, sequence)
            print(f"\n--- {seq_name} ({sequence_type}) ---")
            print_counts_and_percentages(counts, total_count, sequence_type)
            plot_frequencies(counts, sequence_type, save_y_n, seq_name)
