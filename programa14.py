import random

if __name__ == "__main__":
    contenido = "codigo,edad,peso\n"

    codigo_inicial = 0

    for i in range(5):
            linea = f"{codigo_inicial + i + 1},"
            for _ in range(2):
                a= random.randint(0,50)
                b= round((random.uniform(0,80)),2)
                linea += f"{a},{b}\n"
            contenido += f"{linea[:-1]}\n"

    with open("notas14.csv", "w+", encoding="utf-8") as f:
        f.write(contenido)

