# propanpipe

This repository will host the pipline for annotating and hopefully building amino acid graphs of Covid-19 assemblies.

the environment.yml can be used to make a conda environment to run VAPiD. The metadata file is generated from the covid sequences we received from Dusseldorf, so it's basdically hard coded for that file and it generates a simple csv file that VAPiD accepts to run.
```
python3 vapid3.py fasta_file example.sbt --metadata_loc metadata.csv --db location_of_blast_database_files
```

For the the viruses from Ref Seq Vir I downloaded this file https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/viral.1.1.genomic.fna.gz
Then removed the assemblies with NC_ from the all_fasta provided by vapid and updated it with the ones I downloded. There were 2 thousand more references in the new one.

Then I built a new blast database with `makeblastdb -in all_viruses.fasta -dbtype nucl`
