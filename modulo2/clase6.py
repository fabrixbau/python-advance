from PIL import Image
import os


def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            # Asegurarse de que el path termine con un separador de directorio
            if not image_folder.endswith(os.path.sep):
                image_folder += os.path.sep

            file_name, file_extension = os.path.splitext(file)
            full_file_path = os.path.join(image_folder, file)
            print("Comprimiendo archivo: " + full_file_path)

            if file_extension.lower() == ".jpg":
                with Image.open(full_file_path) as file_compress:
                    compressed_file_path = os.path.join(
                        image_folder, file_name + "comprimido.jpg"
                    )
                    file_compress.save(
                        compressed_file_path, optimize=True, quality=70)
    except Exception as e:
        print("No se pudo comprimir debido a: " + str(e))


if __name__ == '__main__':
    compress_images("D:/github/python-advance/modulo2/fotos/")
