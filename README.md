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

In the repository there are 2 example files called "pois_fail.txt" and "pois_correct.txt". This are the both outputs.
Example if you have any error (`python check_pois.py pois_fail.txt`):<p>
![alt text](https://raw.githubusercontent.com/amerinoo/PoIs_Manager/master/Images/output_pois_fail.png)

Either you do not have any error or when you fix all the error you can see the following output (`python check_pois.py pois_correct.txt`):<p>
![alt text](https://raw.githubusercontent.com/amerinoo/PoIs_Manager/master/Images/output_pois_correct.png)
