from PIL import Image, ImageDraw, ImageFont
import os

# Создаем папку static/images если ее нет
os.makedirs('static/images', exist_ok=True)

# Данные для изображений
phones = [
    {'name': 'iphone15.jpg', 'color': (40, 40, 40), 'text': 'iPhone 15 Pro', 'text_color': (255, 255, 255)},
    {'name': 'galaxy24.jpg', 'color': (30, 80, 160), 'text': 'Galaxy S24', 'text_color': (255, 255, 255)},
    {'name': 'pixel8.jpg', 'color': (60, 130, 250), 'text': 'Pixel 8 Pro', 'text_color': (255, 255, 255)},
    {'name': 'oneplus12.jpg', 'color': (235, 0, 40), 'text': 'OnePlus 12', 'text_color': (255, 255, 255)}
]

def create_phone_images():
    for phone in phones:
        # Создаем изображение 400x400 пикселей
        img = Image.new('RGB', (400, 400), color=phone['color'])
        draw = ImageDraw.Draw(img)
        
        # Простой текст (без шрифта, используем базовый)
        try:
            # Пытаемся использовать шрифт
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            # Если шрифт не доступен, используем стандартный
            font = ImageFont.load_default()
        
        # Рисуем текст по центру
        bbox = draw.textbbox((0, 0), phone['text'], font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (400 - text_width) / 2
        y = (400 - text_height) / 2
        
        draw.text((x, y), phone['text'], fill=phone['text_color'], font=font)
        
        # Сохраняем изображение
        img.save(f'static/images/{phone["name"]}', quality=95)
        print(f'Создано: static/images/{phone["name"]}')

if __name__ == '__main__':
    create_phone_images()