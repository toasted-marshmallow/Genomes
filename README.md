# Genomes

The purpose of this script is to read in text files that contain the genomes of various organisms and/or viral pathogens e.g., SARS-CoV2 (Agent that causes COVID-19 disease), 
Vibrio-cholerae (the Cholera water-borne disease) etc. The script will then count the number of Adenine (A), Thymine (T), Guanine (G), Cytosine (C), and the respective pairs (A-T, G-C), and calculate the total percentages of each of the nucleo-bases in the respective genomes. The script will print the percentages in the python console as well as create a pie chart and bar graph to display the nucleo-base percentages using the matplotlib package. 

You can easily modify this script if you are working with RNA information as well. All you'd have to do is write a line that converts the Thymine (T) to Uracil (U) and do the calculations from there. Furthermore, if you would like to look at other genomes, just download them from the NCBI databases and put them in a folder. In my case the folder that contains all of the text files is called "Genomes," but you can name your folder anything you want -- just modify it in the script. 

Feel free to use this script and/or modify it for your purposes. This is a pretty simple script, but I wrote it because -- well practice and I wanted to see if I could accomplish this. I'm not a great programmer :'(

The genetic information was taken pulled from various NIH and CDC databases, and the specific data that I used will be included in the reference below.

## Resources
Corynebacterium Diphtheriae Genome: https://www.ncbi.nlm.nih.gov/nuccore/LN831026.1?report=fasta <br>
Vibrio Cholerae Genome: https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP010812.1?report=genbank <br>
Middle East Respiratory Syndrome (MERS-CoV) Genome: https://www.ncbi.nlm.nih.gov/nuccore/MH734114.1#sequence_MH734114.1 <br>
SARS-CoV2 Genome: https://www.ncbi.nlm.nih.gov/nuccore/MN908947 <br> 
SARS-COV (2003) Genome: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome-related%20coronavirus,%20taxid:694009 <br>
Bundibugyo Ebolavirus: https://www.ncbi.nlm.nih.gov/nuccore/302371213 <br>
United States Cancer Data (2016): https://gis.cdc.gov/Cancer/USCS/DataViz.html
