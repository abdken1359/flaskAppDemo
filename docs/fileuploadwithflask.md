To show the uploaded image after it's successfully uploaded in Flask, you need to do the following:

1. **Store the uploaded file** in a folder accessible by the Flask server.
2. **Serve the image** by returning the file path and allowing Flask to serve static files from that location.

Here’s how you can achieve that:

### Step 1: Store the Uploaded File

When a user uploads an image, you can save it in a specific folder on the server (like `uploads/`). Flask needs access to that folder to serve the image.

### Step 2: Display the Uploaded Image

After the file is uploaded, you need to return a URL where the image can be accessed and display it on the page.

### Full Example:

#### HTML Form (for uploading images):

```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file" accept="image/*">
    <input type="submit" value="Upload Image">
</form>
```

#### Flask Code to Handle File Upload and Display:

```python
import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

# Define the upload folder (ensure it exists)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Serve static files (images)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/file_upload", methods=["POST", "GET"])
def file_upload():
    if request.method == "POST":
        # Get the uploaded file
        file = request.files.get('file')
        if file:
            # Ensure the file has a proper extension (optional)
            filename = file.filename
            # Save the file in the "uploads" folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Return a response with the image URL to display the image
            image_url = f"/uploads/{filename}"
            return f'Image uploaded! <img src="{image_url}" alt="Uploaded Image">'
    return render_template('upload_form.html')  # Form to upload file

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Components:

1. **`UPLOAD_FOLDER`**:

   * This variable points to the folder where the images will be stored.
   * Make sure that the `uploads/` folder exists in your project directory, or create it manually.

2. **`send_from_directory`**:

   * The `uploaded_file` route serves the image from the `uploads/` folder. Flask will look for the image in this folder and send it to the client.

3. **File Handling**:

   * The file is saved using `file.save()`. The file will be saved under the `uploads/` folder.
   * Once uploaded, the image is displayed on the same page by returning an `<img>` tag with the image’s URL.

4. **HTML Form**:

   * The form allows users to upload an image. The `enctype="multipart/form-data"` attribute is necessary for file uploads.

### How it Works:

* When the user selects a file and submits the form, Flask saves the file in the `uploads/` folder.
* After the upload, Flask returns the image URL (`/uploads/{filename}`) and displays it on the page using an `<img>` tag.

### Folder Structure Example:

```
your_project/
│
├── app.py                # Flask app
├── uploads/              # Folder where images are stored
│   └── some_image.jpg
├── templates/            
│   └── upload_form.html  # HTML form for file upload
└── static/               # Flask's default folder for static files (not needed in this example)
```

### Notes:

* Make sure the `uploads/` directory is created, or Flask will throw an error when attempting to save the file. You can add some checks to ensure the folder exists in the code.
* You can also add file validation (e.g., check for allowed image formats or file size) before saving the file.

### Displaying Multiple Images:

If you want to display multiple images after upload, you can loop over the list of uploaded files and show each image in the HTML response.

This should enable you to upload and display images with Flask! Let me know if you need any further clarification!
