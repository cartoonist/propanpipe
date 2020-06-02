import gzip
import os
import logging
import sys


def read_fasta(fasta_file_path, sequences):
    """
    read fasta file and return a dict

    :param fasta_file_path: path to fasta file
    :return: a dictionary of seq_name:seq
    """

    if not os.path.exists(fasta_file_path):
        logging.error("file {} does not exist".format(fasta_file_path))
        sys.exit()

    if fasta_file_path.endswith("gz"):
        fasta_file = gzip.open(fasta_file_path, "rt")
    else:
        fasta_file = open(fasta_file_path, "r")

    seqs = []
    seq_name = ""
    for line in fasta_file:
        line = line.strip()
        if not line:  # empty line
            continue

        if line.startswith(">"):
            if len(seqs) != 0:  # there was a sequence before
                sequences[seq_name] = "".join(seqs)
                seq_name = line[1:]
                seqs = []
            else:
                seq_name = line[1:]
        else:
            seqs.append(line)

    if seqs:
        sequences[seq_name] = "".join(seqs)

sequences = dict()
read_fasta(sys.argv[1], sequences)

# sequences is a dictionary of seq names and seq
metadata_out = ["strain,collection-date,country,coverage"]  # header
splitted_names = []
for k in sequences.keys():
    splitted_names.append(k.split("/"))

for k in splitted_names:
    if len(k) == 3:  # some had 3 and some had 4
        metadata_out.append(",".join([k[1], k[2], k[0], "0"]))  # strain, date, country, coverage

    elif len(k) == 2:
        metadata_out.append(",".join([k[0], k[1], "Wuhan", "0" ]))
    
    elif (len(k) == 4) and (k[0] == "Belgium"):
        metadata_out.append(",".join([k[2], k[3], k[0], "0" ]))

    else:
        # the assemblies had different sequence names with different order
        metadata_out.append(",".join([k[2], k[3], k[1], "0" ]))

out_file = open("metadata.csv", "w")
for m in metadata_out:
    out_file.write(m)
    out_file.write("\n")
out_file.close()
