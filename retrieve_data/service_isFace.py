from flask import Flask, request, jsonify
app = Flask(__name__)
from checkIfFace import calc_conf_score
import os

save_folder_path = "../data/tmp"
save_file_path = save_folder_path + "/upload.jpg"

@app.route('/is_face', methods=['GET', 'POST'])
def exec_isFace_func():
	if request.method == 'POST':
		f = request.files['']
		os.makedirs(save_folder_path, exist_ok=True)
		os.remove(save_file_path)
		f.save(save_file_path)
		(n_faces, scores) = calc_conf_score(save_file_path, isPath=True)
		return jsonify(number_of_faces=n_faces,
			their_detection_scores=scores)
	return 'Expected POST request including an upload of an image.\n'