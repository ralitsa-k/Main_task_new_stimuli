%% Read in the .csv file for each participants

% This matlab script uses the R-produced csv files from the judgment game
% to construct the pairs of faces which will be used in the main task.

% variables of the table are:
% - file name,
% - good(0) or bad(1),
% - standardised rating,
% - original rating
tic
clear all
% define the initials of the current participant
part = 'DS'

% define main working directory to main folder with faces
% pwd should be /Main_task_stimuli 
main_folder = pwd

% then go to folder of current participant
cd(strcat(main_folder, '/Trust_define_data/stim_', part))

% open the csv with selected faces
files = dir('6_faces.csv');
files.name;
r_dat = table2cell(readtable(files.name));

% go back to folder with faces
% cd(main_folder)
cd(strcat(main_folder, '/neutral_each'))

% the scale which is used for the current participant (6 faces)
scale = cell2mat(r_dat(1:7,3));
scale_down = flip(scale);


%% Social stimuli for Psychopy
% read the images by using the file names from the csv file (r_dat)
% there are 8 images for each participant. Here we read in only the ones
% for the social condition 6 + 1
for i = 1:7
    % read the faces for the current participant
    im(i).face = imread(r_dat{i,2});
    % also record the names of the files
    im(i).name = strcat(cell2mat(r_dat(i,2)));
end

% A black frame is added to the top of each image to fox the distance from
% the edges
black_frame = zeros(50, 600, 3);

% this loop combined the pairs of faces and writes names for new files
for i = 1:7
    % get the reverse of the structure to combine each face with its
    % symmetrical value e.g. 2 with 8, 3 with 7 etc.
    im_rev = flip(im);
    im(i).combined = cat(1, black_frame, im(i).face, im_rev(i).face);
    im(i).file_name = strcat('Soc_', mat2str(scale(i)), mat2str(scale_down(i)), '.png');
end

cd(strcat(main_folder))

% write .png files of combined faces
for i = 1:7
    imwrite(im(i).combined, im(i).file_name)
end

%% Social file for Psychopy

% create cell with names of files, conditions, and headers
pair_faces = cell(8,1);

% Following is the building of a file to be used by Psychopy
% stimuli are repeated and randomised
for i = 1:7
    pair_faces{i+1,1} = im(i).file_name;
end

pair_faces(1,1)      = {'img_names'}
pair_faces(1:8,5)    = {'trigger_integer'; 117; 226; 335; 444; 553; 662; 771}
pair_faces(1, 1)     = {'img_names'};
pair_faces(1, 2)     = {'cond'};
pair_faces(1, 3)     = {'cueCol'};
pair_faces(1, 4)     = {'polygonPos'};
pair_faces(1, 5)     = {'trigger_integers'};
pair_faces(1, 6)     = {'order'};

pair_faces(2:7, 2)   = {'risk'};
pair_faces(8, 2)     = {'zero'};
pair_faces(1, 3)     = {'cueCol'};
pair_faces(2:4, 3)   = {'[90,1,1]'}; %cyan
pair_faces(6:8, 3)   = {'[90,1,1]'}; %cyan
pair_faces(5, 3)     = {'[0,0.5,1]'} %pink

headers = pair_faces(1,:);

% Repeat risk trial and neutral trials a certain number of times and
% combine in a single cell called all_trials
risk_trials = repmat(pair_faces(2:7, :),15, 1);
zero_trials = repmat(pair_faces(8,:),12,1);
all_trials = vertcat(risk_trials,zero_trials);

% randomise trials order
all_random = all_trials(randperm(size(all_trials, 1)), :);

% get a random column of upper' and lower' for position of highlight on each trial
vars = cell({'upper.png'; 'lower.png'})
cell_pos = repelem(vars, 51);
rand_pos = cell_pos(randperm(size(cell_pos,1)),:);
% add the random highlight position to the file
all_random(:,4) = rand_pos;

% add the headings to the final file
final_file = [headers; all_random];
final_file(2:103, 6) = num2cell(1:102);

% write the csv file
writecell(final_file, 'pair_faces_Soc.csv')

%% Non-social condition stimuli

% Set working directory to the folder with all faces
folder = cd(strcat(main_folder, '/neutral_each'));

% read the neutral face for the non-social condition
im8 = imread(r_dat{8, 2});

clear number

for i = 1:7
    num_comb = zeros(1650, 600, 7);
    bw = [];
    bw_3d = [];
    % prepare the neutral face
    non_soc_f = cat(1, black_frame, im8, im8);

    % Create a struct with the names of the .png files containing the numbers
    number(i).file = strcat('num_', mat2str(cell2mat(r_dat(i,3))), '.png');
    % read in the numbers - 1d, according to participants' values
    number(i).read = imread(number(i).file);

end

rev_number = flip(number);

for i = 1:7

    % create the pairs of opposite values
    number(i).combined = cat(1, number(i).read, rev_number(i).read);
    % turn the numbers into black and white
    number(i).combined(number(i).combined ~= 0) = 255;
    % make the numbers 3d
    number(i).trid = repmat(number(i).combined, 1, 1, 3);
    % write the neutral face in the structure
    number(i).face = non_soc_f;
    % put the numbers on top of the neutral face
    number(i).face(number(i).trid ~= 0) = 255;

end


% write the names of the new files
for k = 1:7
    number(k).newfile = strcat('nonS_', mat2str(scale(k)), mat2str(scale_down(k)), '.png');
end

% Write the images for Psychopy non-social block
cd(strcat(main_folder))

for i = 1:7
    imwrite(number(i).face, number(i).newfile)
end


%% Non-social file for Psychopy
% Similar to the social one, this is construction of the file to be used by
% Psychopy with defined repetition of trials and randomisation

pair_num = cell(8,1);

for i = 1:7
    pair_num{i+1,1} = number(i).newfile;
end

pair_num(1,1)      = cell({'img_names'})
pair_faces(1:8,5)    = {'trigger_integer'; 117; 226; 335; 444; 553; 662; 771}
pair_num(1, 1)     = {'img_names'};
pair_num(1, 2)     = {'cond'};
pair_num(1, 3)     = {'cueCol'};
pair_num(1, 4)     = {'polygonPos'};
pair_num(1, 5)     = {'trigger_integers'};
pair_num(1, 6)     = {'order'};

pair_num(2:7, 2)   = {'risk'};
pair_num(8, 2)     = {'zero'};
pair_num(1, 3)     = {'cueCol'};
pair_num(2:4, 3)   = {'[90,1,1]'}; %cyan
pair_num(6:8, 3)   = {'[90,1,1]'}; %cyan
pair_num(5, 3)     = {'[0,0.5,1]'} %pink

headers2 = pair_num(1,:);

% define risk and zero trials and combine with all_trials
risk_trials2 = repmat(pair_num(2:7, :),15, 1);
zero_trials2 = repmat(pair_num(8,:),12,1);
all_trials2 = vertcat(risk_trials2,zero_trials2);

% randomise trials order
all_random2 = all_trials2(randperm(size(all_trials2, 1)), :);

% get a random column of upper' and lower' for position of polygon on each trial
vars2 = cell({'upper.png'; 'lower.png'})
cell_pos2 = repelem(vars2, 51);
rand_pos2 = cell_pos(randperm(size(cell_pos2,1)),:);

% add the random polygon position to the file
all_random2(:,4) = rand_pos2;
% add the headings
final_file2 = [headers2; all_random2];
final_file2(2:103, 6) = num2cell(1:102);


% write the csv file
writecell(final_file2, 'pair_num_nonSoc.csv')

toc
