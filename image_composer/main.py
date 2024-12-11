import os
from PIL import Image

class ImageProcessor:
    def __init__(self, input_folder, output_folder, overlay_path):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.overlay_path = overlay_path
        self.overlay = Image.open(overlay_path).convert("RGBA")

    def overlay_image(self, image_path, output_path):
        """Sobrepõe a imagem de proporção 1:1 na imagem base e salva no destino."""
        base_image = Image.open(image_path).convert("RGBA")

        resized_overlay = self.overlay.resize(base_image.size)
        combined_image = Image.alpha_composite(base_image, resized_overlay)

        output_image = combined_image.convert("RGB")
        output_image.save(output_path, "JPEG")

    def process_all_images(self):
        """Processa todas as imagens na pasta de entrada."""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(self.output_folder, os.path.splitext(filename)[0] + ".jpg")
                self.overlay_image(input_path, output_path)

    def process_single_image(self, image_name):
        """Processa uma única imagem especificada pelo nome."""
        input_path = os.path.join(self.input_folder, image_name)
        output_path = os.path.join(self.output_folder, os.path.splitext(image_name)[0] + ".jpg")
        if os.path.exists(input_path):
            self.overlay_image(input_path, output_path)
        else:
            print(f"Imagem '{image_name}' não encontrada na pasta '{self.input_folder}'.")

class Menu:
    def __init__(self, processor):
        self.processor = processor

    def display(self):
        """Exibe o menu para o usuário."""
        print("Selecione uma opção:")
        print("1. Processar todas as imagens")
        print("2. Processar uma imagem específica")
        choice = input("Escolha uma opção (1 ou 2): ").strip()

        if choice == "1":
            self.processor.process_all_images()
            print("Todas as imagens foram processadas com sucesso!")
        elif choice == "2":
            image_name = input("Digite o nome da imagem (com extensão): ").strip()
            self.processor.process_single_image(image_name)
            print(f"A imagem '{image_name}' foi processada com sucesso!")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    input_folder = "Originais"
    output_folder = "Editadas"
    overlay_path = "image.png"

    processor = ImageProcessor(input_folder, output_folder, overlay_path)
    menu = Menu(processor)
    menu.display()
