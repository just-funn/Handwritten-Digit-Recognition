# 🤖 Handwritten Digit Recognition

A simple and beginner-friendly **Handwritten Digit Recognition** application built with Python, TensorFlow, and Streamlit. This app uses a CNN (Convolutional Neural Network) trained on the MNIST dataset to recognize handwritten digits (0–9).

## 📋 Features

- ✅ **Upload Images**: Upload JPG/PNG images of handwritten digits
- ✅ **Draw & Recognize**: Draw digits directly on a canvas (optional feature)
- ✅ **Real-time Predictions**: Get instant digit predictions with confidence scores
- ✅ **Probability Distribution**: View prediction confidence for all digits (0–9)
- ✅ **Pre-trained MNIST Model**: Uses a CNN trained on 60,000 MNIST images
- ✅ **User-Friendly UI**: Built with Streamlit for easy interaction
- ✅ **Beginner-Friendly**: Simple, well-commented code

## 🛠️ Project Structure

```
Handwritten-Digit-Recognition/
├── main.py                 # Streamlit web application
├── train_model.py          # Script to train a CNN model on MNIST
├── requirements.txt        # Python dependencies
├── mnist_model.h5          # Pre-trained model (generated after training)
└── README.md               # This file
```

## 📦 Dependencies

- **TensorFlow/Keras**: Deep learning framework for model training and inference
- **NumPy**: Numerical computations
- **OpenCV (cv2)**: Image preprocessing
- **Streamlit**: Web framework for the user interface
- **Pillow**: Image handling
- **scikit-learn**: Machine learning utilities

## 🚀 Quick Start

### Step 1: Install Python
Ensure you have Python 3.7+ installed. Download from [python.org](https://www.python.org/downloads/)

### Step 2: Clone the Repository
```bash
git clone https://github.com/just-funn/Handwritten-Digit-Recognition.git
cd Handwritten-Digit-Recognition
```

### Step 3: Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Train the Model (First Time Only)
The model needs to be trained once. This generates `mnist_model.h5`:
```bash
python train_model.py
```

**Note**: This may take 5-10 minutes depending on your computer. The script downloads the MNIST dataset automatically (~11 MB).

### Step 6: Run the Streamlit App
```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

## 📚 How to Use

### Option 1: Upload an Image
1. Go to the **"Upload Image"** tab
2. Click **"Choose an image file"**
3. Select a PNG or JPG image with a handwritten digit
4. View the prediction and confidence score
5. Expand **"View all predictions"** to see confidence for all digits

### Option 2: Draw a Digit (Requires streamlit-canvas)
1. Go to the **"Draw Digit"** tab
2. Draw a digit on the canvas
3. View the prediction and confidence score

**Optional**: To enable drawing, install streamlit-canvas:
```bash
pip install streamlit-canvas
```

## 🧠 Model Architecture

The CNN model used is:
```
Conv2D(32 filters, 3x3) → MaxPooling → Conv2D(64 filters, 3x3) → MaxPooling → Flatten → Dense(64) → Dense(10 - softmax)
```

- **Input**: 28×28 grayscale images
- **Output**: 10 probabilities (one for each digit 0–9)
- **Training**: 5 epochs on MNIST training set (60,000 images)

## 🔧 Key Functions

### `preprocess_image(image_array)`
Preprocesses the input image:
- Converts to grayscale
- Resizes to 28×28 pixels
- Normalizes pixel values (0–1 range)
- Inverts colors if necessary (white digit on black background)
- Reshapes for model input

### `predict_digit(model, image_array)`
Predicts the digit from an image:
- Returns: (predicted_digit, confidence, all_probabilities)
- Uses model predictions and selects the highest confidence

## ⚠️ Common Errors & Solutions

### Error 1: `ModuleNotFoundError: No module named 'tensorflow'`
**Solution**:
```bash
pip install tensorflow
```

### Error 2: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**:
```bash
pip install streamlit
```

### Error 3: `FileNotFoundError: mnist_model.h5 not found`
**Solution**: Run the training script first:
```bash
python train_model.py
```

### Error 4: Drawing canvas not working
**Solution**: Install streamlit-canvas:
```bash
pip install streamlit-canvas
```

### Error 5: Poor prediction accuracy
**Possible causes & solutions**:
- Image is too small or unclear → Use a clearer, larger digit
- Digit orientation is unusual → Model expects upright digits
- Colors are inverted → The preprocessing should handle this automatically
- Try different digits with the sample MNIST images

### Error 6: `PermissionError` when running the script
**Solution**: Check file permissions or try:
```bash
chmod +x main.py train_model.py
```

## 📊 Training Details

- **Dataset**: MNIST (handwritten digits 0–9)
- **Training Samples**: 60,000 images
- **Test Samples**: 10,000 images
- **Image Size**: 28×28 pixels (grayscale)
- **Epochs**: 5
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Expected Accuracy**: ~98–99%

## ⚙️ Parts That Cannot Be Fully Automated

1. **Initial Environment Setup**: Python installation and virtual environment creation require user action
2. **Model Training**: First-time training requires downloading MNIST dataset (~11 MB) and training (~5-10 minutes)
3. **Drawing Feature**: Requires additional library (streamlit-canvas) which user must install
4. **GPU Setup** (Optional): For faster training, CUDA/cuDNN setup is manual

## 💡 How to Improve the App

1. **Better Model**: Train with more epochs or use a pre-trained model from Keras
2. **Data Augmentation**: Add rotation, scaling, distortion to MNIST data before training
3. **Multiple Models**: Ensemble predictions from multiple models
4. **Real-time Drawing**: Use lower latency processing
5. **Model Quantization**: Reduce model size for faster inference

## 📝 Example Test Cases

Try these to test the app:

1. **Clear handwritten digits**: Upload or draw clear, large digits (28×28 pixels or larger)
2. **Blurry digits**: Test how the model handles low-quality images
3. **Thick vs. thin strokes**: Compare predictions for different stroke widths
4. **MNIST test set**: Download sample MNIST images from [Kaggle](https://www.kaggle.com/datasets/scolianni/mnistasjpg)

## 🔗 Resources

- **MNIST Dataset**: [Yann LeCun's MNIST Page](http://yann.lecun.com/exdb/mnist/)
- **TensorFlow Documentation**: [tensorflow.org](https://www.tensorflow.org/)
- **Streamlit Documentation**: [streamlit.io](https://www.streamlit.io/)
- **OpenCV Documentation**: [opencv.org](https://docs.opencv.org/)

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Created by **just-funn**

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

---

**Happy Digit Recognition! 🎉**