# propanpipe

This repository will host the pipline for annotating and hopefully building amino acid graphs of Covid-19 assemblies.

the environment.yml can be used to make a conda environment to run VAPiD. The metadata file is generated from the covid sequences we received from Dusseldorf, so it's basdically hard coded for that file and it generates a simple csv file that VAPiD accepts to run.
```
python3 vapid3.py fasta_file example.sbt --metadata_loc metadata.csv --db location_of_blast_database_files
```

