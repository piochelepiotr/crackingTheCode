def get_point(image, p):
    i, j = p
    return image[i][j]


def set_point(image, p, value):
    i, j = p
    image[i][j] = value


def rotate_in_place(image):
    """
    To rotate the image in place, we do it in squares, going from the outside to the inside
    Returns:
    None

    Args:
    image list(list(int)): all pixels of the image to rotate
        the image must be square
    """
    n = len(image)
    nbr_squares = n // 2
    for s in range(nbr_squares):
        m = n - 1 - 2 * s
        for i in range(m):
            points = [
                (s, s + i),
                (s + i, n - 1 - s),
                (n - 1 - s, n - 1 - s - i),
                (n - 1 - s - i, s),
            ]
            first = get_point(image, points[0])
            for i in range(3):
                set_point(image, points[i], get_point(image, points[i + 1]))
            set_point(image, points[-1], first)
