# This file is kept for compatibility, but the main application
# is now configured in app/__init__.py to follow Flask conventions.
# For new code, please reference app directly from __init__.py

from app import app  # noqa: F401

# This ensures the app is available when 'from app.app import app' is used
# in your project, maintaining backward compatibility

# Entry point for running the application directly
if __name__ == "__main__":
    app.run(debug=True)
