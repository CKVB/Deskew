from .index import index
from .deskewImage import deskew_image

views = {
    "INDEX": index,
    "DESKEW": deskew_image
}


def get_view(view, *args):
    return views.get(view)(*args)
