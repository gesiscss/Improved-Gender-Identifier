import dlib

def calc_conf_score(image, isPath=True):
	detector = dlib.get_frontal_face_detector()

	if isPath:
		img = dlib.load_rgb_image(image)
	else:
		img = image
		
	dets, scores, idx = detector.run(img, 1, -1)
	n_faces = len(dets)
	img_scores = []
	for i, d in enumerate(dets):
		img_scores.append(scores[i])

	image_results = (n_faces, scores)
	return image_results