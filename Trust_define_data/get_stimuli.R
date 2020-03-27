library(tidyverse)
library(plotly)
library(ggpubr)
library(stringi)
rm(list=ls())

# First define the working directory (after selecting session>source file location)
wd <- getwd()

# Define participant initials and create a folder
part = 'GI'
dir.create(paste0(wd, '/', 'stim_', part))


## 2nd pilot ----------------------------------------------------------------------------------------

# define current person data
raw_dat <- read.csv(Sys.glob(paste0(part, '*')))


# select right columns, remove NAs 
# find mean and sd of each face ratings 

clean_dat <- raw_dat %>%
  select(file_name,slider_4.response) %>%
  na.omit() %>%
  group_by(file_name) %>%
  na.omit() %>%
  mutate(mean_rat = round(mean(slider_4.response)), sd_rat = round(sd(slider_4.response), 2))

# Select the face with minimum SD for each rating category 
sum_dat <- clean_dat %>%
  arrange(mean_rat) %>%
  group_by(mean_rat) %>%
  slice(which.min(sd_rat)) # for each mean rating take the one with the smallets SD

# what are the unique mean ratings? 
sort(unique(clean_dat$mean_rat))

# Select the scale of 7 faces to be used
soc <- sum_dat %>%
  ungroup() %>%
  top_n(-7, mean_rat) 

# Find the 8th face, for the non-social cognition
non_soc <- clean_dat %>%
  filter(mean_rat == median(soc$mean_rat)) %>%
  arrange(sd_rat) %>%
  filter(row_number() == 2)
  
# combine the above into a single csv 
# give them rank 1 to 6 and 99 for neutral
final_dat <- bind_rows(soc, non_soc) %>%
  rename(file = 'file_name') %>%
  select(-slider_4.response)



write.csv(final_dat, paste0(wd, paste0('/stim_', part, '/6_faces.csv')))


