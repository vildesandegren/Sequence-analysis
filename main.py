from analysis import analyze_sequence_file

def main():
    input_file = input("Input FASTA sequence file:")
    save_y_n = input("Would you like to automatically save the plots created? (y/n)")
    analyze_sequence_file(input_file, save_y_n)

if __name__ == "__main__":
    main()



