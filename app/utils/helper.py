def generate_slug(name: str) -> str:
    """Generate a URL-friendly slug from a given name."""
    return name.lower().replace(" ", "-")