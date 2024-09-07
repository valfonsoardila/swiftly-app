from main.server.api.firebase.requests import guides_request


def create_guide(guide_data):
    result = guides_request.create_guide(guide_data)
    return result


def read_guides():
    result = guides_request.read_guides()
    return result


def read_guide(number_od_guide):
    result = guides_request.read_guide(number_od_guide)
    if result:
        return result
    else:
        return "User not found"


def update_guide(number_od_guide, update_data):
    result = guides_request.update_guide(number_od_guide, update_data)
    return result


def delete_guide(number_od_guide):
    result = guides_request.delete_guide(number_od_guide)
    return result
