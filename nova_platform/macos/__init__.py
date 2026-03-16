"""macOS platform tools and skills."""

from nova_platform.macos.skills import register_skills

def register_tools():
    """Register all macOS tools.
    
    Currently returns an empty list as no tools are implemented yet.
    """
    return []

__all__ = ["register_tools", "register_skills"]