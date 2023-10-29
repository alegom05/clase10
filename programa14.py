import random

if __name__ == "__main__":
    contenido = "codigo,edad,peso\n"

    codigo_inicial = 0

    linea=''

    for i in range(5):
        codigo = codigo_inicial + i + 1
        a= random.randint(0,50)
        b= round((random.uniform(0,80)),2)
        linea = f"{codigo},{a},{b}\n"
        contenido += linea

    with open("notas14.csv", "w+", encoding="utf-8") as f:
        f.write(contenido)

