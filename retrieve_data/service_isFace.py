from flask import Flask, request
app = Flask(__name__)
from checkIfFace import calc_conf_score
import os

save_folder_path = "../data/tmp"
save_file_path = save_folder_path + "/upload.jpg"

@app.route('/is_face', methods=['GET', 'POST'])
def exec_isFace_func():
	if request.method == 'POST':
		f = request.files['']
		os.makedirs(save_folder_path)
		f.save(save_file_path)
		(n_faces, scores) = calc_conf_score(save_file_path, isPath=True)
		return "number of faces: {}. Their scores are {}".format(
			n_faces, scores)

	return 'Expected POST request including an upload of an image.\n'