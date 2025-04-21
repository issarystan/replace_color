from PIL import Image
import numpy as np

def replace_color(image_path, old_color, new_color, output_path):
    image = Image.open(image_path).convert("RGBA")  # Открываем изображение в формате RGBA
    data = np.array(image)  # Преобразуем в массив

    # Разделяем цветовые каналы
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]

    # Создаем маску: заменяем только пиксели с old_color, но НЕ трогаем полностью прозрачные (a == 0)
    mask = (r == old_color[0]) & (g == old_color[1]) & (b == old_color[2]) & (a > 0)

    # Меняем только цвет (R, G, B), оставляя альфа-канал (прозрачность) без изменений
    data[mask, 0:3] = new_color  # Только RGB, не трогаем A

    # Преобразуем массив обратно в изображение и сохраняем
    new_image = Image.fromarray(data)
    new_image.save(output_path)
    print(f"Изображение сохранено как {output_path}")

# Запрос цвета в формате RGB(0 0 0) через пробел
old_color = tuple(map(int, input("Введите цвет для замены (R G B): ").split()))
new_color = tuple(map(int, input("Введите новый цвет (R G B): ").split()))

# Указываем путь к изображению и выходной файл
image_path = "\in\name.png"
output_path = "\out\name.png"

replace_color(image_path, old_color, new_color, output_path)