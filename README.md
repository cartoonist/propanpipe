# propanpipe

This repository will host the pipline for annotating and hopefully building amino acid graphs of Covid-19 assemblies.

the environment.yml can be used to make a conda environment to run VAPiD. The metadata file is generated from the covid sequences we received from Dusseldorf, it needs a specific format of a .csv file to run (similar to the one they have in the example in their repo)


For the the viruses from Ref Seq Vir I downloaded this file https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz
Then removed the assemblies with NC_ from the all_fasta provided by vapid and updated it with the ones I downloded. There were 2 thousand more references in the new one.

Then I built a new blast database with `makeblastdb -in all_viruses.fasta -dbtype nucl`

When calling vapid, I gave the following command, I kept the same example.sbt file they had in their repo, but we're not publishing these assemblies, it doesn't matter what the information is inside the .sbt:
```
python3 vapid3.py input_fasta_file.fasta example.sbt --metadata_loc metadata.csv --db all_virusts.fasta
```
