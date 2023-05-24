from django.http import JsonResponse


def getRoutes(request):
    routes=[
        {
            'Endpoint': '/notes/',
            'method':'GET',
            'body':'None',
            'description':'Returns an array of notes',
        },
        {
            'Endpoint': '/notes/id',
            'method':'GET',
            'body':'None',
            'description':'Returns a single note object',
        },
        {
            'Endpoint': '/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Create an existing note',
        },
        {
            'Endpoint': '/notes/id/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Create an existing note',
        },
           {
            'Endpoint': '/notes/id/delete',
            'method':'DELETE',
            'body':'None',
            'description':'Delete an existing note',
        },
    ]
    return JsonResponse(routes, safe=False)