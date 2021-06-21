from django.http import JsonResponse


def get_response(data, code=200, msg="OK"):
    return JsonResponse({"code": code, "msg": msg, "data": data},
                        content_type="application/json;charset=utf-8",
                        json_dumps_params={'ensure_ascii': False}
                        )
