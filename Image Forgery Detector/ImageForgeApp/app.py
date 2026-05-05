from flask import Flask, request, render_template, g, jsonify
# Task 1: Import Libraries
import os
import hashlib
import cv2
from skimage.metrics import structural_similarity as ssim

app = Flask(__name__)
# Task 3a: Implement Image Upload Functionality
# Configure the upload folder
UPLOAD_FOLDER = "/usercode/ImageForgeApp/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

# Task 4b: Handle Upload Request to Backend
@app.route('/upload', methods=['POST'])

def upload():
    # Task 3b: Implement Image Upload Functionality
    # Get uploaded files from the request
    if 'file1' in request.files and 'file2' in request.files:
        g.file1 = request.files['file1']
        g.file2 = request.files['file2']

        # Ensure the upload folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save the uploaded files to the upload folder
        g.file1.save(os.path.join(app.config['UPLOAD_FOLDER'], g.file1.filename))
        g.file2.save(os.path.join(app.config['UPLOAD_FOLDER'], g.file2.filename))
    else:
        return jsonify({'error': 'Upload Two Images For Similarity Calculation!!'}), 400


    # Task 7: Determine Forgery and Display Results
        flag = False
    if calculate_similarity():
        if calculate_md5():
            reply = "No forgery detected!"
        else:
            reply = "Image is forged!"
            flag = True

    else:
        reply = "Images are different!"

    return jsonify({'message': reply, 'flag':flag})

    return

# Task 6a: Calculate MD5 Hash
def calculate_hash(file_path):
    # Calculate MD5 hash of a file
    with open(file_path, "rb") as file:
        md5_hash = hashlib.md5()
        while chunk := file.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


# Task 6b: Calculate MD5 Hash
def calculate_md5():
    # Calculate MD5 hash for uploaded files
    file_path1 = os.path.join(UPLOAD_FOLDER, g.file1.filename)
    file_path2 = os.path.join(UPLOAD_FOLDER, g.file2.filename)
    hash1 = calculate_hash(file_path1)
    hash2 = calculate_hash(file_path2)

    if (hash1 == hash2):
        return True
    return False



# Task 5: Calculate Similarity of Images
SSIM_THRESHOLD = 0.9

def calculate_similarity():
    # Load and compare image similarity
    image_path1 = os.path.join(UPLOAD_FOLDER, g.file1.filename)
    image_path2 = os.path.join(UPLOAD_FOLDER, g.file2.filename)
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # Resize the image to have both of the same size
    image1_resized = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Calculate the similarity
    ssim_score = ssim(image1_resized, image2)

    if ssim_score > SSIM_THRESHOLD:
        return True
    return False



if __name__ == '__main__':
    app.run(debug=True)