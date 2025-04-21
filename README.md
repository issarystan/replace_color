# replace_color

This project is a simple Python script that replaces a specific color in an image with a new one, using the **Pillow** and **NumPy** libraries.

---

## Folder Structure

```
replace_color/
│
├── replace_color.py         # Main script
├── in/                      # Input images
│   ├── image1.png
│   └── ...
├── out/                     # Output images after color replacement
│   ├── image1_modified.png
│   └── ...
└── README.md
```

---

## How It Works

- The script loads an image from the `in/` folder.
- It prompts the user to input:
  - The **old color** to be replaced (RGB format)
  - The **new color** (RGB format)
- It replaces the selected color in all non-transparent pixels.
- The result is saved in the `out/` folder with the same filename.

---

## Example

When running:

```bash
python replace_color.py
```

The terminal will prompt:

```
Введите цвет для замены (R G B): 0 0 0
Введите новый цвет (R G B): 255 255 255
```

This will replace all black (`0,0,0`) pixels with white (`255,255,255`) in the selected image.

---

## Requirements

Install required libraries:

```bash
pip install pillow numpy
```

---

## Notes

- Input and output image paths are currently hardcoded:
  ```python
  image_path = "\in\name.png"
  output_path = "\out\name.png"
  ```
  ➤ You must rename or update these paths manually before running the script.

- Only fully matching RGB values are replaced (with alpha > 0).

---

## Author

**Arystan Issatayev**  
📧 issatayev4@gmail.com  
💬 [@issarystan](https://t.me/issarystan)

---

> This is a simple utility project for learning and experimentation purposes.
