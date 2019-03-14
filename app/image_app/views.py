from django.shortcuts import render
from .flicker_api import FlickerAPI

flicker_api = FlickerAPI()

def image_search_get(request):
    text = request.GET.get('text', '')
    sort_type = request.GET.get('sort_type', '')
    page = request.GET.get('page', '')

    if text != "":

        data = flicker_api.find(text, sort_type, page)

        return render(
            request,
            'image_app/index.html',
            {
                'images': data["photos"]["photo"],
                'page_number': data["photos"]["page"],
                'pages': data["photos"]["pages"],
                'sort_types': flicker_api.FLICKER_SORT_TYPES
            }
        )
    
    else:
        return render(
            request,
            'image_app/index.html',
            {
                'images': [],
                'page_number': 1,
                'pages': 1,
                'sort_types': flicker_api.FLICKER_SORT_TYPES
            }
        )


def image_search_post(request):
    text = request.POST['text']
    sort_type = request.POST['sort_type']

    data = flicker_api.find(text, sort_type)
    print(data)

    return render(
        request,
        'image_app/index.html',
        {
            'images': data["photos"]["photo"],
            'page_number': data["photos"]["page"],
            'pages': data["photos"]["pages"],
            'sort_types': flicker_api.FLICKER_SORT_TYPES
        }
    )


def image_search(request):
    if request.method == 'GET':
        return image_search_get(request)
    elif request.method == 'POST':
        return image_search_post(request)
    else:
        return render(
            request,
            'base/method_not_alowed.html',
            {}
        )
