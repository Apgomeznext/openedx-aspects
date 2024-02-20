"""
aspects Django application initialization.
"""

from django.apps import AppConfig


class AspectsConfig(AppConfig):
    """
    Configuration for the aspects Django application.
    """

    name = 'aspects'

    plugin_app = {
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "production": {"relative_path": "settings.production"},
            },
        },
    }

    def ready(self):
        """Load modules of Aspects."""
        from aspects.extensions import (  # pylint: disable=unused-import, import-outside-toplevel
            filters,
        )
