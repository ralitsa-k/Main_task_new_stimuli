This project deals with creating the stimuli for the main task of the Risk-prediction error experiment by Philiastides lab. 

It contains the data of multiple participants who took part in a pilot study (Trust game), aiming to determine the number 
and type of faces necessary for the main task. 

The experiment created in **Psychopy** shows one face at a time and the participants is required to rate the face on its trustworthiness (as defined in the inctructions).

An R file in the folder 'Trust_define_data' named 'get_stimuli.R' reads in the .csv files produced by online experiment 
in Pavlovia, and extract the names of the faces which were rated most consistently by each participant across the 5 blocks of the pilot. 
.csv file created for each participant by R ('6_faces.csv'), and loads the 
6 faces + 1 neutral (for the Social part of the Main task), and 1 neutral (for the Non-social part of the main task). Resulting in 8 faces. 
The 7 faces for the social part range on a scale from 2 to 12 (e.g. 2, 3, 4, 5, 6, 7, 8, as here 5 is the middle = the neutral face).
The 8th face is selected for each participant by taking the median (5 in the top example). 
