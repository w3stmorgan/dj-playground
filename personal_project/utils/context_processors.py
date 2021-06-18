from django.conf import settings


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}


def add_page_info(request):
    return {
        "app_name": request.resolver_match.app_name,
        "page_path": request.path,
        "user": request.user if request.user.is_authenticated else None,
    }
