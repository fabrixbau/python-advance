texto = """
Python es uno de los lenguajes de programación dinámicos más populares
que existen entre los que se encuentran Java, Javascript, Go y C#.
Aunque es considerado a menudo como un lenguaje "scripting",
es realmente un lenguaje de propósito general. En la actualidad,
Python es usado para todo, desde simples "scripts",
hasta grandes servidores web que proveen servicio ininterrumpido 24×7.
Es utilizado para la programación de interfaces gráficas y bases de datos,
programación web tanto en el cliente como en el servidor (véase Django o Flask)
y
testing de aplicaciones. Además tiene una amplia aceptación por científicos que
hacen aplicaciones para las supercomputadores más rápidas del
mundo y por los niños que recién están comenzando a programar."""

texto = texto.replace("Python", "python", 1)
palabra_busqueda = input("Ingrese palabra a buscar : ")
index = texto.find(palabra_busqueda)

if (index != -1):
    print(f"{palabra_busqueda} se encontro en el índice {index}")

    total_encontrados = texto.count(palabra_busqueda)
    print(f"{palabra_busqueda} aparece {total_encontrados} veces")
else:
    print("No se encontro la palabra")
