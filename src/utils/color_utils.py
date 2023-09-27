from PIL import ImageColor

def alpha(hex_color, opacity):
    rgb_tuple = ImageColor.getcolor(hex_color, "RGB")
    rgb_list = list(rgb_tuple)
    rgb_list.append(opacity)
    rgba = tuple(rgb_list)
    return f"rgba({str(rgba)})"

