def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    """
    Trains a k-nearest neighbors classifier for face recognition.

    :param train_dir: directory that contains a sub-directory for each known person, with its name.

     (View in source code to see train_dir example tree structure)

     Structure:
        <train_dir>/
        ├── <person1>/
        │   ├── <somename1>.jpeg
        │   ├── <somename2>.jpeg
        │   ├── ...
        ├── <person2>/
        │   ├── <somename1>.jpeg
        │   └── <somename2>.jpeg
        └── ...

    :param model_save_path: (optional) path to save model on disk
    :param n_neighbors: (optional) number of neighbors to weigh in classification. Chosen automatically if not specified
    :param knn_algo: (optional) underlying data structure to support knn.default is ball_tree
    :param verbose: verbosity of training
    :return: returns knn classifier that was trained on the given data.
    """
    # Load images from training directory and store in X and y
    X = []
    y = []
    for subdir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, subdir)):
            continue

        # Load images from this subdirectory
        sub_dir = os.path.join(train_dir, subdir)
        img_paths = image_files_in_folder(sub_dir)
        images = [face_recognition.load_image_file(img_path) for img_path in img_paths]
        face_encodings = [face_recognition.face_encodings(img, known_face_locations=face_recognition.face_locations(img))[0] for img in images if len(face_recognition.face_locations(img)) == 1]
        labels = [subdir] * len(face_encodings)

        X += face_encodings
        y += labels

        if verbose:
            print(f"Loaded {len(face_encodings)} faces from {subdir}")

    # Determine how many neighbors to use for weighting in the KNN classifier
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    # Create and train the KNN classifier
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf
