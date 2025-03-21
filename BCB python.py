pip install biopython

from Bio import SeqIO
from itertools import zip_longest

def interleave_fastq(forward_file, reverse_file, output_file):
    """
    Interleaves two paired-end FASTQ files using Biopython's SeqIO.
    """
    try:
        with open(forward_file, 'r') as fwd, open(reverse_file, 'r') as rev, open(output_file, 'w') as out:
            forward_reads = SeqIO.parse(fwd, 'fastq')
            reverse_reads = SeqIO.parse(rev, 'fastq')

            for i, (fwd_read, rev_read) in enumerate(zip_longest(forward_reads, reverse_reads), start=1):
                if fwd_read is None or rev_read is None:
                    raise ValueError(f"Error: Unequal number of reads. Mismatch at record {i}.")

                SeqIO.write(fwd_read, out, 'fastq')
                SeqIO.write(rev_read, out, 'fastq')
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f" Interleaving complete! Output saved to '{output_file}'.")

# Example usage (update filenames as needed):
forward_file = "bacterium_R1.fastq"
reverse_file = "bacterium_R2.fastq"
output_file = "interleaved_output.fastq"

interleave_fastq(forward_file, reverse_file, output_file)

!python interleave_fastq.py bacterium_R1.fastq bacterium_R2.fastq interleaved_output.fastq

interleave_fastq("bacterium_R1.fastq", "bacterium_R2.fastq", "interleaved.fastq")

files.download("interleaved.fastq")

