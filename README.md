# PoIs Manager
This repository has done to facility the correction and extraction of PoIs on the Google 
Code-in tasks by the Liquid Galaxy Lab.

## Extract PoIs
To extract PoIs you have to execute the following command:
`python extract_pois.py`<p>
By default the script will take all the kmz files from a folder called KMZ and will generate 
a pois.txt with all the PoIs generated.

## Check PoIs
If you have a txt file with all your PoIs you can use the following command in order to check
common errors:
`python check_pois.py`<p>
In this script you must give the file name that you want to check. After the script will 
show you if you have any error or anything otherwise.
