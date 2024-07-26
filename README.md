# Background Remover Using Python

This project is a Python script that removes the background from an uploaded image, specifically focusing on isolating a person. It uses the `rembg` library, which leverages deep learning models to perform background removal.

![Untitled design](https://github.com/user-attachments/assets/23aeb754-ccd3-48ce-9555-6623f5065de5)


## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Dineshkumaryara/Image-Background-Remover-using-python.git
    cd Image-Background-Remover-using-python
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place Your Image**:

   Place the image you want to process in the `input` directory (create it if it doesn't exist).

2. **Run the Script**:

    ```bash
    python background_remover.py
    ```

3. **Check the Output**:

   The output image with the background removed will be saved in the `output` directory (create it if it doesn't exist).
