from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def paginate_instances(request, instances, per_page=10):
    paginator = Paginator(instances, per_page)
    page = request.GET.get("page", 1)

    try:
        paginator_instances = paginator.page(page)
    except PageNotAnInteger:
        paginator_instances = paginator.page(1)
    except EmptyPage:
        paginator_instances = paginator.page(paginator.num_pages)
    
    next_page_number = 1
    has_next_page = False
    if paginator_instances.has_next():
        has_next_page = True
        next_page_number = paginator_instances.next_page_number()

    has_previous_page = False
    previous_page_number = 1
    if paginator_instances.has_previous():
        has_previous_page = True
        previous_page_number = paginator_instances.previous_page_number()
    
    paginator_response = {
        'current_page': paginator_instances.number,
        'has_next_page': has_next_page,
        'next_page_number': next_page_number,
        'has_previous_page': has_previous_page,
        'previous_page_number': previous_page_number,
        'total_pages': paginator.num_pages,
        'total_items': paginator.count,
        'first_item': paginator_instances.start_index(),
        'last_item': paginator_instances.end_index(),
    }
    
    return paginator_instances, paginator_response


def success_response_data(message, data=None, pagination_data=None):
    response_data = {
        "status_code": 6000,
        "data": data,
        "pagination_data": pagination_data,
        "message": {
            "title": "Success",
            "message": message
        }
    }

    if not pagination_data:
        response_data.pop('pagination_data')

    return response_data

def error_response_data(message):
    response_data = {
        "status_code": 6001,
        "message": {
            "title": "Failed",
            "message": message
        }
    }

    return response_data

def generate_form_errors(form):
    field = ""
    message = ""
    for field in form:
        if field.errors:
            message += field.errors
    for err in form.non_field_errors():
        message += str(err)
    
    return message
