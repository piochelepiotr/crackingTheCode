def draw_line(screen, width, x1, x2, y):
    s = ""
    first_pixel = y*width + x1
    first_byte = first_pixel // 8
    offset = first_pixel % 8
    s += screen[first_byte] & ((1 << (8 - offset)) - 1)
