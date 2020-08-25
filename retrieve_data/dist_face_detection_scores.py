import os
import pandas as pd
from checkIfFace import calc_conf_score

def list_files(dir):
    img_paths = []
    folder = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            img_paths.append(os.path.join(root, name))
            folder.append(root[root.rfind('/')+1:])
    return (folder, img_paths)

scrape_folder_path = "../data/male_sample10/"
f_and_fs = list_files(scrape_folder_path)

dist_conf_vals = pd.DataFrame({
	"name" : f_and_fs[0],
	"image_path" : f_and_fs[1],
	"number_of_faces" : [None for i in range(len(f_and_fs[0]))],
	"confidence_value(s)" : [None for i in range(len(f_and_fs[0]))],
	})

for row in dist_conf_vals.itertuples(index=True):
	score_calc_results = calc_conf_score(row[2])
	n_faces = score_calc_results[0]
	conf_scores = score_calc_results[1]
	dist_conf_vals.iloc[row[0],2] = n_faces
	dist_conf_vals.iloc[row[0],3] = conf_scores

conf_scores_save_path = scrape_folder_path + "face_conf_scores.csv"
dist_conf_vals.to_csv(conf_scores_save_path)
