This project deals with creating the stimuli for the main task of the Risk-prediction error experiment by Philiastides lab. 

It contains the data of multiple participants who took part in a pilot study (Trust game), aiming to determine the number 
and type of faces necessary for the main task. 

An R file in the folder 'Trust_define_data' named 'get_stimuli.R' reads in the .csv files produced by online experiment 
in Pavlovia, and extract the names of the faces which were rated most consistently by each participant across the 5 blocks of the pilot. 
.csv file created for each participant by R ('6_faces.csv'), and loads the 
6 faces + 1 neutral (for the Social part of the Main task), and 1 neutral (for the Non-social part of the main task). Resulting in 8 faces. 
The 7 faces for the social part range on a scale from 2 to 12 (e.g. 2, 3, 4, 5, 6, 7, 8, as here 5 is the middle = the neutral face).
The 8th face is selected for each participant by taking the median (5 in the top example). 

The Matlab file 'find_and_join_faces2.m' then uses the names of 8 faces and ratings to extract the relevant images from the common 
folder with all faces. It produces 7 images with pairs of faces symmetrical around the median (2 top with 8 bottom image, 8 bottom 2
on top, 3 top 7 bottom, 7 top 3 bottom, etc.). For the non-social condition only one face is used on top and bottom - 8th face, and 
number according to the scale are places in front of the top and bottom faces (similar to the social condition).
Then the same matlab script produces a .csv files which is used by Psychopy, and contains the order under which stimuli are presented,
the randomised position of the yellow frame which highlights a face on each trial, and the colour of the fixation cross which is 
cyan before risk faces (2, 3, 4, 6, 7, 8) and pink to indicate a neutral face is coming (5). For the non-social condition it is 
the same, although the cyan and pink crosses predict the values, rather than faces associated with these values. 

After the raw data from the Trust_define game is stored, the R and Matlab files are run in succession, by only changing the initials of 
the current participant. Right now, R should be checked if:
- the participants has a consistent scale with at least 7 values 
- the SDs are low 
- there are 2 different faces for the social and non-social neutral trials

If the above conditions are met, both files will work and the correct stimuli will be generated. Then the Psychopy files is opened and
the two csv files produced by Matlab should be selected. No other changes are necessary. 
