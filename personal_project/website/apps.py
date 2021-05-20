from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'personal_project.website'

    def ready(self):
        try:
            import personal_project.users.signals  # noqa F401
        except ImportError:
            pass
