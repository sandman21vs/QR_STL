import os
import platform

# Função para instalar bibliotecas necessárias no Windows
def install_windows_requirements():
    os.system("pip install numpy qrcode[pil] numpy-stl")

# Função para instalar bibliotecas necessárias no Linux
def install_linux_requirements():
    os.system("pip install numpy qrcode[pil] numpy-stl")

if __name__ == "__main__":
    # Verifica o sistema operacional
    system_platform = platform.system()
    
    # Instala as bibliotecas necessárias com base no sistema operacional
    if system_platform == "Windows":
        install_windows_requirements()
    elif system_platform == "Linux":
        install_linux_requirements()
    else:
        print("Sistema operacional não suportado.")
        exit()




from stl import mesh
import numpy as np
import qrcode

# Função para gerar o QR code
def generate_qr_code(data, size=200):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=75,  # Tamanho do QR code em mm
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")  # Invertendo as cores
    img = img.convert("L")
    img = img.resize((size, size))
    return img

# Função para criar o arquivo STL com o QR code sobre o cubo
def create_stl_with_qr_on_cube(output_filename, qr_image, cube_scale=100, qr_scale=100, qr_height_mm=3.0):
    cube_width = 200 * (cube_scale / 100.0)  # Calcula a largura do cubo em mm
    cube_height = 1.0 * (cube_scale / 100.0)  # Calcula a altura do cubo em mm
    qr_image = qr_image.resize((int(200 * (qr_scale / 100.0)), int(200 * (qr_scale / 100.0))))  # Redimensiona o QR code

    qr_width, qr_height = qr_image.size  # Obtém as dimensões do QR code

    # Define as coordenadas dos vértices do cubo
    base_vertices = np.array([
        [-cube_width/2, -cube_width/2, 0], [-cube_width/2, cube_width/2, 0],
        [cube_width/2, -cube_width/2, 0], [cube_width/2, cube_width/2, 0],
        [-cube_width/2, -cube_width/2, cube_height], [-cube_width/2, cube_width/2, cube_height],
        [cube_width/2, -cube_width/2, cube_height], [cube_width/2, cube_width/2, cube_height]
    ])

    qr_vertices = []

    for x in range(qr_width):
        for y in range(qr_height):
            qr_thickness = cube_height + (qr_image.getpixel((x, y)) / 255.0 * qr_height_mm)  # Espessura do QR code em mm
            qr_vertices.append([x - qr_width/2, y - qr_height/2, qr_thickness])

    all_vertices = np.concatenate((base_vertices, qr_vertices))

    base_faces = [
        [0, 1, 2], [2, 1, 3],
        [4, 5, 6], [6, 5, 7],
        [0, 4, 1], [1, 4, 5],
        [2, 6, 3], [3, 6, 7],
        [0, 2, 4], [4, 2, 6],
        [1, 5, 3], [3, 5, 7]
    ]

    qr_faces = []

    for x in range(qr_width - 1):
        for y in range(qr_height - 1):
            v0 = x * qr_height + y + len(base_vertices)
            v1 = v0 + 1
            v2 = (x + 1) * qr_height + y + len(base_vertices)
            v3 = v2 + 1
            qr_faces.append([v0, v2, v1])
            qr_faces.append([v1, v2, v3])

    base_bottom_vertex = len(base_vertices) - 4  # Índice do vértice da base inferior

    all_faces = base_faces + qr_faces + [
        [base_bottom_vertex, base_bottom_vertex + 1, base_bottom_vertex + 2],
        [base_bottom_vertex + 1, base_bottom_vertex + 3, base_bottom_vertex + 2],
        [base_bottom_vertex, base_bottom_vertex + 2, base_bottom_vertex + 1],  # Adicionando as faces laterais da base
        [base_bottom_vertex + 1, base_bottom_vertex + 2, base_bottom_vertex + 3]
    ]

    qr_stl = mesh.Mesh(np.zeros(len(all_faces), dtype=mesh.Mesh.dtype))

    for i, f in enumerate(all_faces):
        for j in range(3):
            qr_stl.vectors[i][j] = all_vertices[f[j]]

    qr_stl.save(output_filename)

if __name__ == "__main__":
    qr_data = input("Digite a palavra, frase ou link que deseja transformar em QR code: ")
    qr_image = generate_qr_code(qr_data)

    cube_scale = float(input("Digite a porcentagem de tamanho do cubo (por exemplo, 100 para 100%): "))
    qr_scale = float(input("Digite a porcentagem de tamanho do QR code (por exemplo, 100 para 100%): "))
    qr_height_mm = float(input("Digite a altura do QR code em milímetros: "))
    
    # Define o nome do arquivo STL com base nas configurações
    stl_filename = f"cube_with_qr_{cube_scale}percent_{qr_scale}percent_{qr_height_mm}mm.stl"
    
    # Cria o arquivo STL com o QR code e o cubo
    create_stl_with_qr_on_cube(stl_filename, qr_image, cube_scale, qr_scale, qr_height_mm)
    print(f"Cube with scaled QR code and cube STL file '{stl_filename}' created.")
