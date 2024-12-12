import tkinter as tk
from PIL import Image, ImageTk
import cv2


def content_viewer(root, slides, go_back):
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Переменная для отслеживания текущего слайда
    current_slide = tk.IntVar(value=0)

    def update_slide():
        """
        Обновляет содержимое слайда в зависимости от текущего индекса.
        """
        # Очистка области слайда
        slide_frame = root.children.get("slide_frame")
        if slide_frame:
            slide_frame.destroy()

        # Создание новой области
        slide_frame = tk.Frame(root, name="slide_frame")
        slide_frame.pack(pady=10)

        # Данные текущего слайда
        slide = slides[current_slide.get()]
        tk.Label(slide_frame, text=f"Slide {current_slide.get() + 1}/{len(slides)}", font=("Arial", 12)).pack()
        tk.Label(slide_frame, text=slide["text"], wraplength=400, justify="left").pack(pady=10)

        # Картинка (если есть)
        if "image" in slide and slide["image"]:
            try:
                image = Image.open(slide["image"])
                image = image.resize((200, 200), Image.Resampling.LANCZOS)
                image_tk = ImageTk.PhotoImage(image)
                tk.Label(slide_frame, image=image_tk).pack(pady=5)
                slide_frame.image_tk = image_tk  # Необходимо сохранить ссылку
            except Exception as e:
                tk.Label(slide_frame, text=f"Error loading image: {e}", fg="red").pack(pady=5)

        # Видео (если есть)
        if "video" in slide and slide["video"]:
            play_video(slide_frame, slide["video"])

    def play_video(slide_frame, video_path):
        """
        Отображает видео в рамке.

        :param slide_frame: Рамка для отображения видео.
        :param video_path: Путь к видеофайлу.
        """
        video_label = tk.Label(slide_frame)
        video_label.pack(pady=5)

        cap = cv2.VideoCapture(video_path)

        def stream():
            ret, frame = cap.read()
            if ret:
                # Конвертация BGR (OpenCV) в RGB (Tkinter)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (400, 300))
                img = ImageTk.PhotoImage(Image.fromarray(frame))
                video_label.config(image=img)
                video_label.image = img
                video_label.after(10, stream)  # Задержка для плавного воспроизведения
            else:
                cap.release()

        stream()

    def next_slide():
        """Переход к следующему слайду."""
        if current_slide.get() < len(slides) - 1:
            current_slide.set(current_slide.get() + 1)
            update_slide()

    def prev_slide():
        """Переход к предыдущему слайду."""
        if current_slide.get() > 0:
            current_slide.set(current_slide.get() - 1)
            update_slide()

    # Заголовок
    tk.Label(root, text="Content Viewer", font=("Arial", 16)).pack(pady=10)

    # Навигационные кнопки
    nav_frame = tk.Frame(root)
    nav_frame.pack(pady=10)
    tk.Button(nav_frame, text="Previous", width=15, command=prev_slide).grid(row=0, column=0, padx=5)
    tk.Button(nav_frame, text="Next", width=15, command=next_slide).grid(row=0, column=1, padx=5)
    tk.Button(nav_frame, text="Back", width=15, command=go_back).grid(row=0, column=2, padx=5)

    # Инициализация первого слайда
    update_slide()


