from .deskewImage import deskew_image

views = {
    "DESKEW": deskew_image
}


def get_view(view, *args):
    return views.get(view)(*args)
