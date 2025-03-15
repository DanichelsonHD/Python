def draw_triangle (base: int):
    for i in range(1, base + 1):
        print("*" * i)

draw_triangle(int(input("Digite a base do triângulo: ")))