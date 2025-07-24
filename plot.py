import os
import matplotlib.pyplot as plt
import time

def plot_frequencies(counts: dict, sequence_type: str, save_y_n: str, seq_name):

    labels = list(counts.keys())
    values = list(counts.values())

    # Decide labels according to sequence type
    if sequence_type == "DNA":
        x_label = "Base"
        title = "DNA base frequencies"
    elif sequence_type == "RNA":
        x_label = "Base"
        title = "RNA base frequencies"
    elif sequence_type == "protein":
        x_label = "Amino acid"
        title = "Protein amino acid frequencies"
    else:
        x_label = "Symbol"
        title = "Unknown sequence frequencies"

    # Make plot
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel("Count")
    
    # Lag filnavn på plot 
    timestamp = time.strftime("%d%m%Y - %H%M")
    plot_name = f"{seq_name}_plot_{timestamp}.png"


    # Lagre plot i ny mappe
    if save_y_n.lower() == "y":
        folder = "plots"
        os.makedirs(folder, exist_ok=True) # Lager mappen. exist_ok=True betyr 'lag mappen hvis den ikke finnes, hvis den finnes, gjør ingenting'
        file_path = os.path.join(folder, plot_name) # Bygger trygg filsti
        plt.savefig(file_path, format="png") #Lagrer plottet
        print(f"Plot saved as {plot_name}") 
    
    plt.show()
